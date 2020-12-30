file=open('file.txt', 'r')
baris=file.readlines()
dicti={}
listDict=[]
for i in range(len(baris)) :
    a=baris[i].split('|')
    a[2]=a[2].replace('\n', '')
    dicti={'nim' : a[0], 'nama' : a[1], 'alamat' : a[2]}
    listDict.append(dicti)
print(listDict)
