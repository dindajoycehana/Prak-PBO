from functools import wraps

class Smartphone:
  def __init__(self, brand, type):
    self.brand = brand
    self.type = type
    self.baterai = 100
    print(f"Smartphone {self.brand} {self.type} telah dibuat!")

  #destructor
  def __del__(self):
    print(f"Smartphone {self.brand} {self.type} telah dihapus!")

  # Decorator untuk mengecek baterai
  def cek_baterai(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
      if self.baterai <= 0:
        raise ValueError("Baterai smartphone habis!")
      return func(self, *args, **kwargs)
    return wrapper

  #method
  @cek_baterai
  def menelpon(self, nomor_tujuan):
    self.baterai -= 5
    print(f"Menelpon ke nomor {nomor_tujuan}")

  @cek_baterai
  def buka_aplikasi(self, nama_aplikasi):
    self.baterai -= 2
    print(f"Membuka aplikasi {nama_aplikasi}")

#Inisiasi object
Hp = Smartphone("Vivo", "S1 Pro")

#memanggil method
Hp.menelpon("087465392741")
Hp.buka_aplikasi("Instagram")

#untuk menguji ketika bateri habis
try:
  Hp.menelpon("08123456789")
except ValueError as e:
  print(e)

#menghapus
del Hp
