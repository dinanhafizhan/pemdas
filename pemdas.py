data_panen = {
    'lokasi1':{
        'nama_lokasi': 'kebun A',
        'hasil_panen':{
            'padi': 1200,
            'jagung': 800,
            'kedelai': 500
        }
    },
    'lokasi2':{
        'nama_lokasi': 'kebun B',
        'hasil_panen':{
            'padi': 1500,
            'jagung': 900,
            'kedelai': 450
        }
    },
    'lokasi3':{
        'nama_lokasi': 'kebun C',
        'hasil_panen':{
            'padi': 1100,
            'jagung': 750,
            'kedelai': 600
        }
    },
    'lokasi4':{
        'nama_lokasi': 'kebun D',
        'hasil_panen':{
            'padi': 1300,
            'jagung': 850,
            'kedelai': 550
        }
    },
    'lokasi5':{
        'nama_lokasi': 'kebun E',
        'hasil_panen':{
            'padi': 1400,
            'jagung': 950,
            'kedelai': 480
        }
    }            
}

print("="*100)
# Menampikan semua data pada dictionary data panen
for i,j in data_panen.items():
    print(i,j)

print("="*100)

# Jumlah hasil panen jagung lokasi 3
print("Jumlah hasil panen jagung pada lokasi 3 :", data_panen['lokasi3']['hasil_panen']['jagung'])

print("="*100)

# Tampilkan nama lokasi dari lokasi 3
print("nama lokasi pada lokasi 3 :", data_panen['lokasi3']['nama_lokasi'])


print("="*100)
# Masukkan Jumlah Hasil Panen Padi dan Kedelai Setiap Lokasi ke Dalam Variabel yang Berbeda 
# Buat variabel terpisah untuk menyimpan jumlah hasil panen padi dan kedelai dari setiap lokasi.
#Buat Percabangan Jika jumlah hasil panen padi lebih dari 1300 atau jagung lebih dari 800 di suatu lokasi, maka lokasi tersebut memerlukan perhatian khusus. Jika tidak, maka lokasi tersebut dalam kondisi baik.

for nama, lokasi in data_panen.items():
    nama = lokasi['nama_lokasi']
    padi = lokasi['hasil_panen']['padi']
    kedelai = lokasi['hasil_panen']['kedelai']
    jagung = lokasi['hasil_panen']['jagung']

    if padi > 1300 or jagung > 800:
        print(f"{nama} memerlukan perhatioan khusus")
    else:
        print(f"{nama} dalam kondisi baik")
    
print("="*100)