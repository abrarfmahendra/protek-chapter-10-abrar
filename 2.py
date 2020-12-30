print ("Data Mahasiswa")
print ("Format : nim | nama mhs| alamat ")
print('-' *30)
print ("Data akan tersimpan dengan nama \"file.txt\" di folder yang sama")
file = open ("file.txt", 'a+')
status = True
while status == True :
    data = []
    nim = input ("NIM Mahasiswa/i : ")
    data.append(nim)
    nama = input ("Nama Mahasiswa/i : ")
    data.append(nama)
    alamat = input ("Alamat : ")
    data.append(alamat)
    gabung = ' | '.join(data)
    file.write(gabung + '\n')
    konfirmasi = input ("Ingin menambahkan lagi? (y/n) : ")
    if konfirmasi != 'y' :
        print ("File tersimpan")

        file.close()
        status = False
