# Contoh program dengan if-else panjang
nilai = float(input("Masukkan nilai Anda: "))

if nilai >= 90:
    print("Nilai Anda adalah A.")
elif nilai >= 80:
    print("Nilai Anda adalah B.")
elif nilai >= 70:
    print("Nilai Anda adalah C.")
elif nilai >= 60:
    print("Nilai Anda adalah D.")
else:
    print("Maaf, Anda tidak lulus. Nilai Anda adalah E.")

# Contoh lain dengan if-else panjang
umur = int(input("Berapa umur Anda? "))

if umur < 0:
    print("Masukkan umur yang valid.")
elif umur < 18:
    print("Anda masih di bawah umur.")
elif umur < 30:
    print("Anda masih muda.")
elif umur < 50:
    print("Anda sudah dewasa.")
else:
    print("Anda sudah tua.")
    