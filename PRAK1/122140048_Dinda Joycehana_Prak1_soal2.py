def hitung_lingkaran(r):

  if r < 0:
    print("Jari-jari lingkaran tidak boleh negatif")
    return

  phi = 3.14
  luas = phi * r**2
  keliling = 2 * phi * r

  print(f"Luas lingkaran dengan jari-jari {r} adalah {luas}")
  print(f"Keliling lingkaran dengan jari-jari {r} adalah {keliling}")

r = float(input("Masukkan jari-jari lingkaran: "))

hitung_lingkaran(r)
