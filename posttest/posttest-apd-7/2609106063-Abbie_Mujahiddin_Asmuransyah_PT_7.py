import os

bagus = "=" * 65
bagus_tipis = "-" * 50

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
program_berjalan = True


def validasi_nama(teks):
    nama = teks.strip()
    if nama == "":
        raise ValueError("Nama tidak boleh kosong")
    if not nama.replace(" ", "").isalpha():
        raise ValueError("Nama hanya boleh berisi huruf")
    return nama


def validasi_angka(teks, label, minimum, maksimum):
    try:
        angka = int(teks)
    except ValueError:
        raise ValueError(f"{label} harus berupa angka") from None
    if angka < minimum or angka > maksimum:
        raise ValueError(f"{label} harus antara {minimum}-{maksimum}")
    return angka


def cek_login(username, password):
    try:
        akun = data_user[username]
    except KeyError:
        raise ValueError("Username atau password salah") from None
    if akun["password"] != password:
        raise ValueError("Username atau password salah")
    return akun["role"]


def cari_rekursif(data, daftar_id, kata_kunci, indeks=0):
    if indeks >= len(daftar_id):
        return []
    id_sekarang = daftar_id[indeks]
    cocok = []
    if kata_kunci in data[id_sekarang]["nama"].lower():
        cocok = [id_sekarang]
    return cocok + cari_rekursif(data, daftar_id, kata_kunci, indeks + 1)


def input_angka(pesan, label, minimum, maksimum):
    while True:
        try:
            return validasi_angka(input(pesan), label, minimum, maksimum)
        except ValueError as e:
            print(e)


def pilih_data(pesan):
    id_teks = input(pesan).strip()
    try:
        id_vaksin = int(id_teks)
        return id_vaksin, data_vaksin[id_vaksin]
    except ValueError:
        print("ID harus berupa angka")
    except KeyError:
        print(f"ID {id_teks} tidak ditemukan")
    return None, None


def buat_id_baru():
    return max(data_vaksin, default=0) + 1


def input_nama():
    while True:
        try:
            return validasi_nama(input("Nama Penerima Vaksin: "))
        except ValueError as e:
            print(e)


def input_vaksin():
    while True:
        vaksin = input("Jenis Vaksin: ").strip()
        try:
            if vaksin == "":
                raise ValueError("Jenis vaksin tidak boleh kosong")
            return vaksin
        except ValueError as e:
            print(e)


def input_username_baru():
    while True:
        username = input("Username: ").strip().lower()
        if username == "0":
            return None
        try:
            if len(username) < 4:
                raise ValueError("Username minimal 4 karakter")
            if " " in username:
                raise ValueError("Username tidak boleh mengandung spasi")
            if username in data_user:
                raise ValueError("Username sudah digunakan, buat yang lain")
            return username
        except ValueError as e:
            print(e)


def input_password_baru():
    while True:
        password = input("Password: ")
        try:
            if len(password) < 6:
                raise ValueError("Password minimal 6 karakter")
        except ValueError as e:
            print(e)
            continue
        if input("Konfirmasi Password: ") == password:
            return password
        print("Password tidak sama, coba lagi")


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def jeda(pesan="Tekan Enter untuk melanjutkan..."):
    try:
        input(pesan)
    except EOFError:
        pass


def tampilkan_judul(judul):
    print(f"     {judul}")
    print(bagus_tipis)


def tampilkan_tabel(data):
    print(bagus)
    print(f"{'ID':<5}{'Nama':<30}{'Umur':<8}{'Jenis Vaksin':<15}{'Dosis':<6}")
    print(bagus)
    for id_vaksin, d in data.items():
        print(f"{id_vaksin:<5}{d['nama']:<30}{d['umur']:<8}{d['vaksin']:<15}{d['dosis']:<6}")
    print(bagus)


def tampilkan_menu_awal():
    print(bagus)
    print("            Sistem Data Vaksin")
    print(bagus)
    print("1. Login")
    print("2. Register")
    print("0. Keluar")
    print(bagus)


def tampilkan_menu_utama():
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


def keluar_program():
    global program_berjalan
    program_berjalan = False
    print("Terima Kasih Telah Menggunakan Sistem Data Vaksin")


def proses_login():
    global user_aktif
    tampilkan_judul("Login")
    username = input("Username: ").strip().lower()
    password = input("Password: ")
    try:
        role = cek_login(username, password)
    except ValueError as e:
        print(e)
    else:
        user_aktif = {"username": username, "role": role}
        print(f"Login berhasil, {username}!")
    finally:
        jeda()


def proses_register():
    tampilkan_judul("Register Akun Baru")
    print("Ketik '0' pada Username untuk kembali ke menu utama")
    username = input_username_baru()
    if username is None:
        print("Registrasi dibatalkan")
    else:
        password = input_password_baru()
        data_user[username] = {"password": password, "role": "user"}
        print("Registrasi berhasil! Silakan login.")
    jeda()


def proses_logout():
    global user_aktif
    user_aktif = None
    print("Logout berhasil.")


