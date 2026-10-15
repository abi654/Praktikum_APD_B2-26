bagus = ("=" * 65)
bagus_tipis = ("-" * 50)
import os


def clear():
    os.system("cls" if os.name == "nt" else "clear")

clear()

data_user = [
    ["admin", "admin123", "admin"],
    ["abbie", "abbie123", "user"]
]

data_vaksin = [
    [1, "Abbie Mujahiddin Asmuransyah",19, "Covid-19", 1],
    [2, "rolan", 23, "Tetanus", 2]
]

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

            akun_nya = None
            for u in data_user:
                if u[0] == username and u[1] == password:
                    akun_nya = u

            if akun_nya is None:
                print("Username atau password salah!")
            else:
                user_aktif = akun_nya
                print(f"Login berhasil, {user_aktif[0]}!") 
            input("Tekan Enter untuk melanjutkan...")
        elif pilihan == "2":
            os.system("cls" if os.name == "nt" else "clear")
            print("            Register Akun Baru")
            print("Ketik '0' Pada Username untuk kembali ke menu utama")
            batal  = False  

            while True:
                username = input("Username: ").strip().lower()

                if username == "0":
                    batal = True
                    break
                elif len(username) < 4:
                    print("Username minimal 4 karakter!")
                elif " " in username:
                    print("Username tidak boleh mengandung spasi!")
                else:
                    dah_ada = False
                    for u in data_user:
                        if u[0] == username:
                            dah_ada = True
                    if dah_ada:
                        print("Username Sudah Digunakan, Buat yang lain")
                    else:
                        break

            if batal == False:
                while True:
                    password = input("Password: ")
                    if len(password) < 6:
                        print("Password minimal 6 karakter!")
                    else:
                        konfirmasi = input("Konfirmasi Password: ") 
                        if konfirmasi == password:
                            break
                        else:
                            print("Password tidak sama, coba lagi")

                data_user.append([username, password, "user"])
                print("Registrasi berhasil! Silahkan login .")
            else:    
                print("Registrasi dibatalkan")
            input("Tekan Enter untuk melanjutkan...")


       
        elif pilihan == "0":
            print("Terima Kasih Telah Menggunakan Sistem Data Vaksin")
            break
        
        else:
            print("Pilihan tidak valid!")
            input("Tekan Enter untuk melanjutkan...")

    else:
        peran = user_aktif[2]

        print(bagus)
        print("           Sistem Data Vaksin")  
        print(f" login sebagai: {user_aktif[0]} ({peran})")
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

        aksi = ""
        if peran == "admin":
            if pilihan == "1":
                aksi = "tambah"
            elif pilihan == "2":
                aksi = "lihat"
            elif pilihan == "3":
                aksi = "cari"
            elif pilihan == "4":
                aksi = "ubah"
            elif pilihan == "5":
                aksi = "hapus"
            elif pilihan == "6":
                aksi = "logout"
        else:
            if pilihan == "1":
                aksi = "lihat"
            elif pilihan == "2":
                aksi = "cari"
            elif pilihan == "3":
                aksi = "logout"
        os.system("cls" if os.name == "nt" else "clear")

        if aksi == "tambah":
            while True:
                nama = input("Nama Penerima Vaksin: ").strip()
                if  nama== "":
                    print("Nama tidak boleh kosong!")
                elif nama.isalpha() == False:
                    print("Nama hanya boleh berisi huruf")
                else:
                    break

            while True:
                umur = input("Umur (1-100): ")
                if umur.isdigit() == False:
                    print("Umur harus berupa angka!")
                elif int(umur) < 1 or int(umur) > 100:
                    print("Umur harus antara 1-100")
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
                id_baru = data_vaksin[-1][0] + 1

            data_vaksin.append([id_baru, nama, umur, vaksin, dosis])
            print("Data berhasil ditambahkan!")

        elif aksi == "lihat":
            print("     Daftar Data Vaksin:")
            if len(data_vaksin) == 0:
                print("Belum ada data vaksin")
            else:
                print(bagus)
                print(f"{'ID':<5}{'Nama':<30}{'Umur':<8}{'Jenis Vaksin':<15}{'Dosis':<6}")
                print(bagus)
                for d in data_vaksin:
                    print(f"{d[0]:<5}{d[1]:<30}{d[2]:<8}{d[3]:<15}{d[4]:<6}")
                print(bagus)
                print(f"Total data: {len(data_vaksin)}")   
        elif aksi == "cari":
            print("     CARI DATA VAKSIN ")
            kata_kunci = input("Masukkan nama yang dicari: ").strip().lower()

            if kata_kunci == "":
                print("Kata kunci tidak boleh kosong!")
            else:
                ditemukan = False
                print(bagus)
                print(f"{'ID':<5}{'Nama':<30}{'Umur':<8}{'Jenis Vaksin':<15}{'Dosis':<6}")
                print(bagus)
                for d in data_vaksin:
                    if kata_kunci in d[1].lower():
                        print(f"{d[0]:<5}{d[1]:<30}{d[2]:<8}{d[3]:<15}{d[4]:<6}")
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
                for d in data_vaksin:
                    print(f"{d[0]:<5}{d[1]:<30}{d[2]:<8}{d[3]:<15}{d[4]:<6}")
                print(bagus)

                ubah = input("Masukkan ID yang ingin diubah: ")

               
                data = None
                if  ubah.isdigit():
                    for d in data_vaksin:
                        if d[0] == int(ubah):
                            data = d
                if data is None:
                    print("ID tidak valid atau tidak ditemukan!")
                else:
                    print("(Kosongkan lalu tekan Enter jika tidak ingin mengubah)")
                    nama_baru = input(f"Nama [{data[1]}]: ").strip()
                    umur_baru = input(f"Umur [{data[2]}]: ").strip()
                    vaksin_baru = input(f"Vaksin [{data[3]}]: ").strip()
                    dosis_baru = input(f"Dosis [{data[4]}]: ").strip()

                    print()
                    if nama_baru != "":
                        if nama_baru.replace(" ", "").isalpha():
                            data[1] = nama_baru
                        else:
                            print("Nama hanya boleh huruf, nama tidak diubah.")

                    if umur_baru != "":
                        if umur_baru.isdigit() and 1 <= int(umur_baru) <= 120:
                            data[2] = int(umur_baru)
                        else:
                            print("Umur harus angka 1-120, umur tidak diubah.")

                    if vaksin_baru != "":
                        data[3] = vaksin_baru

                    if dosis_baru != "":
                        if dosis_baru.isdigit() and 1 <= int(dosis_baru) <= 3:
                            data[4] = int(dosis_baru)
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
                print("=" * 60)
                for d in data_vaksin:
                    print(f"{d[0]:<5}{d[1]:<30}{d[2]:<8}{d[3]:<15}{d[4]:<6}")
                print(bagus)

                id_hapus = input("Masukkan ID yang ingin dihapus: ")

                data = None
                if id_hapus.isdigit():
                    for d in data_vaksin:
                        if d[0] == int(id_hapus):
                            data = d

                if data is None:
                    print("ID tidak valid atau tidak ditemukan!")
                else:
                    yakin = input(f"Yakin hapus data '{data[1]}'? (y/t): ").strip().lower()
                    if yakin == "y":
                        data_vaksin.remove(data)
                        print("Data berhasil dihapus!")
                    elif yakin == "t":
                        print("Penghapusan dibatalkan.")
                    else:
                        print("Input tidak valid, penghapusan dibatalkan.")

        
        elif aksi == "logout":
            user_aktif = None
            print("Logout berhasil.")

        else:
            print("Pilihan tidak valid!")

        input("Tekan Enter untuk kembali ke menu...")
                    
                