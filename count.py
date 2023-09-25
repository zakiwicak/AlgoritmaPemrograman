from re import L


def hitung_hurufangka():
    s = input("input a string : ")
    d=l=0
    for c in s:
        if c.isdigit():
            d=d+1
        elif c.isalpha():
            l=l+1
        else:
            pass

print("letter", l)
print("letter", d)


def utama():
    print ("program hitung angka dan huruf")
    hitung_hurufangka()
    print("complete")