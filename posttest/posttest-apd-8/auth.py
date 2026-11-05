from getpass import getpass as pwinput

from data import data_user, sesi
from tampilan import (
    jeda,
    pesan_error,
    pesan_info,
    pesan_sukses,
    tampilkan_judul,
)


def cek_login(username, password):
    try:
        akun = data_user[username]
    except KeyError:
        raise ValueError("Username atau password salah") from None
    if akun["password"] != password:
        raise ValueError("Username atau password salah")
    return akun["role"]


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
            pesan_error(str(e))


def input_password_baru():
    while True:
        password = pwinput("Password: ")
        try:
            if len(password) < 6:
                raise ValueError("Password minimal 6 karakter")
        except ValueError as e:
            pesan_error(str(e))
            continue
        if pwinput("Konfirmasi Password: ") == password:
            return password
        pesan_error("Password tidak sama, coba lagi")


def proses_login():
    tampilkan_judul("LOGIN")
    username = input("Username: ").strip().lower()
    password = pwinput("Password: ")
    try:
        role = cek_login(username, password)
    except ValueError as e:
        pesan_error(str(e))
    else:
        sesi["user_aktif"] = {"username": username, "role": role}
        pesan_sukses(f"Login berhasil, {username}!")
    finally:
        jeda()


def proses_register():
    tampilkan_judul("REGISTER AKUN BARU")
    pesan_info("Ketik '0' pada Username untuk kembali ke menu utama")
    username = input_username_baru()
    if username is None:
        pesan_info("Registrasi dibatalkan")
    else:
        password = input_password_baru()
        data_user[username] = {"password": password, "role": "user"}
        pesan_sukses("Registrasi berhasil! Silakan login.")
    jeda()


def proses_logout():
    sesi["user_aktif"] = None
    pesan_sukses("Logout berhasil.")

