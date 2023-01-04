hasil_akhir = [
    { 'nama':'dimas', 'nilai':70 },
    { 'nama':'Cut tari', 'nilai':63 },
    { 'nama':'zinedine', 'nilai':80 },
    { 'nama':'indra', 'nilai':40 }
]
siswalulus = []
for siswa in hasil_akhir:
    if siswa ['nilai'] > 65:
        siswalulus.append(siswa ['nama'])
print(siswalulus)