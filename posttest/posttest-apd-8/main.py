import auth
import crud
from data import sesi
from tampilan import (
    clear,
    jeda,
    pesan_error,
    pesan_info,
    tampilkan_menu_awal,
    tampilkan_menu_utama,
)

# Nomor menu -> nama aksi, dibedakan berdasarkan role
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

# Nama aksi -> fungsi yang dijalankan
aksi_fungsi = {
    "tambah": crud.proses_tambah,
    "lihat": crud.proses_lihat,
    "cari": crud.proses_cari,
    "ubah": crud.proses_ubah,
    "hapus": crud.proses_hapus,
    "logout": auth.proses_logout,
}


def keluar_program():
    sesi["berjalan"] = False
    pesan_info("Terima Kasih Telah Menggunakan Sistem Data Vaksin")


def menu_awal():
    clear()
    tampilkan_menu_awal()
    pilihan = input("Pilih Menu (0-2): ").strip()

    if pilihan == "1":
        clear()
        auth.proses_login()
    elif pilihan == "2":
        clear()
        auth.proses_register()
    elif pilihan == "0":
        keluar_program()
    else:
        pesan_error("Pilihan tidak valid")
        jeda()


def menu_pengguna():
    user = sesi["user_aktif"]
    daftar_menu = menu_admin if user["role"] == "admin" else menu_user

    clear()
    tampilkan_menu_utama(user["username"], user["role"], daftar_menu)
    pilihan = input("Pilih Menu: ").strip()
    aksi = daftar_menu.get(pilihan, "")
    clear()

    if aksi in aksi_fungsi:
        aksi_fungsi[aksi]()
    else:
        pesan_error("Pilihan tidak valid")

    jeda("Tekan Enter untuk kembali ke menu...")


def main():
    while sesi["berjalan"]:
        try:
            if sesi["user_aktif"] is None:
                menu_awal()
            else:
                menu_pengguna()
        except (KeyboardInterrupt, EOFError):
            print()
            keluar_program()
        except Exception as e:
            pesan_error(f"Terjadi kesalahan tidak terduga: {e}")
            jeda()


if __name__ == "__main__":
    main()