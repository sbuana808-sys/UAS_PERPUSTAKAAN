import csv

undo_stack = []


# ==========================
# CREATE
# ==========================
def tambah_buku():

    id_buku = input("ID Buku      : ")
    judul = input("Judul Buku   : ")
    penulis = input("Penulis      : ")
    tahun = input("Tahun Terbit : ")

    with open("buku.csv", "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([id_buku, judul, penulis, tahun])

    print("Buku berhasil ditambahkan.")


# ==========================
# READ
# ==========================
def lihat_buku():

    try:
        with open("buku.csv", "r", encoding="utf-8") as file:

            reader = csv.reader(file)

            print("\n===== DAFTAR BUKU =====")

            for row in reader:
                print(row)

    except FileNotFoundError:
        print("File buku.csv tidak ditemukan.")


# ==========================
# UPDATE
# ==========================
def ubah_buku():

    id_cari = input("Masukkan ID Buku : ")

    data = []

    with open("buku.csv", "r", encoding="utf-8") as file:
        reader = csv.reader(file)

        for row in reader:
            data.append(row)

    ditemukan = False

    for i in range(1, len(data)):

        if data[i][0] == id_cari:

            print("\nData ditemukan")

            data[i][1] = input("Judul baru   : ")
            data[i][2] = input("Penulis baru : ")
            data[i][3] = input("Tahun baru   : ")

            ditemukan = True
            break

    if ditemukan:

        with open("buku.csv", "w", newline="", encoding="utf-8") as file:

            writer = csv.writer(file)
            writer.writerows(data)

        print("Data berhasil diubah")

    else:
        print("ID tidak ditemukan")


# ==========================
# DELETE
# ==========================
def hapus_buku():

    id_cari = input("Masukkan ID Buku : ")

    data = []

    with open("buku.csv", "r", encoding="utf-8") as file:
        reader = csv.reader(file)

        for row in reader:
            data.append(row)

    ditemukan = False

    for i in range(1, len(data)):

        if data[i][0] == id_cari:

            undo_stack.append(data[i])

            del data[i]

            ditemukan = True
            break

    if ditemukan:

        with open("buku.csv", "w", newline="", encoding="utf-8") as file:

            writer = csv.writer(file)
            writer.writerows(data)

        print("Data berhasil dihapus")

    else:
        print("ID tidak ditemukan")


# ==========================
# UNDO DELETE
# ==========================
def undo_hapus():

    if len(undo_stack) == 0:

        print("Tidak ada data yang bisa dikembalikan")
        return


    data = undo_stack.pop()

    with open("buku.csv", "a", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        writer.writerow(data)

    print("Data berhasil dikembalikan")


# ==========================
# SEARCHING
# ==========================
def cari_buku():

    id_cari = input("Masukkan ID Buku : ")

    ditemukan = False

    with open("buku.csv", "r", encoding="utf-8") as file:

        reader = csv.DictReader(file)

        for row in reader:

            if row["id"] == id_cari:

                print("\n===== DATA DITEMUKAN =====")

                print("ID      :", row["id"])
                print("Judul   :", row["judul"])
                print("Penulis :", row["penulis"])
                print("Tahun   :", row["tahun"])

                ditemukan = True

    if not ditemukan:
        print("Data tidak ditemukan")


# ==========================
# SORTING
# ==========================
def urutkan_buku():

    data = []

    with open("buku.csv", "r", encoding="utf-8") as file:

        reader = csv.reader(file)

        for row in reader:
            data.append(row)

    if len(data) <= 1:
        print("Tidak ada data untuk diurutkan")
        return


    header = data[0]
    isi = data[1:]

    isi.sort(key=lambda x: x[1])

    print("\n===== DATA TERURUT =====")

    print(header)

    for row in isi:
        print(row)


# ==========================
# MENU
# ==========================
while True:

    print("\n==============================")
    print("   SISTEM PERPUSTAKAAN")
    print("==============================")

    print("1. Tambah Buku")
    print("2. Lihat Buku")
    print("3. Ubah Buku")
    print("4. Hapus Buku")
    print("5. Cari Buku")
    print("6. Urutkan Buku")
    print("7. Undo Hapus")
    print("8. Keluar")

    pilih = input("\nPilih Menu : ")

    if pilih == "1":
        tambah_buku()

    elif pilih == "2":
        lihat_buku()

    elif pilih == "3":
        ubah_buku()

    elif pilih == "4":
        hapus_buku()

    elif pilih == "5":
        cari_buku()

    elif pilih == "6":
        urutkan_buku()

    elif pilih == "7":
        undo_hapus()

    elif pilih == "8":
        print("Program selesai")
        break

    else:
        print("Pilihan tidak valid")