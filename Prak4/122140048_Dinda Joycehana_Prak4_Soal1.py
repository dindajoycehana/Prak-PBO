class Hewan :
    def __init__(self, nama, jenis_kelamin):
        self.nama = nama
        self.jenis_kelamin = jenis_kelamin

    def bersuara(self):
        pass

    def makan(self):
        pass
    @property
    def minum(self):
        print(f"{self.nama} sedang minum air")

class Kucing(Hewan) :
    def __init__(self, nama, jenis_kelamin):
        super().__init__(nama,jenis_kelamin)
    @property
    def bersuara(self):
        print(f"Kucing {self.nama} bersuara: Meong!")
    @property
    def makan(self):
        print(f"Kucing {self.nama} sedang makan : tulang")

class Anjing(Hewan) :
    def __init__(self, nama, jenis_kelamin):
        super().__init__(nama,jenis_kelamin)
    @property
    def bersuara(self):
        print(f"Anjing {self.nama} bersuara: Guk Guk!")
    @property
    def makan(self):
        print(f"Anjing {self.nama} sedang makan : tulang")

hewan1 = Kucing("Kiki", "Betina")
hewan2 = Anjing("Ichi", "Jantan")
print(hewan1.nama) 
print(hewan2.nama) 

hewan1.bersuara
hewan1.makan
hewan1.minum
hewan2.bersuara
hewan2.makan
hewan2.minum