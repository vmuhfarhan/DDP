#KOLABORATOR : Muhammad Nadzim Tahara

#Mengimport library turtle
import turtle as t
from tkinter import messagebox

#Memunculkan layar
layar = t.Screen()
#Mengatur kecepatan turtle
t.speed('fastest')
#Membuat judul program
t.title("Mini Super Mario Towers")

#Melakukan while loop masing-masing input untuk mengecek ke-valid-an input dari user sesuai syarat
running = True
while running:
    cek1 = True
    cek2 = True
    cek3 = True
    cek4 = True
    cek5 = True
    cek6 = True
    cek7 = True

    while cek1:
        jumlah_tower = int(layar.numinput("Tower to Build", "Enter the number of towers you want to build (integer)"))
        if jumlah_tower < 1:
            messagebox.showwarning("Too small", "The allowed minimum value is 1. Please try again.")
            continue
        elif jumlah_tower == 1:
            bedatinggi_tower = 0
            jarak_tower = 0
            cek1 = False
            cek2 = False
            cek3 = False
        else:
            cek1 = False

    while cek2:
        jarak_tower = int(layar.numinput("Distance between Towers", "Enter the distance between towers (integer)"))
        if jarak_tower < 2 or jarak_tower > 5:
            messagebox.showwarning("Too large", "Choose from 2 to 5. Please try again.")
            continue
        else:
            cek2 = False

    while cek3:
        bedatinggi_tower = int(layar.numinput("Tower Layer Difference", "Enter the number of layer differences between each tower (integer)"))
        if bedatinggi_tower < 2 or bedatinggi_tower > 5:
            messagebox.showwarning("Too large", "Choose from 2 to 5. Please try again.")
            continue
        else:
            cek3 = False

    while cek4:
        panjang_bata = int(layar.numinput("Brick Width", "Enter the width of a brick (integer)"))
        if panjang_bata > 35:
            messagebox.showwarning("Too large", "The allowed maximum value is 35. Please try again.")
            continue
        elif panjang_bata < 1:
            messagebox.showwarning("Too small", "The allowed minimum value is 1. Please try again.")
            continue
        else:
            cek4 = False

    while cek5:
        tinggi_bata = int(layar.numinput("Brick Height", "Enter the height of a brick (integer)"))
        if tinggi_bata > 25:
            messagebox.showwarning("Too large", "The allowed maximum value is 25. Please try again.")
            continue
        elif tinggi_bata < 1:
            messagebox.showwarning("Too small", "The allowed minimum value is 1. Please try again.")
            continue
        else:
            cek5 = False

    while cek6:
        tinggi_tower = int(layar.numinput("The Number of First Tower Layers", "Enter the number of layers for the first tower (integer)"))
        if tinggi_tower > 10:
            messagebox.showwarning("Too large", "The allowed maximum value is 10. Please try again.")
            continue
        elif tinggi_tower < 1:
            messagebox.showwarning("Too small", "The allowed minimum value is 1. Please try again.")
            continue
        else:
            cek6 = False

    while cek7:
        lebar_tower = int(layar.numinput("Layer Width", "Enter the width of the layer (integer)"))
        if lebar_tower > 10:
            messagebox.showwarning("Too large", "The allowed maximum value is 10. Please try again.")
            continue
        elif lebar_tower < 1:
            messagebox.showwarning("Too small", "The allowed minimum value is 1. Please try again.")
            continue
        else:
            cek7 = False

    break

#Melakukan pemindahan posisi awal turtle agar presisi di layar
t.penup()
t.setpos((-((panjang_bata * lebar_tower) * jumlah_tower - 100)), -250) #kira kira aja koordinat x dan y nya

#Menjalankan program utama untuk membuat tower
nambah_tinggi = 0 #pertambahan tinggi tower (akumulasi bedatinggi terhitung dari tower ke-2)
total_lebih_bata = 0 #total lebih bata per tower (bata tower sekarang - bata tower awal)

for tower in range(jumlah_tower):
    koor_y = t.ycor() #Mengetahui koordinat y (konsisten)
    
    for bata in range (nambah_tinggi + tinggi_tower):
        #Melakukan for loop untuk membuat badan tower
        for badan_tower in range (lebar_tower):
            warna_bata = "#CA7F65"
            t.pendown()
            t.fillcolor(warna_bata)
            t.begin_fill()
            t.forward(panjang_bata)
            t.left(90)
            t.forward(tinggi_bata)
            t.left(90)
            t.forward(panjang_bata)
            t.left(90)
            t.forward(tinggi_bata)
            t.end_fill()
            t.penup()
            t.left(90)
            t.forward(panjang_bata)
            koor_x = t.xcor() #Mengetahui koordinat x (dinamis, sesuai tower)

        #Melakukan pemindahan turtle ke lapisan berikutnya
        t.penup()
        t.right(180)
        t.forward(panjang_bata * lebar_tower)
        t.right(90)
        t.forward(tinggi_bata)
        t.right(90)

    #Melakukan for loop untuk membuat atap tower
    t.backward(panjang_bata / 2)
    for atap_tower in range (lebar_tower + 1):
        warna_bata = "#693424"
        t.pendown()
        t.fillcolor(warna_bata)
        t.begin_fill()
        t.forward(panjang_bata)
        t.left(90)
        t.forward(tinggi_bata)
        t.left(90)
        t.forward(panjang_bata)
        t.left(90)
        t.forward(tinggi_bata)
        t.end_fill()
        t.penup()
        t.left(90)
        t.forward(panjang_bata)

    tower += 1
    lebih_bata = lebar_tower * (nambah_tinggi)
    total_lebih_bata += lebih_bata
    nambah_tinggi += bedatinggi_tower

    #Memindahkan turtle ke area kosong untuk membuat tower selanjutnya
    t.goto(koor_x + (panjang_bata * jarak_tower), koor_y)

#Menghitung total bata yang digunakan
total_bata = (jumlah_tower * lebar_tower * tinggi_tower) + total_lebih_bata + ((lebar_tower + 1) * jumlah_tower)

#Menulis text summary yang berada di bawah tower
t.hideturtle()
t.penup()
t.goto(-340, -350) #Koor x dan y nya pake kira-kira 
t.pendown()
t.write(str(jumlah_tower) + " Super Mario Towers have been built with a total of " + str(total_bata) + " bricks", font=("verdana", 15, "normal"))
t.done()
layar.exitonclick()
