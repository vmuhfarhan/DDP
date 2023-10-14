def print_menu(): #Fungsi untuk mencetak daftar menu dari program
    print("""Selamat datang di Database Nilai Dek Depe
1. Tambah data ke database
2. Baca data dari database
3. Update data di database
4. Hapus data dari database
5. Keluar""")
    
list_nama = []   #Untuk menyimpan nama                              #Karena index nama dan data sama, kita bisa indexing masing" 
list_data = []   #Untuk menyimpan kumpulan nilai dari nama              list melalui index yang sama

running = True #While loop untuk menjalankan menu utama
while running:
    print()
    print_menu()
    menu = int(input("Masukkan kegiatan yang ingin dilakukan: ")) # Input menu yang diberikan user + validasi input
    if menu == 1: #1. Tambah data ke database
        nama = input("Masukkan nama: ")
        nama_lower = nama.lower()
        if nama_lower not in list_nama:  #Mengecek apakah nama ada di dalam list_nama. Jika tidak ada, buat list baru
            list_nama.append(nama_lower)
            menu1 = True
            labcount = 0
            list_nilai = []
            while menu1:
                input_menu_1 = input(f"Masukkan nilai Lab {labcount + 1} (ketik STOP untuk selesai): ")
                if input_menu_1 == "STOP":    #Jika menu = STOP. keluar dari menu 1
                    print(f"Berhasil menambahkan {labcount} nilai untuk {nama} ke database")
                    menu1 =  False
                    if len(list_nilai) != 0:
                        list_data.append(list_nilai)
                elif 0 <= int(input_menu_1) <= 100:   #Jika nilai valid
                    list_nilai.append(input_menu_1)
                    labcount += 1
                else:           #Jika nilainya tidak valid
                    print(f"Nilai yang anda masukkan tidak valid")
        else:   #Mengecek apakah nama ada di dalam list_nama. Jika ada
            print("Nama sudah terdapat di dalam database")
            
    elif menu == 2: #2. Baca data dari database
        nama = input("Masukkan nama: ")
        nama_lower = nama.lower()
        if nama_lower in list_nama: #Mengecek apakah nama ada di dalam list_nama. Jika ada, memproses menu 2
            index_nama = list_nama.index(nama_lower)
            input_menu_2 = input("Masukkan nilai Lab ke berapa yang ingin dilihat: ")
            if list_data[index_nama][int(input_menu_2)-1] == None:
                print(f"Tidak terdapat nilai untuk Lab {input_menu_2}")
            else:
                if 0 < int(input_menu_2) <= len(list_data[index_nama]):
                    print(f"Nilai Lab {input_menu_2} {nama} adalah {float(list_data[index_nama][int(input_menu_2) - 1])}")
                else:
                    print(f"Tidak terdapat nilai untuk Lab {input_menu_2}")        
        else:      #Mengecek apakah nama ada di dalam list_nama. Jika tidak ada
            print("Nama tidak ada dalam database")

    elif menu == 3: #3. Update data di database
        nama = input("Masukkan nama: ")
        nama_lower = nama.lower()
        if nama_lower in list_nama:        #Mengecek apakah nama ada di dalam list_nama. Jika ada, memproses menu 3
            index_nama = list_nama.index(nama_lower)
            input_menu_3a = input("Masukkan nilai Lab ke berapa yang ingin diupdate: ")
            if 0 < int(input_menu_3a) <= len(list_data[index_nama]):
                input_menu_3b = input(f"Masukkan nilai baru untuk Lab {input_menu_3a}: ")
                if 0 <= int(input_menu_3b) <= 100:    
                    nilai_lama = list_data[index_nama][int(input_menu_3a) - 1]
                    list_data[index_nama][int(input_menu_3a) - 1] = input_menu_3b
                    print(f'Berhasil mengupdate nilai Lab {input_menu_3a} {nama} dari {float(nilai_lama)} ke {float(input_menu_3b)}')
                else:
                    print(f"Nilai yang anda masukkan tidak valid")      #Jika nilai tidak valid
            else:
                print(f"Tidak terdapat nilai untuk Lab {input_menu_3a}")    #Jika tidak ada nilai 
        else:
            print("Nama tidak ada dalam database")     #Mengecek apakah nama ada di dalam list_nama. Jika tidak ada

    elif menu == 4: #4. Hapus data dari database   
        nama = input("Masukkan nama: ")
        nama_lower = nama.lower()
        if nama_lower in list_nama:        #Mengecek apakah nama ada di dalam list_nama. Jika ada, memproses menu 4
            index_nama = list_nama.index(nama_lower)
            input_menu_4 = input("Masukkan nilai Lab ke berapa yang ingin dihapus: ")
            if list_data[index_nama][int(input_menu_4) - 1] == None:
                print(f"Tidak terdapat nilai untuk Lab {input_menu_4}")
            elif 0 < int(input_menu_4) <= len(list_data[index_nama]):
                list_data[index_nama][int(input_menu_4) - 1] = None
                print(f"Berhasil menghapus nilai Lab {input_menu_4} {nama} dari database")
            else:
                print(f"Tidak terdapat nilai untuk Lab {input_menu_4}")
        else:
            print("Nama tidak ada dalam database")

    elif menu == 5: #5. Keluar
        print("Terimakasih telah menggunakan Database Nilai Dek Depe")
        running = False

    else:
        print("Menu yang anda masukkan tidak valid")

