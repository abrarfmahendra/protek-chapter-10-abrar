file=open('nomor1.txt','r')
angka1=file.readlines()

angkagenap=[]
angkaganjil=[]

for i in range(len(angka1)) :
    if('\n' in angka1[i] == True) :
        angka1[i].replace('\n', '')
        if(int(angka1[i])%2 == 0) :
            angkagenap.append(angka1[i])
        else :
            angkaganjil.append(angka1[i])
    else :
        if(int(angka1[i])%2 == 0) :
            angkagenap.append(angka1[i])
        else :
            angkaganjil.append(angka1[i])

print('Banyaknya bilangan genap:{0}'.format(len(angkagenap)))
print('Banyaknya bilangan ganjil:{0}'.format(len(angkaganjil)))
