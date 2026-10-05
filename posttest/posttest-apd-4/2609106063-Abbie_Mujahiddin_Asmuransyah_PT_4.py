username_benar = "abbie"
password_benar = "63"

bagus = "=" * 50
bagus_tipis = "-" * 50

print(bagus)
print("                Los Pollos Hermanos")
print("                   Program MBG")
print("                Kota Albuquerque")
print(bagus)
print("Silahkan Login Terlebih Dahulu")
print(bagus_tipis)

percobaan = 0
maks_percobaan = 3
login_berhasil = False

while percobaan < maks_percobaan:
    sisa = maks_percobaan - percobaan
    print(f"Percobaan ke {percobaan + 1} dari {maks_percobaan}")

    username = input("Masukkan Username: ").strip().lower()
    password = input("Masukkan Password: ").strip().lower()

    if username == "" or password == "":
        print("Username dan password tidak boleh kosong")
        if percobaan < maks_percobaan :
            print(f"Sisa percobaan: {maks_percobaan - percobaan - 1}")
        continue

    username = username.lower() == username_benar.lower()
    password = password.lower() == password_benar.lower()

    if username and password:
        login_berhasil = True
        print("Selamat datang ", username_benar.upper())
        break
    else:
        percobaan += 1
        if not username and password:
            print("GAGAL, Username anda salah")
        elif username and not password:
            print("GAGAL, Password anda salah")
        else:
            print("GAGAL, Username dan Password anda salah")
        if percobaan < maks_percobaan:
            print(f"Sisa percobaan: {maks_percobaan - percobaan}")  

if not login_berhasil:
    print(bagus)
    print("Login anda gagal 3 kali, Akses ditolak")
    print(bagus)
else:
    menu = True

    while menu:
        print(bagus)
        print("Menu Distribusi Paket")
        print(bagus)
        print("1. Paket Reguler   (1 porsi)")
        print("2. Paket Anak      (1 porsi)")
        print("3. Paket Keluarga  (3 porsi)") 
        print("4. Keluar")
        print(bagus_tipis)

        pilihan_menu = False
        while not pilihan_menu:
            pilihan = input("Pilih menu (1-4): ").upper()
            if pilihan == "":
                print("Pilihan menu tidak boleh kosong")
            elif not pilihan.isdigit() :
                print("Pilihan menu harus berupa angka")
            elif pilihan not in ("1", "2", "3", "4"):
                print("Pilihan menu tidak ada, silahkan pilih menu yang lain")
            else:
                pilihan_menu = True

            pilihan = int(pilihan)

            if pilihan == 4:
                print(bagus)
                print("Terima kasih telah Berbagi")
                print("Program Distribusi Paket Selesai")
                print(bagus)
                menu = False    
                continue
            if pilihan == 1:
                paket = "Paket Reguler"
                porsi = 1
            elif pilihan == 2:
                paket = "Paket Anak"
                porsi = 1
            else:
                paket = "Paket Keluarga"
                porsi = 3

            jumlah_paket = False
            while not jumlah_paket:     
                jumlah = input(f"Masukkan jumlah {paket} yang akan dibagikan: ")       
                if jumlah == "":
                    print("Jumlah paket tidak boleh kosong")
                elif not jumlah.isdigit():
                    print("Jumlah paket harus berupa angka")
                elif int(jumlah) <= 0:
                    print("Jumlah paket harus lebih dari 0")        
                else:
                    jumlah_paket = True
            jumlah_total = int(jumlah)

            total_porsi = 0     
            for i in range(jumlah_total):
                total_porsi += porsi

            penerima_manfaat = total_porsi 

            if total_porsi >= 20:
                bonus = "5 paket buah"       
            elif total_porsi >= 10:
                bonus = "3 botol susu"
            elif total_porsi >= 5:
                bonus = "2 paket snack"
            else:
                bonus = "Tidak ada bonus"

            print(bagus)
            print("     Hasil Distribusi Paket")
            print(bagus) 
            print(f"Jenis Paket: {paket}")
            print(f"Jumlah Paket: {jumlah_total}")
            print(f"Total Porsi: {total_porsi} porsi")           
            print(f"Penerima Manfaat: {penerima_manfaat} orang")
            print(f"Bonus: {bonus}")
            print(bagus_tipis)
            print("Makanan yang dibagikan Gratis Untuk Masyarakat")
            print(bagus)