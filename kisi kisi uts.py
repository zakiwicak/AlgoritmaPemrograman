#data = int(input("masukken dek :"))
#print(data)

rupiah = input(int("masukkan berapa dolar:"))
dolar = input(int("masukkan berapa dolar"))

def konfersikeusd(rupiah):
    return(dolar/rupiah)
print("jadi anda memiliki",(konfersikeusd(rupiah)))

def konfersikeidr(dolar):
    return(rupiah/dolar)
print("jadi anda memiliki",(konfersikeidr(dolar)))
