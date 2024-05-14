data_diri = ('Revaldo Fransisco Hohary', 71231042, 'Biak, Papua')

print('Data:', data_diri)
print('NIM :', data_diri[1])
print('NAMA :', data_diri[0])
print('ALAMAT :', data_diri[2])

nim = tuple(str(data_diri[1]))
print('NIM :', nim)

nama = tuple(data_diri[0].split()[0])
print('NAMA DEPAN :', nama)

terbalik = tuple(reversed(data_diri[0].split()))
print('NAMA TERBALIK :', terbalik)