def check_data_type (td,tebakan):
    cekdata = tebakan.lower()
    
    if td == []:
        tipe="list"
        if cekdata == "list":
            print ("jawaban anda benar")
        else:
            print ("jawaban anda salah, seharusnya asalah: list")
    elif td == {}:
        tipe="dict"
        if cekdata == "dict":
            print ("jawaban anda benar")
        else:
            print ("jawaban anda salah, seharusnya asalah: dict")
    elif td == (True or False):
        tipe="bool"
        if cekdata == "bool":
            print ("jawaban anda benar")
        else:
            print ("jawaban anda salah, seharusnya asalah: bool")
    elif td == ():
        tipt="tuple"
        if cekdata == "tuple":
            print ("jawaban anda benar")
        else:
            print ("jawaban anda salah, seharusnya asalah: tuple")
    else:
        print ("invalid input")

    return (cekdata == tipe)


print(check_data_type(True,"Bool"))
print(check_data_type(True,"bool"))
print(check_data_type({},"TUPLE"))
print(check_data_type({},"DIct"))
print(check_data_type([],""))
