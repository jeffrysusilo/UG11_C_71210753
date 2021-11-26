def nilai(list_nilai):
    list_nilai.sort()
    tertinggi=max(list_nilai)
    terendah=min(list_nilai)
    rata_rata=sum(list_nilai)/len(list_nilai)
    print ("nilai tertinggi adalah:",tertinggi)
    print ("nilai terendah adalah:",terendah)
    print ("nilai rata rata adalah:",rata_rata)
    return (list_nilai)







daftar_nilai1 = [10,40,30,53,50]
daftar_nilai2 = [99,78,89,85,46]
daftar_nilai3 = [57,90,76,85,78]
print(nilai(daftar_nilai1))
