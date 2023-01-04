# nilaiX = int(input("Berapakah nilai X nya? "))
# nilaiY = int(input("Berapakah nilai Y nya? "))
# nilaiZ = int(input("Berapakah nilai Z nya? "))


# def PersamaanLinear(X,Y,Z):
#     print("Hasil dari persaman linear x^2 + 7y - z adalah")
#     return print( (X**2) + (7*Y) - Z)
# PersamaanLinear(nilaiX,nilaiY,nilaiZ)



# def pilihan(i):
#     switcher = {
#         1:'---Cuaca Hujan---',
#         2:'---Cuaca Adem---'
#     }
#     return switcher.get(i, "Masukan Pilihan Yang Benar")

# print("1. Hujan")
# print("2. Adem")
# nomor = int(input("Masukan Pilihan: "))
# cuaca = pilihan(nomor)
# print(cuaca)

# if nomor==1:
#     print("Karena Cuaca Hujan. Maka, Kuliah Naik Gocar")
# if nomor==2:
#     print("Karena Cuaca Adem. Maka, Kuliah Naik Motor")






#biodata

def biodata(nama,alamat,tanggal,umur,tb):
    
    print ("nama  : "+nama)
    print ("alamat : "+alamat)
    print ("tanggal lahir : "+tanggal)
    print ("umur : "+umur)
    print ("tinggi badan : ",tb)
    berat_ideal = int (tb) - 110
    print("Berat badan ideal :",berat_ideal)

biodata(" dimas","depok","jakarta 16 03 04","18","179")