def proses_tambah():
    tampilkan_judul("TAMBAH DATA VAKSIN")
    nama = input_nama()
    umur = input_angka("Umur (1-120): ", "Umur", 1, 120)
    vaksin = input_vaksin()
    dosis = input_angka("Dosis (1-3): ", "Dosis", 1, 3)

    id_baru = buat_id_baru()
    data_vaksin[id_baru] = {
        "nama": nama,
        "umur": umur,
        "vaksin": vaksin,
        "dosis": dosis,
    }
    print("Data berhasil ditambahkan!")


def proses_lihat():
    tampilkan_judul("DAFTAR DATA VAKSIN")
    if len(data_vaksin) == 0:
        print("Belum ada data vaksin")
    else:
        tampilkan_tabel(data_vaksin)
        print(f"Total data: {len(data_vaksin)}")


def proses_cari():
    tampilkan_judul("CARI DATA VAKSIN")
    kata_kunci = input("Masukkan nama yang dicari: ").strip().lower()
    if kata_kunci == "":
        print("Kata kunci tidak boleh kosong")
        return

    daftar_id = list(data_vaksin.keys())
    try:
        hasil_id = cari_rekursif(data_vaksin, daftar_id, kata_kunci)
    except RecursionError:
        hasil_id = [i for i in daftar_id if kata_kunci in data_vaksin[i]["nama"].lower()]

    if len(hasil_id) == 0:
        print("Data tidak ditemukan.")
    else:
        hasil = {i: data_vaksin[i] for i in hasil_id}
        tampilkan_tabel(hasil)
        print(f"Ditemukan: {len(hasil)} data")


def proses_ubah():
    tampilkan_judul("UBAH DATA VAKSIN")
    if len(data_vaksin) == 0:
        print("Belum ada data.")
        return

    tampilkan_tabel(data_vaksin)
    id_ubah, data = pilih_data("Masukkan ID yang ingin diubah: ")
    if data is None:
        return

    print("(Kosongkan lalu tekan Enter jika tidak ingin mengubah)")
    nama_baru = input(f"Nama [{data['nama']}]: ").strip()
    umur_baru = input(f"Umur [{data['umur']}]: ").strip()
    vaksin_baru = input(f"Vaksin [{data['vaksin']}]: ").strip()
    dosis_baru = input(f"Dosis [{data['dosis']}]: ").strip()

    print()
    if nama_baru != "":
        try:
            data["nama"] = validasi_nama(nama_baru)
        except ValueError as e:
            print(f"{e}, nama tidak diubah.")

    if umur_baru  != "":
        try:
            data["umur"] = validasi_angka(umur_baru, "Umur", 1, 120)
        except ValueError as e:
            print(f"{e}, umur tidak diubah.")

    if vaksin_baru != "":
        data["vaksin"] = vaksin_baru

    if dosis_baru != "":
        try:
            data["dosis"] = validasi_angka(dosis_baru, "Dosis", 1, 3)
        except ValueError as e:
            print(f"{e}, dosis tidak diubah.")

    print("Proses ubah data selesai.")


def proses_hapus():
    tampilkan_judul("HAPUS DATA VAKSIN")
    if len(data_vaksin) == 0:
        print("Belum ada data.")
        return

    tampilkan_tabel(data_vaksin)
    id_hapus, data = pilih_data("Masukkan ID yang ingin dihapus: ")
    if data is None:
        return

    yakin = input(f"Yakin hapus data '{data['nama']}'? (y/t): ").strip().lower()
    if yakin == "y":
        del data_vaksin[id_hapus]
        print("Data berhasil dihapus!")
    elif yakin == "t":
        print("Penghapusan dibatalkan.")
    else:
        print("Input tidak valid, penghapusan dibatalkan.")


def menu_awal():
    clear()
    tampilkan_menu_awal()
    pilihan = input("Pilih Menu (0-2): ").strip()

    if pilihan == "1":
        clear()
        proses_login()
    elif pilihan == "2":
        clear()
        proses_register()
    elif pilihan == "0":
        keluar_program()
    else:
        print("Pilihan tidak valid")
        jeda()


def menu_pengguna():
    clear()
    tampilkan_menu_utama()
    peran = user_aktif["role"]
    pilihan = input("Pilih Menu: ").strip()

    if peran == "admin":
        aksi = menu_admin.get(pilihan, "")
    else:
        aksi = menu_user.get(pilihan, "")
    clear()

    if aksi == "tambah":
        proses_tambah()
    elif aksi == "lihat":
        proses_lihat()
    elif aksi == "cari":
        proses_cari()
    elif aksi == "ubah":
        proses_ubah()
    elif aksi == "hapus":
        proses_hapus()
    elif aksi == "logout":
        proses_logout()
    else:
        print("Pilihan tidak valid")

    jeda("Tekan Enter untuk kembali ke menu...")


def main():
    while program_berjalan:
        try:
            if user_aktif is None:
                menu_awal()
            else:
                menu_pengguna()
        except (KeyboardInterrupt, EOFError):
            print()
            keluar_program()
        except Exception as e:
            print(f"Terjadi kesalahan tidak terduga: {e}")
            jeda()


main()
