class Buku:
    def __init__(self, judul, pengarang, tahun_terbit, isbn):
        self.__judul = judul
        self.__pengarang = pengarang
        self.__tahun_terbit = tahun_terbit
        self.__isbn = isbn
        self.__status = "tersedia"

    def tampilkan_info_buku(self):
        print(f"Judul       : {self.__judul}")
        print(f"Pengarang   : {self.__pengarang}")
        print(f"Tahun Terbit: {self.__tahun_terbit}")
        print(f"ISBN        : {self.__isbn}")
        print(f"Status      : {self.__status}")

    def pinjam(self):
        if self.__status == "tersedia":
            self.__status = "dipinjam"
            return True
        return False

    def kembalikan(self):
        self.__status = "tersedia"

    def is_tersedia(self):
        return self.__status == "tersedia"


class BukuDigital(Buku):
    def __init__(self, judul, pengarang, tahun_terbit, isbn, ukuran_file):
        super().__init__(judul, pengarang, tahun_terbit, isbn)
        self.__ukuran_file = ukuran_file

    def tampilkan_info_buku(self):
        super().tampilkan_info_buku()
        print(f"Ukuran File : {self.__ukuran_file} MB")


class Anggota:
    def __init__(self, nama, nomor_anggota, alamat):
        self.__nama = nama
        self.__nomor_anggota = nomor_anggota
        self.__alamat = alamat
        self.__daftar_pinjaman = []

    def tampilkan_info_anggota(self):
        print(f"Nama          : {self.__nama}")
        print(f"Nomor Anggota : {self.__nomor_anggota}")
        print(f"Alamat        : {self.__alamat}")
        print("Buku yang dipinjam:")
        for buku in self.__daftar_pinjaman:
            print(f"- {buku._Buku__judul}")  # Mengakses atribut privat kelas Buku

    def pinjam_buku(self, buku):
        self.__daftar_pinjaman.append(buku)

    def kembalikan_buku(self, buku):
        if buku in self.__daftar_pinjaman:
            self.__daftar_pinjaman.remove(buku)


class Perpustakaan:
    def __init__(self):
        self.__daftar_buku = []
        self.__daftar_anggota = []

    def tambah_buku(self, buku):
        self.__daftar_buku.append(buku)

    def daftar_buku_tersedia(self):
        print("Daftar Buku Tersedia:")
        for buku in self.__daftar_buku:
            if buku.is_tersedia():
                buku.tampilkan_info_buku()
                print("-" * 20)

    def tambah_anggota(self, anggota):
        self.__daftar_anggota.append(anggota)

    def pinjam_buku(self, nomor_anggota, isbn):
        anggota = next((a for a in self.__daftar_anggota if a._Anggota__nomor_anggota == nomor_anggota), None)
        buku = next((b for b in self.__daftar_buku if b._Buku__isbn == isbn), None)

        if anggota and buku and buku.pinjam():
            anggota.pinjam_buku(buku)
            print("Buku berhasil dipinjam!")
        else:
            print("Buku tidak tersedia atau anggota tidak ditemukan.")

    def kembalikan_buku(self, nomor_anggota, isbn):
        anggota = next((a for a in self.__daftar_anggota if a._Anggota__nomor_anggota == nomor_anggota), None)
        buku = next((b for b in self.__daftar_buku if b._Buku__isbn == isbn), None)

        if anggota and buku:
            anggota.kembalikan_buku(buku)
            buku.kembalikan()
            print("Buku berhasil dikembalikan!")
        else:
            print("Buku atau anggota tidak ditemukan.")


# Fungsi Utama
def main():
    perpustakaan = Perpustakaan()

    while True:
        print("\n=== Menu Perpustakaan ===")
        print("1. Tambah Buku")
        print("2. Daftar Buku Tersedia")
        print("3. Tambah Anggota")
        print("4. Pinjam Buku")
        print("5. Kembalikan Buku")
        print("6. Tampilkan Info Anggota")
        print("0. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            judul = input("Judul: ")
            pengarang = input("Pengarang: ")
            tahun_terbit = input("Tahun Terbit: ")
            isbn = input("ISBN: ")
            buku = Buku(judul, pengarang, tahun_terbit, isbn)
            perpustakaan.tambah_buku(buku)
            print("Buku berhasil ditambahkan!")
        elif pilihan == "2":
            perpustakaan.daftar_buku_tersedia()
        elif pilihan == "3":
            nama = input("Nama: ")
            nomor_anggota = input("Nomor Anggota: ")
            alamat = input("Alamat: ")
            anggota = Anggota(nama, nomor_anggota, alamat)
            perpustakaan.tambah_anggota(anggota)
            print("Anggota berhasil ditambahkan!")
        elif pilihan == "4":
            nomor_anggota = input("Nomor Anggota: ")
            isbn = input("ISBN Buku: ")
            perpustakaan.pinjam_buku(nomor_anggota, isbn)
        elif pilihan == "5":
            nomor_anggota = input("Nomor Anggota: ")
            isbn = input("ISBN Buku: ")
            perpustakaan.kembalikan_buku(nomor_anggota, isbn)
        elif pilihan == "6":
            nomor_anggota = input("Nomor Anggota: ")
            anggota = next((a for a in perpustakaan._Perpustakaan__daftar_anggota if a._Anggota__nomor_anggota == nomor_anggota), None)
            if anggota:
                anggota.tampilkan_info_anggota()
            else:
                print("Anggota tidak ditemukan.")
        elif pilihan == "0":
            print("Terima kasih telah menggunakan aplikasi perpustakaan!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


if __name__ == "__main__":
    main()
