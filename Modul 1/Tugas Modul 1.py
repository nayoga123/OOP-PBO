class PersegiPanjang:
    # Constructor untuk inisialisasi atribut
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    # Method untuk menghitung luas
    def hitung_luas(self):
        return self.panjang * self.lebar

    # Method untuk menghitung keliling
    def hitung_keliling(self):
        return 2 * (self.panjang + self.lebar)

# Program utama
print("=== Program Menghitung Luas dan Keliling Persegi Panjang ===")
p = float(input("Masukkan panjang: "))
l = float(input("Masukkan lebar: "))

# Membuat objek dari class PersegiPanjang
pp = PersegiPanjang(p, l)

# Menampilkan hasil
print(f"\nLuas Persegi Panjang     : {pp.hitung_luas()}")
print(f"Keliling Persegi Panjang : {pp.hitung_keliling()}")