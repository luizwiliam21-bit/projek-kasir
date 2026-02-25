mahasiswa = [
    {"nama": "Andi", "nilai": 80},
    {"nama": "Budi", "nilai": 65},
    {"nama": "Citra", "nilai": 90},
    {"nama": "Dina", "nilai": 50}
]

tertinggi = mahasiswa[0]   # anggap sementara paling tinggi

for mhs in mahasiswa:
    if mhs["nilai"] > tertinggi["nilai"]:
        tertinggi = mhs

print("Mahasiswa dengan nilai tertinggi:")
print("Nama:", tertinggi["nama"])
print("Nilai:", tertinggi["nilai"])

terendah = mahasiswa[0]
for mhs in mahasiswa:
    if mhs["nilai"] < terendah["nilai"]:
        terendah = mhs

print("Mahasiswa dengan nilai terendah:")
print("Nama:", terendah["nama"])
print("Nilai:", terendah["nilai"])

for mhs in mahasiswa:
    if mhs["nilai"] > 85:
        mhs["status"] = "excellent"
    elif 70 <= mhs["nilai"] <= 85:
        mhs["status"] = "good"
    elif mhs["nilai"] < 70:
        mhs["status"] = "remedial"

print(mahasiswa)