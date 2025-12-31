
import os

os.system("cls")

def proses(kamarTamu,durasiTamu,namaKamar,hargaKamar):
    jenis = namaKamar[kamarTamu-1]
    harga = hargaKamar[kamarTamu-1]
    hargaAsli = harga * durasiTamu
    diskon = [hargaAsli * 0.1, hargaAsli * 0.2, hargaAsli * 0.3]
    
    if durasiTamu >= 1 and durasiTamu <= 3:
        diskonTamu = diskon[0]
    elif durasiTamu >= 4 and durasiTamu <= 6:
        diskonTamu = diskon[1]
    else: 
        diskonTamu = diskon[2]
        
    totalHarga = hargaAsli - diskonTamu
    return [jenis,harga,hargaAsli,diskonTamu,totalHarga]
    



judul = "SISTEM INFORMASI PENYEWAAN KAMAR HOTEL ALFATIH"
header = "Daftar Jenis Kamar dan Harga"
header2 = "(per malam)"
tipeKamar = [1,2,3,4,5]
namaKamar = ["Tulip", "Teratai", "Anggrek", "Paviliun Rosalia", "Paviliun Cendana"]
hargaKamar = [500000, 1000000, 1500000, 2000000, 3000000]

# Header
print(f"{judul:^100}")
print(f"{header:^100}")
print(f"{header2:^100}")

# Menu
print(f"{60*"*":^100}")
print(f"{"":>17} {"Tipe Kamar":^20} {"Nama Kamar":<20} {"Harga Per Malam":<20}")

for i in range(len(tipeKamar)):
    print(f"{"":>17} {tipeKamar[i]:^20} {namaKamar[i]:<20} {"Rp" + str(hargaKamar[i]):<20}")
print(f"{60*"*":^100}")

while(True):
    kamarTamu = int(input("Pilih Tipe Kamar (1 - 5)    : "))
    durasiTamu = int(input("Berapa Malam Anda Menginap : "))
    
    hasilProses = proses(kamarTamu,durasiTamu,namaKamar,hargaKamar)
    jenis = hasilProses[0]
    harga = hasilProses[1]
    hargaAsli = hasilProses[2]
    diskonTamu = hasilProses[3]
    totalharga = hasilProses[4]
    
    print(50*"=")
    
    
    
    print(f"Anda Memilih Tipe Kamar        : {kamarTamu} ")
    print(f"Jenis Kamar                    : {jenis}")
    print(f"Harga Kamar Per Malam          : {harga}")
    print(f"Lama Menginap                  : {durasiTamu} Malam ")
    print(f"Total Harga Sebelum Diskon     : {hargaAsli} ")
    print(f"Harga Diskon                   : {diskonTamu} ")
    print(f"Total Harga yang Harus Dibayar : {totalharga}")
    
    konfirmasi = input("Anda Ingin Memilih Tipe Kamar Lagi [Y/T] : ").upper()
    if konfirmasi == "T":
        break

print("Terima Kasih, Anda telah melakukan pemesanan kamar pada Hotel Alfatih")