from collections import deque

# data mahasiswa pakai array

mahasiswa = [
    ["1255011001", "Andi", "Teknik Informatika"],
    ["1255011002", "Budi", "Teknik Informatika"],
    ["1255011003", "Citra", "Teknik Informatika"]
]

# stack - fitur untuk undo

stack_undo = []

# queue - untuk antrean

antrian = deque()

# hash table - untuk pencarian nim nya

data_nim = {}

for data in mahasiswa:
    data_nim[data[0]] = data

# untuk nampilin data mahasiswa

def tampilkan_data():
    print("\n=== DATA MAHASISWA ===")

    for data in mahasiswa:
        print(
            "NIM   :", data[0],
            "| Nama :", data[1],
            "| Prodi:", data[2]
        )

#untuk tambah mahasiswa

def tambah_mahasiswa():
    print("\n=== TAMBAH MAHASISWA ===")

    nim = input("NIM   : ")
    nama = input("Nama  : ")
    prodi = input("Prodi : ")

    data_baru = [nim, nama, prodi]

    # Array
    mahasiswa.append(data_baru)

    # Hash Table
    data_nim[nim] = data_baru

    # Stack
    stack_undo.append(data_baru)

    print("Data mahasiswa berhasil ditambahkan.")

# sistem undo

def undo():
    print("\n=== UNDO ===")

    if not stack_undo:
        print("Tidak ada aktivitas yang dapat di-Undo.")
        return

    data_terakhir = stack_undo.pop()

    mahasiswa.remove(data_terakhir)
    del data_nim[data_terakhir[0]]

    print("Data terakhir berhasil di-Undo.")

#sistem tambah ke antrean

def tambah_antrian():
    print("\n=== TAMBAH KE ANTREAN ===")

    nim = input("Masukkan NIM: ")

    if nim in data_nim:
        antrian.append(data_nim[nim])
        print(data_nim[nim][1], "berhasil masuk antrean.")
    else:
        print("NIM tidak ditemukan.")

#sistem untuk proses antrean

def proses_antrian():
    print("\n=== PROSES ANTREAN ===")

    if not antrian:
        print("Antrean kosong.")
        return

    data = antrian.popleft()

    print(
        "Memproses:",
        data[1],
        "-",
        data[0]
    )

#untuk cari mahasiswa

def cari_mahasiswa():
    print("\n=== CARI MAHASISWA ===")

    nim = input("Masukkan NIM: ")

    if nim in data_nim:
        data = data_nim[nim]

        print("Data ditemukan:")
        print("NIM   :", data[0])
        print("Nama  :", data[1])
        print("Prodi :", data[2])
    else:
        print("Data mahasiswa tidak ditemukan.") 

#program utama
while True:

    print("\n==============================")
    print("       SISTEM AKADEMIK")
    print("==============================")
    print("1. Tampilkan Data Mahasiswa")
    print("2. Tambah Mahasiswa")
    print("3. Undo")
    print("4. Tambah ke Antrean")
    print("5. Proses Antrean")
    print("6. Cari Mahasiswa")
    print("7. Keluar")
    print("==============================")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tampilkan_data()

    elif pilihan == "2":
        tambah_mahasiswa()

    elif pilihan == "3":
        undo()

    elif pilihan == "4":
        tambah_antrian()

    elif pilihan == "5":
        proses_antrian()

    elif pilihan == "6":
        cari_mahasiswa()

    elif pilihan == "7":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak tersedia.")