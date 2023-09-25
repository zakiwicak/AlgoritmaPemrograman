def usdkeidr(usd):
    return usd*15000

def idrkeusd(idr):
    return idr/15000


print("Pilih Perhitungan:")
print("1.usd ke idr")
print("2.idr ke usd")

while True:
    pilihan = input("Pilih Nomor: ")
    
    if pilihan in ('1', '2'):
        inputan = float(input("berapa nominal yang mau di konvers :  "))

        if pilihan == '1':
            print('rp',usdkeidr(inputan))

        elif pilihan == '2':
            print('usd',idrkeusd(inputan))

        reset = input("Mau menghitung lagi? (ya/tidak): ")
        if reset == "tidak":
          break
        
    else:
        print("Inputan salah")
        
#https://www.ekorkode.com/2022/10/python-program-kalkulator-sederhana-source-code-full-fungsi-looping.html