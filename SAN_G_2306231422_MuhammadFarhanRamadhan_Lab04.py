#Mengimport library sys
import sys

#Membuat fungsi untuk menjalankan program awal 
def basic_function():
    argumen = sys.argv
    global file_input, file_content, keyword, column, line_fix, check, string_gabungan

    #Memastikan bahwa argumen yang diberikan adalah 4 (tidak lebih dan tidak kurang)
    if len(argumen) == 4:
        file_input = sys.argv[1]
        keyword = sys.argv[2].lower()
        column = sys.argv[3]
    else:
        print("Usage: python script_name.py <file_path> <search_keyword> <column_num>")
        sys.exit()

    #Memastikan bahwa file input ada
    try:
        file_open = open(file_input, "r")
        file_content = file_open.readlines()
    except FileNotFoundError:
        print("Maaf, file input tidak ada")
        sys.exit()

    line_fix = []
    check = False

    #Memisahkan item di dalam list berdasarkan tab
    for line in file_content:
        file_replace = line.replace("\n", "")
        file_replace2 = file_replace.split("\t")
        line_fix.append(file_replace2)

    #Memastikan apakah ada kata kunci di setiap line pada input
    for x in line_fix:
        separator = " "
        string_gabungan = separator.join(x).lower()
        if keyword in string_gabungan.lower():
            check = True

#Membuat fungsi untuk mencetak header tabel
def print_headers():
    print("| {: <2} | {: <25} | {: <8} | {: <10} | {: <3} |".format("No", "Smartphone", "Price", "Screensize", "RAM"))
    print("================================================================")

#Membuat fungsi untuk mencetak tabel sesuai file input
def print_table():
    print_headers()
    number = 1
    for x in line_fix:
        smartphone = x[0]
        price = x[1]
        screensize = x[2]
        ram = x[3]
        print("| {: <2} | {: <25} | {: <8} | {: <10} | {: <3} |".format(number, smartphone, price, screensize, ram))
        number += 1

#Membuat fungsi untuk mencari apakah keyword ada di line di dalam file input. Jika ada, mencetak tabel
def search_phone(keyword):
    if check == True:
        print_headers()
        number = 1
        for x in line_fix:
            smartphone = x[0]
            price = x[1]
            screensize = x[2]
            ram = x[3]
            separator = " "
            string_x = separator.join(x).lower()
            if keyword in string_x:
                print("| {: <2} | {: <25} | {: <8} | {: <10} | {: <3} |".format(number, smartphone, price, screensize, ram))
                number += 1
    else:
        print("Maaf, kata kunci tidak ditemukan")

#Membuat fungsi untuk mencetak statistik dari column sesuai input yang diberikan
def desc_stat(column):
    list_price = []
    list_screensize = [] 
    list_ram = []
    number = 1
    for x in line_fix:
        price = x[1]
        screensize = x[2]
        ram = x[3]
        list_price.append(price)
        list_screensize.append(screensize)
        list_ram.append(ram)
        separator = " "
        string_x = separator.join(x).lower()
        if keyword in string_x.lower():
            number += 1
    
    #Mengubah list yang berbentuk string menjadi float agar bisa dilakukan operator min, max, dan sum
    float_list_price = [float(x) for x in list_price]
    float_list_screensize = [float(x) for x in list_screensize]
    float_list_ram = [float(x) for x in list_ram]

    #Membuat conditional sesuai input (1.price | 2.screensize | 3.RAM)
    if column == "1":
        print(f"Ukuran data dari hasil pencarian: {number-1} x 4")
        print(f"Min data: {min(float_list_price):.2f}")
        print(f"Max data: {max(float_list_price):.2f}")
        print(f"Rata - rata: {sum(float_list_price)/len(file_content):.2f}")

    elif column == "2":
        print(f"Ukuran data dari hasil pencarian: {number-1} x 4")
        print(f"Min data: {min(float_list_screensize):.2f}")
        print(f"Max data: {max(float_list_screensize):.2f}")
        print(f"Rata - rata: {sum(float_list_screensize)/len(file_content):.2f}")

    elif column == "3":
        print(f"Ukuran data dari hasil pencarian: {number-1} x 4")
        print(f"Min data: {min(float_list_ram):.2f}")
        print(f"Max data: {max(float_list_ram):.2f}")
        print(f"Rata - rata: {sum(float_list_ram)/len(file_content):.2f}")

    else:
        print("Maaf, Argumen anda tidak valid")
        sys.exit()

#Menjalankan program utama
running = True
while running:
    basic_function()
    print_table()
    search_phone(keyword)
    desc_stat(column)
    running = False

sys.exit()

