active = True
while active:
    #Mem-print opening
    print("Selamat datang! Masukkan dua nama file yang berisi daftar makanan yang kamu miliki.")

    #Melakukan input untuk nama file input & output
    file_input = input("Masukkan nama file input daftar makanan: ")
    file_output = input("Masukkan nama file output: ")
    print()

    #Mengecek validasi input, apakah ada yang error apa tidak
    try:
        my_file_input = open(file_input, "r")
        active = False
    except FileNotFoundError:
        print("Maaf, file input tidak ada\n")
        continue

    try:
        my_file_output = open(file_output, "a")
        active = False
    except FileNotFoundError:
        print("Maaf, file input tidak ada\n")
        continue

#Mencetak line gabungan kedua list (hanya objek saja)
line_1 = my_file_input.readline()
line_2 = my_file_input.readline()
line_1_noheader = line_1.replace("Daftar Makanan 1: ", "")
line_2_noheader = line_2.replace("Daftar Makanan 2: ", "")
line_gabungan = line_1 + line_2
line_gabungan_replace1 = line_gabungan.replace("\n", "")
line_gabungan_replace2 = line_gabungan_replace1.replace("Daftar Makanan 1: ", "")
line_gabungan_replace = line_gabungan_replace2.replace("Daftar Makanan 2: ", ",").lower() 

#Melakukan while loop menu utama
running = True
while running:
    #Mencetak pilihan menu utama
    print("Apa yang ingin kamu lakukan?")
    print("================================================")
    print("1. Tampilkan daftar makanan pertama")
    print("2. Tampilkan daftar makanan kedua")
    print("3. Tampilkan gabungan makanan dari dua daftar")
    print("4. Tampilkan makanan yang sama dari dua daftar")
    print("5. Keluar")
    print("================================================")
    menu = int(input("Masukkan aksi yang ingin dilakukan: "))
    print()

    #Mencetak menu pertama
    if menu == 1:
        print("Daftar makanan pertama:", file = my_file_output)
        print(line_1[18:], file = my_file_output)
        print("Daftar makanan pertama:")
        print(line_1[18:])

    #Mencetak menu kedua
    elif menu == 2:
        print("Daftar makanan kedua:", file = my_file_output)
        print(line_2[18:], file = my_file_output)
        print("Daftar makanan kedua:")
        print(f"{line_2[18:]}\n")

    #Mencetak menu ketiga
    elif menu == 3:
        makanan_gabungan = ""
        q = 0
        while q < len(line_gabungan_replace):
            list_makanan = "" 
            while q < len(line_gabungan_replace) and line_gabungan_replace[q] != ',' and line_gabungan_replace[q] != '\n':
                list_makanan += line_gabungan_replace[q]
                q += 1
            if list_makanan not in makanan_gabungan:
                if makanan_gabungan:
                    makanan_gabungan += ","
                makanan_gabungan += list_makanan
            if q < len(line_gabungan_replace):
                q += 1
        print("\nGabungan makanan favorit dari kedua daftar:", file = my_file_output)
        print(f"{makanan_gabungan}\n", file = my_file_output)
        print("Gabungan makanan favorit dari kedua daftar:")
        print(f"{makanan_gabungan}\n")

    #Mencetak menu keempat 
    elif menu == 4:
        makanan_sama = ""
        p = 0
        while p < len(line_1_noheader):
            makanan_item = ""  
            while p < len(line_1_noheader) and line_1_noheader[p] != ',':
                makanan_item += line_1_noheader[p]
                p += 1
            p += 1  
            
            if makanan_item in line_2_noheader:
                if makanan_sama:
                    makanan_sama += ","
                makanan_sama += makanan_item

        if not makanan_sama:
            print("Tidak ada makanan yang sama dari kedua daftar\n", file = my_file_output)
            print("Tidak ada makanan yang sama dari kedua daftar\n")

        else:
            print("Makanan yang sama dari dua daftar:", file = my_file_output)
            print(f"{makanan_sama}\n", file = my_file_output)
            print("Makanan yang sama dari dua daftar:")
            print(f"{makanan_sama}\n")

    #Mencetak menu kelima
    elif menu == 5:
        print("Terima kasih telah menggunakan program ini!")
        print(f"Semua keluaran telah disimpan pada file {file_output}\n")
        exit()

#Menutup file agar bisa disimpan
my_file_input.close()
my_file_output.close()



