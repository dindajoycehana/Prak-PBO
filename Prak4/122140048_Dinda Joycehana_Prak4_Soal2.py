class Persegi :
    def __init__(self, sisi):
        self.sisi = sisi 
    
    def hitungLuas(self):
        print(f"Luas Persegi : {self.sisi * self.sisi}")

class Lingkaran :
    def __init__(self, jari2):
        self.jari2 = jari2
    
    def hitungLuas(self):
        print(f"Luas Lingkaran : {(22/7) * self.jari2 * self.jari2}")

persegi = Persegi(5)
lingkaran = Lingkaran(3)

persegi.hitungLuas()
lingkaran.hitungLuas()