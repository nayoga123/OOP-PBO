class RekeningBank:
    def __init__(self, nama, saldo):
        self.nama = nama         # Public → bisa diakses dari luar
        self.__saldo = saldo     # Private → tidak bisa diakses langsung dari luar

    # Method untuk menampilkan saldo dengan aman
    def lihat_saldo(self):
        print("Error: Anda tidak memiliki akses langsung ke saldo!")

# --- Program utama ---
akun_budi = RekeningBank("Budi", 1000000)
print(f"Nama: {akun_budi.nama}")

# Mencoba mengakses saldo langsung dari luar class
try:
    print(akun_budi.__saldo) #ii akan menimbulkan erro !
except AttributeError:
        print("Error: saldo tidak dapat diakses langsung!")
# Jika ingin melihat saldo, harus lewat method:
akun_budi.lihat_saldo()