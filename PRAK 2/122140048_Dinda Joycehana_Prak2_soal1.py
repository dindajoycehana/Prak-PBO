class Mahasiswa:
    def __init__(self, nim, nama, angkatan, ismahasiswa=True):
        self.nim = nim
        self.nama = nama
        self.angkatan = angkatan
        self.ismahasiswa = ismahasiswa

    def Display1(self):
        return f"""
        NIM: {self.nim}
        Nama: {self.nama}
        Angkatan: {self.angkatan}
        Status: {self.ismahasiswa}
        """

    def Display2(self):
        return f"{self.nama} dengan NIM {self.nim} merupakan mahasiswa ITERA angkatan {self.angkatan}\n"

    def Display3(self):
        return f"{self.nama} merupakan seorang mahasiswa ITERA"

    @property
    def get_nim(self):
        return self.nim

    @get_nim.setter
    def set_nim(self, nomorindukmahasiswa):
        self.nim = nomorindukmahasiswa
    
    @property
    def get_nama(self):
        return self.nama

    @get_nama.setter
    def set_nama(self, namamhs):
        self.nama = namamhs


data1 = Mahasiswa(122140048, "Dinda Joycehana", 2022, True)
data2 = Mahasiswa(123140123, "Prabowo S.", 2023)

print(data1.Display1())
print(data1.Display2())
print(data1.Display3())
print("\n")
print(data2.Display1())
print(data2.Display2())
print(data2.Display3())