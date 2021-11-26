def ambil_dan_sisipkan(kalimat, i1, i2):
    hasil = kalimat + kalimat[i1-1] + kalimat[i2-1]
    return (hasil)

kalimat = str(input("masukan kalimat: "))
i1 = int(input("masukan index 1: "))
i2 = int(input("masukan index 2: "))

print (ambil_dan_sisipkan(kalimat,i1,i2))
