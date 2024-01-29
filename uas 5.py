#Belajar bahasa inggris
import random

# Kosakata Bahasa Inggris dan Artinya
kosakata = {
    "cat": "kucing",
    "dog": "anjing",
    "book": "buku",
    "pen": "pulpen",
    "table": "meja",
    "love": "cinta"
    
    # Tambahkan lebih banyak kosakata sesuai kebutuhan
}

#Pengguna memilih antara latihan kosakata, ujian kosakata, atau keluar dari program
def belajar_kosakata():
    print("Selamat datang di Program Belajar Bahasa Inggris!")
    print("Pilihan Menu:")
    print("1. Latihan Kosakata")
    print("2. Ujian Kosakata")
    print("3. Keluar")

    pilihan = input("Masukkan nomor menu yang diinginkan: ")

    if pilihan == '1':
        latihan_kosakata()
    elif pilihan == '2':
        ujian_kosakata()
elif pilihan == '3':
        print("Terima kasih. Sampai jumpa!")
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
        belajar_kosakata()

#Memilih secara acak beberapa kata dari kamus dan meminta pengguna untuk menebak artinya
def latihan_kosakata():
    print("\nLatihan Kosakata:")
    for _ in range(5):  # Lima pertanyaan
        kata_inggris, arti = random.choice(list(kosakata.items()))
        jawaban_pengguna = input(f"Arti dari '{kata_inggris}' adalah: ").lower()

        if jawaban_pengguna == arti.lower():
            print("Benar! Selamat!")
        else:
            print(f"Salah. Jawaban yang benar adalah: {arti}")

#Memberikan pertanyaan mengenai arti kata secara acak dari seluruh kamus
def ujian_kosakata():
    print("\nUjian Kosakata:")
    skor = 0
    for kata_inggris, arti in kosakata.items():
        jawaban_pengguna = input(f"Arti dari '{kata_inggris}' adalah: ").lower()

        if jawaban_pengguna == arti.lower():
            print("Benar!")
            skor += 1
        else:
            print(f"Salah. Jawaban yang benar adalah: {arti}")

    print(f"\nSelesai! Skor Anda: {skor}/{len(kosakata)}")

if _name_ == "_main_":
    belajar_kosakata()