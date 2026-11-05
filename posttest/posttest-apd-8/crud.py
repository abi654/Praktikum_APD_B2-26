from data import data_vaksin
from tampilan import (
    pesan_error,
    pesan_info,
    pesan_sukses,
    tampilkan_judul,
    tampilkan_tabel,
)
from validasi import (
    input_angka,
    input_nama,
    input_vaksin,
    validasi_angka,
    validasi_nama,
)


# ---------- Fungsi bantu ----------
def buat_id_baru():
    return max(data_vaksin, default=0) + 1


def pilih_data(pesan):
    id_teks = input(pesan).strip()
    try:
        id_vaksin = int(id_teks)
        return id_vaksin, data_vaksin[id_vaksin]
    except ValueError:
        pesan_error("ID harus berupa angka")
    except KeyError:
        pesan_error(f"ID {id_teks} tidak ditemukan")
    return None, None


def cari_rekursif(data, daftar_id, kata_kunci, indeks=0):
    if indeks >= len(daftar_id):
        return []
    id_sekarang = daftar_id[indeks]
    cocok = []
    if kata_kunci in data[id_sekarang]["nama"].lower():
        cocok = [id_sekarang]
    return cocok + cari_rekursif(data, daftar_id, kata_kunci, indeks + 1)


# ---------- Fitur CRUD ----------
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
    pesan_sukses("Data berhasil ditambahkan!")


def proses_lihat():
    tampilkan_judul("DAFTAR DATA VAKSIN")
    if len(data_vaksin) == 0:
        pesan_info("Belum ada data vaksin")
    else:
        tampilkan_tabel(data_vaksin)
        print(f"Total data: {len(data_vaksin)}")


def proses_cari():
    tampilkan_judul("CARI DATA VAKSIN")
    kata_kunci = input("Masukkan nama yang dicari: ").strip().lower()
    if kata_kunci == "":
        pesan_error("Kata kunci tidak boleh kosong")
        return

    daftar_id = list(data_vaksin.keys())
    try:
        hasil_id = cari_rekursif(data_vaksin, daftar_id, kata_kunci)
    except RecursionError:
        hasil_id = [i for i in daftar_id if kata_kunci in data_vaksin[i]["nama"].lower()]

    if len(hasil_id) == 0:
        pesan_info("Data tidak ditemukan.")
    else:
        hasil = {i: data_vaksin[i] for i in hasil_id}
        tampilkan_tabel(hasil)
        print(f"Ditemukan: {len(hasil)} data")


def proses_ubah():
    tampilkan_judul("UBAH DATA VAKSIN")
    if len(data_vaksin) == 0:
        pesan_info("Belum ada data.")
        return

    tampilkan_tabel(data_vaksin)
    id_ubah, data = pilih_data("Masukkan ID yang ingin diubah: ")
    if data is None:
        return

    pesan_info("(Kosongkan lalu tekan Enter jika tidak ingin mengubah)")
    nama_baru = input(f"Nama [{data['nama']}]: ").strip()
    umur_baru = input(f"Umur [{data['umur']}]: ").strip()
    vaksin_baru = input(f"Vaksin [{data['vaksin']}]: ").strip()
    dosis_baru = input(f"Dosis [{data['dosis']}]: ").strip()

    print()
    if nama_baru != "":
        try:
            data["nama"] = validasi_nama(nama_baru)
        except ValueError as e:
            pesan_error(f"{e}, nama tidak diubah.")

    if umur_baru != "":
        try:
            data["umur"] = validasi_angka(umur_baru, "Umur", 1, 120)
        except ValueError as e:
            pesan_error(f"{e}, umur tidak diubah.")

    if vaksin_baru != "":
        data["vaksin"] = vaksin_baru

    if dosis_baru != "":
        try:
            data["dosis"] = validasi_angka(dosis_baru, "Dosis", 1, 3)
        except ValueError as e:
            pesan_error(f"{e}, dosis tidak diubah.")

    pesan_sukses("Proses ubah data selesai.")


def proses_hapus():
    tampilkan_judul("HAPUS DATA VAKSIN")
    if len(data_vaksin) == 0:
        pesan_info("Belum ada data.")
        return

    tampilkan_tabel(data_vaksin)
    id_hapus, data = pilih_data("Masukkan ID yang ingin dihapus: ")
    if data is None:
        return

    yakin = input(f"Yakin hapus data '{data['nama']}'? (y/t): ").strip().lower()
    if yakin == "y":
        del data_vaksin[id_hapus]
        pesan_sukses("Data berhasil dihapus!")
    elif yakin == "t":
        pesan_info("Penghapusan dibatalkan.")
    else:
        pesan_error("Input tidak valid, penghapusan dibatalkan.")
