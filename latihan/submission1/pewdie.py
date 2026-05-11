from google_play_scraper import app, reviews, Sort, reviews_all
from googleapiclient.discovery import build

import pandas as pd

API_KEY = "AIzaxxxxxxxxxxxxxxxxxxxxxxxxxxx"
VIDEO_ID = "VGt-BZ-SxGI"


def get_comments(vidid):
    youtube = build("youtube", "v3", developerKey=API_KEY)

    comments = []

    request = youtube.commentThreads().list(
        part="snippet", videoId=vidid, maxResults=100000, textFormat="plainText"
    )
    response = request.execute()

    while response:
        for item in response["items"]:
            comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
            likes = item["snippet"]["topLevelComment"]["snippet"]["likeCount"]
            comments.append([comment, likes])

        if "nextPageToken" in response:
            request = youtube.commentThreads().list(
                part="snippet",
                videoId=vidid,
                pageToken=response["nextPageToken"],
                maxResults=100000,
            )
            response = request.execute()
        else:
            break

    return comments


data = get_comments(VIDEO_ID)
df = pd.DataFrame(data, columns=["Comment", "Likes"])

df.to_csv("./youtube_comments.csv", index=False)
print(f"Berhasil mengambil {len(df)} komentar!")
