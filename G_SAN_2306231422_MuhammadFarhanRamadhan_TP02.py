#KOLABORATOR : Muhammad Azzam

import os   #Mengimport library os, sys, dan time yang akan digunakan oleh program
import sys
import time
# python lab4.py(0) [section](1) [kata kunci 1](2) [AND/OR/ANDNOT](3) [kata kunci 2](4) :
# fitur tambahan = sort, contoh: python lab4.py sort "jateng" // python lab4.py sort "pn-blora" AND/OR/ANDNOT "korupsi"

def print_header(file_path): #fungsi untuk mencetak output berisi informasi
    header = [] # 2 = namafile,  6 = provinsi, 3 = klasifikasi, 8 = subklasifikasi, 5 = pn
    with open(file_path) as f:
        linesplit = file_content.splitlines()[0]
        list_linesplit = linesplit.split()
        list_header = list_linesplit[1:]
        for x in list_header:
            replace = x.replace('"', '')
            result = replace.split('=')[1]
            header.append(result)
    
    print("{: <36} {: >15} {: >15} {: >30} {: >20}".format(header[2]+'.xml', header[6][:15], header[3][:15], header[8][:30], header[5][:20]))
    
start_time = time.time() #Mengetahui waktu dimulai program

if 3 <= len(sys.argv) <= 5: #Validasi input sesuai dengan yang diminta
    section = sys.argv[1]
    if section not in ["sort", "all", "kepala_putusan", "identitas", "riwayat_penahanan", "riwayat_perkara" , "riwayat_tuntutan", "riwayat_dakwaan", "fakta", "fakta_umum", "pertimbangan_hukum", "amar_putusan", "penutup"]:
        print("\nArgumen program tidak benar.")
        sys.exit()
    keyword_1 = sys.argv[2].lower()

    if len(sys.argv) == 4:
        print("\nArgumen program tidak benar.")
        sys.exit()

    elif len(sys.argv) == 5:
        operator = sys.argv[3]
        if operator not in ["AND", "OR", "ANDNOT"]:
            print("\nMode harus berupa AND, OR atau ANDNOT.")
            sys.exit()
        keyword_2 = sys.argv[4].lower()

else:
    print("\nArgumen program tidak benar.")
    sys.exit()

dir_dataset = r'C:\\Users\\FARHAN\\PYTHON\\TP 2\\dataset'   #directory dari folder dataset (tergantung laptop)
print()

quantity = 0 #menghitung jumlah dokumen
for file in os.listdir(dir_dataset): 
    if file.endswith(".xml"): #validasi file apakah xml atau bukan
        file_path = os.path.join(dir_dataset, file)
        file_open = open(file_path, "r")                    # loop untuk membuka dan membaca file xml di dalam directory
        file_content = file_open.read()
        file_open.close()

        if section == "sort":                        # Kasus 1 : jika section = sort
            header = file_content.splitlines()[0]
            header = header.replace('"', " ")
            if len(sys.argv) == 3:
                if keyword_1 in header:
                    print_header(file_path)
                    quantity += 1

            if len(sys.argv) == 5:
                if operator == "AND":
                    if keyword_1 in header and keyword_2 in header:
                        print_header(file_path)
                        quantity += 1
                if operator == "OR":
                    if keyword_1 in header or keyword_2 in header:
                        print_header(file_path)
                        quantity += 1
                if operator == "ANDNOT":
                    if keyword_1 in header and keyword_2 not in header:
                        print_header(file_path)
                        quantity += 1

        elif section == "all":              # Kasus 2 : jika section = all
            index_awal = file_content.find("<kepala_putusan>")
            index_akhir = file_content.find("</penutup>")

            cropped_file_content = file_content[index_awal+17 : index_akhir]
            section_content = cropped_file_content.replace("\n", " ")

            if len(sys.argv) == 3:
                if keyword_1 in section_content:
                    print_header(file_path)
                    quantity += 1

            elif len(sys.argv) == 5:
                if operator == "AND":
                    if keyword_1 in section_content and keyword_2 in section_content:
                        print_header(file_path)
                        quantity += 1

                elif operator == "OR":
                    if keyword_1 in section_content or keyword_2 in section_content:
                        print_header(file_path)
                        quantity += 1

                elif operator == "ANDNOT":
                    if keyword_1 in section_content and keyword_2 not in section_content:
                        print_header(file_path)
                        quantity += 1

        else:                  # Kasus 3 : jika section = input user
            index_awal = file_content.find("<"+section+">")
            index_akhir = file_content.find("</"+section+">")

            cropped_file_content = file_content[index_awal+len(section)+3 : index_akhir]
            section_content = cropped_file_content.replace("\n", " ")
            
            if len(sys.argv) == 3:
                if keyword_1 in section_content:
                    print_header(file_path)
                    quantity += 1

            elif len(sys.argv) == 5:
                if operator == "AND":
                    if keyword_1 in section_content and keyword_2 in section_content:
                        print_header(file_path)
                        quantity += 1

                elif operator == "OR":
                    if keyword_1 in section_content or keyword_2 in section_content:
                        print_header(file_path)
                        quantity += 1

                elif operator == "ANDNOT":
                    if keyword_1 in section_content and keyword_2 not in section_content:
                        print_header(file_path)
                        quantity += 1

end_time = time.time()      #Mengetahui waktu selesai program
run_time = end_time - start_time        #Mencari waktu yang dibutuhkan oleh program untuk running
print()

if quantity > 0:        #print summary jika dokumen ditemukan
    label1 = "Banyaknya dokumen yang ditemukan"
    label2 = "Total waktu pencarian"

    max_label_length = max(len(label1), len(label2))

    print(f"{label1} {' ' * (max_label_length - len(label1))}= {quantity}")
    print(f"{label2} {' ' * (max_label_length - len(label2))}= {run_time:.3f} detik")

else:                   #print summary jika dokumen tidak ditemukan
    print("Maaf dokumen tidak ditemukan")