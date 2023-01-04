data = {"nama":"dimas rio adisaputra"}
print(data["nama"])


nilai = { 'Firda':89, 'inaya':100, 'deden':59, 'ucup':67}

for skor in nilai.values():
    print (skor)

for skor in nilai.keys():
    print (skor)

for nama,nilai in nilai.items():
    print (nama, ":" ,nilai)