# Contoh program dengan list panjang dan komentar
mahasiswa = [
    {"nama": "John", "usia": 20, "nilai": 85},
    {"nama": "Jane", "usia": 22, "nilai": 90},
    {"nama": "Bob", "usia": 21, "nilai": 78},
    {"nama": "Alice", "usia": 23, "nilai": 95},
]

# Menampilkan informasi mahasiswa
for mhs in mahasiswa:
    print(f"Nama: {mhs['nama']}, Usia: {mhs['usia']}, Nilai: {mhs['nilai']}")

# Menghitung rata-rata nilai mahasiswa
total_nilai = sum(mhs["nilai"] for mhs in mahasiswa)
rata_rata_nilai = total_nilai / len(mahasiswa)
print(f"\nRata-rata Nilai Mahasiswa: {rata_rata_nilai}")

# Menampilkan mahasiswa yang mendapatkan nilai di atas rata-rata
print("\nMahasiswa dengan Nilai di Atas Rata-rata:")
for mhs in mahasiswa:
    if mhs["nilai"] > rata_rata_nilai:
        print(f"{mhs['nama']} - Nilai: {mhs['nilai']}")

# Menambahkan informasi tambahan pada setiap mahasiswa
for mhs in mahasiswa:
    mhs["status"] = "Lulus" if mhs["nilai"] >= 70 else "Tidak Lulus"

# Menampilkan informasi mahasiswa setelah penambahan informasi
print("\nInformasi Mahasiswa Setelah Penambahan Status:")
for mhs in mahasiswa:
    print(f"Nama: {mhs['nama']}, Usia: {mhs['usia']}, Status: {mhs['status']}")