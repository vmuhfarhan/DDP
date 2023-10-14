#Menginput pesan kelompok zog dan angka 1 & 2 lalu menyimpan ke masing-masing variabel
pesan_kelompok_zog = str(input('Pesan Kelompok Zog: '))
angka_1 = int(input('Angka 1: '))
angka_2 = int(input('Angka 2: '))

#Mengubah nilai variabel pesan_kelompok_zog yang berupa hexadecimal menjadi bentuk ASCII
bytes_string = bytes.fromhex(pesan_kelompok_zog)
isi_pesan = bytes_string.decode("ASCII")

#Membuat rumus password, yaitu dengan mengalikan angka_1 dengan angka_2 dan 13 sesuai instruksi soal
rumus_password = angka_1 * angka_2 * 13

#Mengubah nilai variabel rumus_password yang berupa angka menjadi bentuk biner
password_pesan = bin(rumus_password)

#Mencetak output yang terdiri dari variabel isi_pesan dan password_pesan
print(f'\nHasil terjemahan pesan: {isi_pesan}')
print(f'Password: {password_pesan}')
print(f'\nPesan "{isi_pesan}" telah diterima dengan password "{password_pesan}".')

