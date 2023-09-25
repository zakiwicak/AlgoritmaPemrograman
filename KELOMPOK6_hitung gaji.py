print("PROGRAM GAJI KARYAWAN")
def penggajian(masakerja):
    if masakerja >= 10:
        tunjangan = 10000000
    elif masakerja >= 8 and masakerja < 10:
        tunjangan = 6000000
    elif masakerja >= 6 and masakerja <8:
        tunjangan = 3000000
    elif masakerja >= 4 and masakerja <6:
        tunjangan = 2000000
    else:
        tunjangan = 500000
    return tunjangan

def gatot(gaji,tunjangan):
    total = gaji + tunjangan
    return total

#main
gaji = int(input("masukan gaji karyawan = "))
masakerja = int(input("berapa tahun anda kerja = "))
totalgaji = gatot(gaji,penggajian(masakerja))
print(f"gaji total anda adalah = {totalgaji:,}")