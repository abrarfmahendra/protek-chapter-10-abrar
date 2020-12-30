cariNIM = input('NIM yang dicari : ')
file = open('file.txt', 'r')
a = file.readlines()

for i in range(len(a)) :
    if(cariNIM in a[i]) :
        status = 'ada'
        break
    else :
        status = 'tidak ada'
        continue
if(status == 'ada') :
        b = a[i].split('|')
        print("\nData Mahasiswa ")
        print("NIM : ", b[0])
        print("Nama : ", b[1])
        print("Alamat : ", b[2])
else :
    print("Data Mahasiswa Tidak Ditemukan")
