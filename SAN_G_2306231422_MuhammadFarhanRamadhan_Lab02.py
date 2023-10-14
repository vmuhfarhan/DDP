#Variabel konstan berisi harga dan diskon
XMAN = 7000
DORAEMOH = 5500
NARTOH = 4000
DISKON = 0.8

#Membuat while loop untuk menginput menu utama
running = True
while running:
    print("Selamat Datang di Toko Buku Place Anak Chill")
    print("============================================")
    print("1. Pinjam buku")
    print("2. Keluar")
    print("============================================")
    input_menu = int(input("Apa yang ingin anda lakukan: "))
    #Membuat kondisional sesuai input menu yang dipilih (menu 1)
    if input_menu == 1:
        input_nama = input("Masukkan nama anda: ")
        input_saldo = int(input("Masukkan saldo anda (Rp): "))
        input_member = input("Apakah anda member? [Y/N]: ")
        if input_member == "Y":
            percobaan = False
            #Membuat for loop yang menghitung berapa kali input akan dimasukkan, jika 3 kali maka balik ke menu awal
            for i in range(3):
                input_id = input("Masukkan ID anda: ")
                total_character = 0
                
                #Membuat for loop untuk menghitung jumlah dari karakter input apakah = 23 dan apakah digitnya 5
                for character in input_id:
                    total_character = total_character + int(character)
                if len(input_id) == 5 and total_character == 23:
                    percobaan = True
                    break
                else:
                    print("ID anda salah!")
                    continue
            
            if percobaan == False:
                print("Program akan kembali ke menu utama\n")
                continue
            
            #Membuat while loop untuk meminta input buku yang dipilih
            print("Login member berhasil!\n")
            while running:
                print("============================================")
                print("Katalog Buku Place Anak Chill")
                print("============================================")
                print("X-Man (Rp 7.000/hari)")
                print("Doraemoh (Rp 5.500/hari)")
                print("Nartoh (Rp 4.000/hari)")
                print("============================================")
                print("Exit")
                print("============================================")
                input_buku = input("Buku yang dipilih: ").lower()
                if input_buku == "exit":
                    break
                input_hari = int(input("Ingin melakukan peminjaman untuk berapa hari: "))
                if input_buku == "x-man":
                    harga = 7000 * input_hari
                elif input_buku == "doraemoh":
                    harga = 5500 * input_hari
                elif input_buku == "nartoh":
                    harga = 4000 * input_hari
                else:
                    print("Komik tidak ditemukan. Masukkan kembali judul komik sesuai katalog!\n")
                
                #Menghitung harga sewa buku yang dipilih
                harga_total = harga * DISKON
                if input_saldo >= harga_total:
                    sisa_saldo = float(input_saldo - harga_total)
                    input_saldo -= harga_total
                    print(f"Berhasil meminjam buku {input_buku} selama {input_hari} hari\nSaldo anda saat ini Rp{sisa_saldo}\n\n")
                    continue
                elif input_saldo < harga_total:
                    sisa_saldo = float(input_saldo - harga_total)
                    input_saldo -= harga_total
                    print(f"Tidak berhasil meminjam! Saldo anda kurang {harga_total - input_saldo}\n\n")
                    continue
                

        if input_member == "N":
            #Membuat while loop untuk meminta input buku yang dipilih
            print("Login non-member berhasil!\n")
            while running:
                print("============================================")
                print("Katalog Buku Place Anak Chill")
                print("============================================")
                print("X-Man (Rp 7.000/hari)")
                print("Doraemoh (Rp 5.500/hari)")
                print("Nartoh (Rp 4.000/hari)")
                print("============================================")
                print("Exit")
                print("============================================")
                input_buku = input("Buku yang dipilih: ").lower()
                if input_buku == "exit":
                    break
                input_hari = int(input("Ingin melakukan peminjaman untuk berapa hari: "))
                if input_buku == "x-man":
                    harga = 7000 * input_hari
                elif input_buku == "doraemoh":
                    harga = 5500 * input_hari
                elif input_buku == "nartoh":
                    harga = 4000 * input_hari
                else:
                    print("Komik tidak ditemukan. Masukkan kembali judul komik sesuai katalog!\n")
                    continue

                #Menghitung harga sewa buku yang dipilih
                harga_total = harga
                if input_saldo >= harga_total:
                    sisa_saldo = float(input_saldo - harga_total)
                    input_saldo -= harga_total
                    print(f"Berhasil meminjam buku {input_buku} selama {input_hari} hari\nSaldo anda saat ini Rp{sisa_saldo}\n\n")
                    continue
                elif input_saldo < harga_total:
                    sisa_saldo = float(input_saldo - harga_total)
                    input_saldo -= harga_total
                    print(f"\n\nTidak berhasil meminjam! Saldo anda kurang {harga_total - input_saldo}\n\n")
                    continue


    #Membuat kondisional sesuai input menu yang dipilih (menu 1) 
    if input_menu == 2:
        print("Terima kasih telah mengunjungi Toko Buku Place Anak Chill!")
        running = False

    
