def duaangka():
    print("masukkan dua buah angka")
    print("dan anda akan check hubugna kedua angka tersebut")
    angka1 =int(input("masukkan angka pertama : "))
    angka2 =int(input("masukkan angka kedua : "))
    if angka1 == angka2 :
        print(angka1,"sama dengan angaka",angka2)
    else :
        print(angka1,"tidak sama dengan angka",angka2)

#memanggil fungsi diatas
duaangka()