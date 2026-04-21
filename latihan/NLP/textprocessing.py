import re
import string

# Contoh teks
teks_asli = "Ini Adalah Contoh Teks yang Akan Dikonversi Menjadi Lowercase."

# Mengubah teks menjadi lowercase
teks_lowercase = teks_asli.lower()

# Menampilkan hasil
print("Teks asli: ", teks_asli)
print("Teks setelah diubah menjadi lowercase: ", teks_lowercase)


# Fungsi untuk menghapus angka dari teks
def hapus_angka(teks):
    teks_tanpa_angka = "".join([char for char in teks if not char.isdigit()])
    return teks_tanpa_angka


# Contoh teks dengan angka
teks_dengan_angka = "Ini adalah contoh teks dengan angka 12345 yang akan dihapus."

# Memanggil fungsi untuk menghapus angka
teks_tanpa_angka = hapus_angka(teks_dengan_angka)

# Menampilkan hasil
print("Teks dengan angka: ", teks_dengan_angka)
print("Teks tanpa angka: ", teks_tanpa_angka)


def hapus_angka_tidak_relevan(teks):
    # Menggunakan regex untuk mengidentifikasi dan menghapus angka yang tidak relevan
    # Pola untuk mengenali angka yang harus dihapus, termasuk nomor rumah dan nomor telepon
    pola_angka_tidak_relevan = r"\b(?:\d{1,3}[-\.\s]?)?(?:\d{3}[-\.\s]?)?\d{4,}\b"
    hasil = re.sub(pola_angka_tidak_relevan, "", teks)
    return hasil.strip()


# Contoh kalimat dengan angka
kalimat = "Di sini ada 3 nomor rumah yaitu  123, 456, dan 789. Silakan hubungi 081234567890 untuk informasi lebih lanjut."

# Memanggil fungsi untuk menghapus angka tidak relevan
hasil_tanpa_angka = hapus_angka_tidak_relevan(kalimat)

# Menampilkan hasil
print("Kalimat dengan angka: ", kalimat)
print("Kalimat tanpa angka tidak relevan: ", hasil_tanpa_angka)


def remove_punctuation(text):
    # Membuat set yang berisi semua tanda baca
    punctuation_set = set(string.punctuation)

    # Menghapus tanda baca dari teks
    text_without_punctuation = "".join(
        char for char in text if char not in punctuation_set
    )

    return text_without_punctuation


# Contoh teks dengan tanda baca
teks_asli = "Ini adalah contoh teks, dengan tanda baca! Contoh ini, digunakan? untuk demonstrasi."

# Menghapus tanda baca dari teks
teks_tanpa_tanda_baca = remove_punctuation(teks_asli)

# Menampilkan hasil
print("Teks asli: ", teks_asli)
print("Teks setelah menghapus tanda baca: ", teks_tanpa_tanda_baca)

# Menghapus whitespaces dengan strip()
