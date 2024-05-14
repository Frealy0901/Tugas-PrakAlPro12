nama = input("Masukkan nama file: ")
try:
    file = open(nama)
except:
    print(f"{nama} is not found!")
    quit()

jam_dict = dict()
for garis in file:
    if garis.startswith('From '):
        words = garis.split()
        waktu = words[5]
        jam = waktu[:2]
        jam_dict[jam] = jam_dict.get(jam, 0) + 1

hours_list = sorted(jam_dict.items())

for jam, count in hours_list:
    print(jam, count)