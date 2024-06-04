data_berat = {
    "Ali": 10,
    "Budi": 10,
    "Cici": 10,
    "Dodi": 10,
    "Evi": 0,  # Misalnya data yang salah, tapi kita belum tahu
}

def hitung_rata_rata_berat(data_berat):
    total_berat = 0
    jumlah_orang = 0
    for nama, berat in data_berat.items():    
        total_berat += berat
        jumlah_orang += 1
    rata_rata = total_berat / jumlah_orang
    return rata_rata

def test_hasil(hasil):
    if hasil == 10.0:
        print("test berhasil")
    else:
        print("test gagal")

if __name__ == '__main__':

    rata_rata_berat = hitung_rata_rata_berat(data_berat)
    test_hasil(rata_rata_berat)
    print(rata_rata_berat)  # Hasil yang salah: 8.0 || Hasil yang benar: 10.0