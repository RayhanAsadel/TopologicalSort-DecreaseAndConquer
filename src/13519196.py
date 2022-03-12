# NIM : 13519196
# Nama : Rayhan Asadel
# Kelas : K-04
########################################

#Kamus Fungsi dan Prosedur

def listToString(s):  
    #Fungsi yang mengubah suatu list s menjadi string str1
    
    str1 = ""  

    for ele in s:  
        str1 += ele    
   
    return str1 

def inputfiletoArray():
    #prosedur yang menerima dan mengolah input file text menjadi matriks adjacency (representasi DAG dengan adjacency list)
    print()
    filename = str(input("Masukan Nama File (Nama.txt): "))         #Masukan nama file dengan format "Nama.txt"
    print()
    with open('../test/'+filename,'r') as file:
        
        #Konversi isi file txt menjadi string yang bersih dari karakter2 pemisah dan "\n"
        ListKiri = []       #Listkiri untuk menampung sementara hasil dari file text
  
        for line in file:
            if line.startswith('-'):
                continue
            else:
                ListKiri.append(line.replace(',','').replace(' ','').replace('C','').replace('\n',' '))
        
        Str = listToString(ListKiri)
        Str = Str.split(' ')
        panjangArr = len(Str)
        Str = listToString(Str)
        panjangString = len(Str)

        #arrayInt merupakan adjacency list, dengan baris sebagai simpul (matkul), dan kolom sebagai prerequisite
        arrayInt = [[0 for x in range(panjangArr)] for y in range(panjangArr)] 
    
        j = 0
        baris = 0
        kolom = 0
        for i in range(1,panjangString):
            Angka = Str[j:i]
            j = j+1

            if (Angka =='.'):
                baris = baris+1
                kolom = 0
            else:
                Angka = int(Angka)
                for n in range (panjangArr+1):                
                    if (n == Angka):
                        if (Angka-1==baris):
                            arrayInt[baris][n-1] = 0
                            kolom = kolom+1
                        else:
                            arrayInt[baris][n-1] = 1
                            kolom = kolom+1

        return arrayInt         ## mereturn matriks dengan elemen[n][0] adalah matkul n, dan elemen[n][1..n] adalah prereq dari matkul n

def findLowestInDegree(matriks):
    #Mencari elemen dengan in degree 0, pada matriks, dan mengeluarkan posisi barisnya
    min = 0
    sum = 0      
    indeksMatkul = -1;

    for i in range(1):
        sum = 0
        for j in range(len(matriks)):
            if (matriks[i][j]!=-1):
                sum = sum + matriks[i][j]

    counter = 0
    for i in range(len(matriks)):
        sum = 0
        counter = 0
        for j in range(len(matriks)):
            if (matriks[i][j]!=-1):
                sum = sum + matriks[i][j]
            else:
                counter = counter + matriks[i][j]

        if (sum == 0) and (counter!=(len(matriks)*-1)) :
            
            indeksMatkul = i
    
    return indeksMatkul

def deleteVertexAndConnection(matriks,indeksMatkul):
    #Menghapus simpul dengan posisi baris indeksMatkul, dan semua busur yang keluar dari simpul tersebut
    for i in range(len(matriks)):
        for j in range(len(matriks)):
            if (i==indeksMatkul):
                matriks[indeksMatkul][j] = -1
            elif (j==indeksMatkul) and (matriks[i][indeksMatkul]==1) :
                matriks[i][indeksMatkul] = -1
    
    return matriks

def findCountZeroDegree(matriks):
    #Mencari ada berapa simpul yang memiliki in degree = 0
    nZeroDegrees = 0
    counter = 0
    for i in range(len(matriks)):
        sum = 0
        counter = 0
        for j in range(len(matriks)):
            if (matriks[i][j]!=-1):
                sum = sum + matriks[i][j]
            else:
                counter = counter + matriks[i][j]
                
        if (sum == 0) and (counter!=(len(matriks)*-1)) :
            nZeroDegrees = nZeroDegrees + 1
    
    return nZeroDegrees
   

## ALGORITMA UTAMA

hasilSortArray = []     #Sebagai array penerima hasil sorting
matriks = inputfiletoArray()
sizeMatriks = len(matriks)

print("Ini Adalah Representasi Matriks dari File Text Anda: ")
print("Dengan Dimensi:",end=' ')
print(sizeMatriks)

for i in range(len(matriks)):
    for j in range(len(matriks)):
        print(matriks[i][j],end='')     #menampilkan matriks
    print()
print()

i = 0
j = 0
ParamLoop = 0
while (i<sizeMatriks):      #topological sort, dengan makin lama baris matriks yang dicek semakin sedikit (decrease by a variable size)
    ParamLoop = findCountZeroDegree(matriks)
    semester = []

    for j in range(ParamLoop):      #loop untuk menentukan >1 matkul pada 1 semester
        target = findLowestInDegree(matriks)
        matriks = deleteVertexAndConnection(matriks,target)
        semester = semester + ['C'+str(target+1)]
    i = i + ParamLoop
    hasilSortArray.append([semester])

#endwhile

panjangHasilSort = len(hasilSortArray)

if (panjangHasilSort>8):
    print("Solusi tidak dapat ditampilkan, perlu lebih dari 8 semester")
else:
    print("Berikut Adalah Rencana Kuliah Anda")
    for i in range(0,panjangHasilSort):
        print("Semester ",i+1,": ",hasilSortArray[i])

    