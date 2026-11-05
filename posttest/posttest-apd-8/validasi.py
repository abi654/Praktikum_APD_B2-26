from tampilan import pesan_error



def validasi_nama(teks):
    nama = teks.strip()
    if nama == "":
        raise ValueError("Nama tidak boleh kosong")
    if not nama.replace(" ", "").isalpha():
        raise ValueError("Nama hanya boleh berisi huruf")
    return nama


def validasi_vaksin(teks):
    vaksin = teks.strip()
    if vaksin == "":
        raise ValueError("Jenis vaksin tidak boleh kosong")
    return vaksin


def validasi_angka(teks, label, minimum, maksimum):
    try:
        angka = int(teks)
    except ValueError:
        raise ValueError(f"{label} harus berupa angka") from None
    if angka < minimum or angka > maksimum:
        raise ValueError(f"{label} harus antara {minimum}-{maksimum}")
    return angka



def input_nama():
    while True:
        try:
            return validasi_nama(input("Nama Penerima Vaksin: "))
        except ValueError as e:
            pesan_error(str(e))


def input_vaksin():
    while True:
        try:
            return validasi_vaksin(input("Jenis Vaksin: "))
        except ValueError as e:
            pesan_error(str(e))


def input_angka(pesan, label, minimum, maksimum):
    while True:
        try:
            return validasi_angka(input(pesan), label, minimum, maksimum)
        except ValueError as e:
            pesan_error(str(e))
