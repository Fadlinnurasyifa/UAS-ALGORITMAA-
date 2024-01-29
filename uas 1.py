# Contoh program dengan perulangan while panjang
total = 0
counter = 1

while counter <= 20:
    if counter % 3 == 0:
        total += counter
    elif counter % 5 == 0:
        total -= counter
    else:
        total *= counter

    if total > 1000:
        break  # Keluar dari perulangan jika total melebihi 1000

    counter += 1

print("Total hasil operasi: ", total)

# Contoh program lain dengan perulangan while panjang
angka = 1
pangkat = 0

while angka <= 10:
    pangkat = 1

    while pangkat <= 5:
        hasil = angka ** pangkat
        print(f"{angka} pangkat {pangkat} adalah: {hasil}")

        if hasil > 100:
            break  # Keluar dari perulangan dalam jika hasil pangkat melebihi 100

        pangkat += 1
    angka += 1