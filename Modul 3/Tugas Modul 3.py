class Pegawai:
    def __init__(self, nama, nip, gaji_pokok):
        self.nama = nama
        self.nip = nip
        self.__gaji_pokok = gaji_pokok   # private

    # Getter gaji pokok
    def get_gaji_pokok(self):
        return self.__gaji_pokok

    # Bonus default = 0
    def hitung_bonus(self):
        return 0

    # Hitung total gaji
    def get_gaji_total(self):
        return self.__gaji_pokok + self.hitung_bonus()

    # Tampilkan info dasar pegawai
    def tampilkan_info(self):
        pass

#   CLASS MANAGER
class Manager(Pegawai):
    def __init__(self, nama, nip, gaji_pokok, tunjangan_jabatan):
        super().__init__(nama, nip, gaji_pokok)
        self.tunjangan_jabatan = tunjangan_jabatan

    def hitung_bonus(self):
        return self.get_gaji_pokok() * 0.15  # 15%

    def tampilkan_info(self):
        print("--- Info Manager ---")
        print(f"Nama: {self.nama}, NIP: {self.nip}")
        print(f"Gaji Pokok: Rp {self.get_gaji_pokok():,}")
        print(f"Tunjangan: Rp {self.tunjangan_jabatan:,}")
        print(f"Gaji Total Manager: Rp {self.get_gaji_total():,}")
        print("\n==============================\n")

#   CLASS STAFF TEKNIS
class StaffTeknis(Pegawai):
    def __init__(self, nama, nip, gaji_pokok, jumlah_proyek):
        super().__init__(nama, nip, gaji_pokok)
        self.jumlah_proyek = jumlah_proyek

    def hitung_bonus(self):
        return 500_000 * self.jumlah_proyek

    def tampilkan_info(self):
        print("--- Info Staff Teknis ---")
        print(f"Nama: {self.nama}, NIP: {self.nip}")
        print(f"Gaji Pokok: Rp {self.get_gaji_pokok():,}")
        print(f"Jumlah Proyek: {self.jumlah_proyek}")
        print(f"Gaji Total Staff: Rp {self.get_gaji_total():,}")
        print("\n==============================\n")

#   CONTOH OBJEK
manager1 = Manager("Budi Hartono", "M-001", 10_000_000, 5_000_000)
staff1 = StaffTeknis("Susi Susanti", "S-001", 6_000_000, 3)

# Cetak info
manager1.tampilkan_info()
staff1.tampilkan_info()

#   BUKTI ENKAPSULASI
print("--- Tes Keamanan (Encapsulasi) ---")
try:
    print(staff1.__gaji_pokok)   # HARUS ERROR
except AttributeError:
    print("ERROR: 'StaffTeknis' object has no attribute '__gaji_pokok'")
    print("-> TIDAK BISA diakses langsung dari luar!")

print(f"Gaji Total Susi (tetap): Rp {staff1.get_gaji_total():,}")