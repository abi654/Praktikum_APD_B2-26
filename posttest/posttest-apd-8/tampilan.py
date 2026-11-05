import os

try:
    import importlib

    _colorama = importlib.import_module("colorama")
    Fore, Style, init = _colorama.Fore, _colorama.Style, _colorama.init
except ImportError:
    class _ColorFallback:
        GREEN = RED = YELLOW = CYAN = RESET_ALL = ""

    Fore = Style = _ColorFallback()

    def init(*args, **kwargs):
        pass
from prettytable import PrettyTable


init(autoreset=True)

LEBAR_TABEL = 50


LABEL_MENU = {
    "tambah": "Tambah Data",
    "lihat": "Lihat Data",
    "cari": "Cari Data",
    "ubah": "Ubah Data",
    "hapus": "Hapus Data",
    "logout": "Logout",
}


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def jeda(pesan="Tekan Enter untuk melanjutkan..."):
    try:
        input(pesan)
    except EOFError:
        pass


# ---------- Pesan berwarna ----------
def pesan_sukses(teks):
    print(Fore.GREEN + teks)


def pesan_error(teks):
    print(Fore.RED + teks)


def pesan_info(teks):
    print(Fore.YELLOW + teks)


# ---------- Tabel PrettyTable ----------
def tampilkan_judul(judul):
    tabel = PrettyTable()
    tabel.header = False
    tabel.min_table_width = LEBAR_TABEL
    tabel.add_row([judul])
    tabel.align = "c"
    print(Fore.CYAN + tabel.get_string())


def tampilkan_tabel(data):
    tabel = PrettyTable()
    tabel.field_names = ["ID", "Nama", "Umur", "Jenis Vaksin", "Dosis"]
    for id_vaksin, d in data.items():
        tabel.add_row([id_vaksin, d["nama"], d["umur"], d["vaksin"], d["dosis"]])
    tabel.align = "c"
    tabel.align["Nama"] = "l"
    tabel.align["Jenis Vaksin"] = "l"
    print(tabel)


def tampilkan_menu_awal():
    tabel = PrettyTable()
    tabel.title = "SISTEM DATA VAKSIN"
    tabel.field_names = ["No", "Menu"]
    tabel.min_table_width = LEBAR_TABEL
    tabel.add_row(["1", "Login"])
    tabel.add_row(["2", "Register"])
    tabel.add_row(["0", "Keluar"])
    tabel.align = "c"
    tabel.align["Menu"] = "l"
    print(Fore.CYAN + tabel.get_string())


def tampilkan_menu_utama(username, peran, daftar_menu):
    """daftar_menu: dict {nomor: aksi}, contoh {"1": "tambah", ...}"""
    tabel = PrettyTable()
    tabel.title = "SISTEM DATA VAKSIN"
    tabel.field_names = ["No", "Menu"]
    tabel.min_table_width = LEBAR_TABEL
    for nomor, aksi in daftar_menu.items():
        tabel.add_row([nomor, LABEL_MENU[aksi]])
    tabel.align = "c"
    tabel.align["Menu"] = "l"
    print(Fore.CYAN + tabel.get_string())
    print(f"Login sebagai: {Fore.GREEN}{username}{Style.RESET_ALL} ({peran})")
