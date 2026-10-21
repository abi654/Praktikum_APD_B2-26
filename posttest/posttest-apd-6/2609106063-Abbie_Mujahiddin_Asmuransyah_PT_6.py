import os

bagus = "=" * 65
bagus_tipis = "-" * 50


def clear():
    os.system("cls" if os.name == "nt" else "clear")


clear()

data_user = {
    "admin": {"password": "admin123", "role": "admin"},
    "abbie": {"password": "abbie123", "role": "user"},
}

data_vaksin = {
    1: {"nama": "Abbie Mujahiddin Asmuransyah", "umur": 19, "vaksin": "Covid-19", "dosis": 1},
    2: {"nama": "rolan", "umur": 23, "vaksin": "Tetanus", "dosis": 2},
}

menu_admin = {
    "1": "tambah",
    "2": "lihat",
    "3": "cari",
    "4": "ubah",
    "5": "hapus",
    "6": "logout",
}
menu_user = {
    "1": "lihat",
    "2": "cari",
    "3": "logout",
}

user_aktif = None

while True:
    os.system("cls" if os.name == "nt" else "clear")
    if user_aktif is None:
        print(bagus)
        print("            Sistem Data Vaksin")
        print(bagus)
        print("1. Login")
        print("2. Register")
        print("0. Keluar")
        print(bagus)

        pilihan = input("Pilih Menu (0-2): ")

        if pilihan == "1":
            os.system("cls" if os.name == "nt" else "clear")
            print("            Login")
            username = input("Username: ").strip().lower()
            password = input("Password: ")

            if username in data_user and data_user[username]["password"] == password:
                user_aktif = {
                    "username": username,
                    "role": data_user[username]["role"],
                }
                print(f"Login berhasil, {user_aktif['username']}!")
            else:
                print("Username atau password salah")
            input("Tekan Enter untuk melanjutkan...")

        elif pilihan == "2":
            os.system("cls" if os.name == "nt" else "clear")
            print("            Register Akun Baru")
            print("Ketik '0' Pada Username untuk kembali ke menu utama")
            batal = False

            while True:
                username = input("Username: ").strip().lower()

                if username == "0":
                    batal = True
                    break
                elif len(username) < 4:
                    print("Username minimal 4 karakter")
                elif " " in username:
                    print("Username tidak boleh mengandung spasi")
                elif username in data_user:
                    print("Username Sudah Digunakan, Buat yang lain")
                else:
                    break

            if batal == False:
                while True:
                    password = input("Password: ")
                    if len(password) < 6:
                        print("Password minimal 6 karakter")
                    else:
                        konfirmasi = input("Konfirmasi Password: ")
                        if konfirmasi == password:
                            break
                        else:
                            print("Password tidak sama, coba lagi")

                data_user[username] = {"password": password, "role": "user"}
                print("Registrasi berhasil! Silahkan login .")
            else:
                print("Registrasi dibatalkan")
            input("Tekan Enter untuk melanjutkan...")

        elif pilihan == "0":
            print("Terima Kasih Telah Menggunakan Sistem Data Vaksin")
            break

        else:
            print("Pilihan tidak valid")
            input("Tekan Enter untuk melanjutkan...")

    else:
        peran = user_aktif["role"]

        print(bagus)
        print("           Sistem Data Vaksin")
        print(f" login sebagai: {user_aktif['username']} ({peran})")
        print(bagus)

        if peran == "admin":
            print("1. Tambah Data ")
            print("2. Lihat Data ")
            print("3. Cari Data ")
            print("4. Ubah Data ")
            print("5. Hapus Data ")
            print("6. Logout")
        else:
            print("1. Lihat Data ")
            print("2. Cari Data ")
            print("3. Logout")
        print(bagus)

        pilihan = input("Pilih Menu: ")

        if peran == "admin":
            aksi = menu_admin.get(pilihan, "")
        else:
            aksi = menu_user.get(pilihan, "")
        os.system("cls" if os.name == "nt" else "clear")

        if aksi == "tambah":
            while True:
                nama = input("Nama Penerima Vaksin: ").strip()
                if nama == "":
                    print("Nama tidak boleh kosong")
                elif nama.replace(" ", "").isalpha() == False:
                    print("Nama hanya boleh berisi huruf")
                else:
                    break

            while True:
                umur = input("Umur (1-120): ")
                if umur.isdigit() == False:
                    print("Umur harus berupa angka")
                elif int(umur) < 1 or int(umur) > 120:
                    print("Umur harus antara 1-120")
                else:
                    umur = int(umur)
                    break

            while True:
                vaksin = input("Jenis Vaksin: ").strip()
                if vaksin == "":
                    print("Jenis vaksin tidak boleh kosong")
                else:
                    break

            while True:
                dosis = input("Dosis (1-3): ")
                if dosis.isdigit() == False:
                    print("Dosis harus berupa angka")
                elif int(dosis) < 1 or int(dosis) > 3:
                    print("Dosis harus antara 1-3")
                else:
                    dosis = int(dosis)
                    break

            if len(data_vaksin) == 0:
                id_baru = 1
            else:
                id_baru = max(data_vaksin) + 1

            data_vaksin[id_baru] = {
                "nama": nama,
                "umur": umur,
                "vaksin": vaksin,
                "dosis": dosis,
            }
            print("Data berhasil ditambahkan!")

        elif aksi == "lihat":
            print("     Daftar Data Vaksin:")
            if len(data_vaksin) == 0:
                print("Belum ada data vaksin")
            else:
                print(bagus)
                print(f"{'ID':<5}{'Nama':<30}{'Umur':<8}{'Jenis Vaksin':<15}{'Dosis':<6}")
                print(bagus)
                for id_vaksin, d in data_vaksin.items():
                    print(f"{id_vaksin:<5}{d['nama']:<30}{d['umur']:<8}{d['vaksin']:<15}{d['dosis']:<6}")
                print(bagus)
                print(f"Total data: {len(data_vaksin)}")

        elif aksi == "cari":
            print("     CARI DATA VAKSIN ")
            kata_kunci = input("Masukkan nama yang dicari: ").strip().lower()

            if kata_kunci == "":
                print("Kata kunci tidak boleh kosong")
            else:
                ditemukan = False
                print(bagus)
                print(f"{'ID':<5}{'Nama':<30}{'Umur':<8}{'Jenis Vaksin':<15}{'Dosis':<6}")
                print(bagus)
                for id_vaksin, d in data_vaksin.items():
                    if kata_kunci in d["nama"].lower():
                        print(f"{id_vaksin:<5}{d['nama']:<30}{d['umur']:<8}{d['vaksin']:<15}{d['dosis']:<6}")
                        ditemukan = True
                print(bagus)

                if ditemukan == False:
                    print("Data tidak ditemukan.")

        elif aksi == "ubah":
            print("     UBAH DATA VAKSIN ")
            if len(data_vaksin) == 0:
                print("Belum ada data.")
            else:
                print(bagus)
                print(f"{'ID':<5}{'Nama':<30}{'Umur':<8}{'Jenis Vaksin':<15}{'Dosis':<6}")
                print(bagus)
                for id_vaksin, d in data_vaksin.items():
                    print(f"{id_vaksin:<5}{d['nama']:<30}{d['umur']:<8}{d['vaksin']:<15}{d['dosis']:<6}")
                print(bagus)

                ubah = input("Masukkan ID yang ingin diubah: ")

                data = None
                if ubah.isdigit() and int(ubah) in data_vaksin:
                    data = data_vaksin[int(ubah)]

                if data is None:
                    print("ID tidak valid atau tidak ditemukan")
                else:
                    print("(Kosongkan lalu tekan Enter jika tidak ingin mengubah)")
                    nama_baru = input(f"Nama [{data['nama']}]: ").strip()
                    umur_baru = input(f"Umur [{data['umur']}]: ").strip()
                    vaksin_baru = input(f"Vaksin [{data['vaksin']}]: ").strip()
                    dosis_baru = input(f"Dosis [{data['dosis']}]: ").strip()

                    print()
                    if nama_baru != "":
                        if nama_baru.replace(" ", "").isalpha():
                            data["nama"] = nama_baru
                        else:
                            print("Nama hanya boleh huruf, nama tidak diubah.")

                    if umur_baru  != "":
                        if umur_baru.isdigit() and 1 <= int(umur_baru) <= 120:
                            data["umur"] = int(umur_baru)
                        else:
                            print("Umur harus angka 1-120, umur tidak diubah.")

                    if vaksin_baru != "":
                        data["vaksin"] = vaksin_baru

                    if dosis_baru != "":
                        if dosis_baru.isdigit() and 1 <= int(dosis_baru) <= 3:
                            data["dosis"] = int(dosis_baru)
                        else:
                            print("Dosis harus angka 1-3, dosis tidak diubah.")

                    print("Proses ubah data selesai.")

        elif aksi == "hapus":
            print("     HAPUS DATA VAKSIN ")
            if len(data_vaksin) == 0:
                print("Belum ada data.")
            else:
                print(bagus)
                print(f"{'ID':<5}{'Nama':<30}{'Umur':<8}{'Jenis Vaksin':<15}{'Dosis':<6}")
                print(bagus)
                for id_vaksin, d in data_vaksin.items():
                    print(f"{id_vaksin:<5}{d['nama']:<30}{d['umur']:<8}{d['vaksin']:<15}{d['dosis']:<6}")
                print(bagus)

                id_hapus = input("Masukkan ID yang ingin dihapus: ")

                data = None
                if id_hapus.isdigit() and int(id_hapus) in data_vaksin:
                    data = data_vaksin[int(id_hapus)]

                if data is None:
                    print("ID tidak valid atau tidak ditemukan")
                else:
                    yakin = input(f"Yakin hapus data '{data['nama']}'? (y/t): ").strip().lower()
                    if yakin == "y":
                        del data_vaksin[int(id_hapus)]
                        print("Data berhasil dihapus!")
                    elif yakin == "t":
                        print("Penghapusan dibatalkan.")
                    else:
                        print("Input tidak valid, penghapusan dibatalkan.")

        elif aksi == "logout":
            user_aktif = None
            print("Logout berhasil.")

        else:
            print("Pilihan tidak valid")

        input("Tekan Enter untuk kembali ke menu...")
