def hitung_ganjil(lower, upper):
  
  if lower < 0 or upper < 0:
    print("Batas bawah dan atas yang dimasukan tidak boleh di bawah Nol")
    return

  jumlah_ganjil = 0
  for i in range(lower, upper ):
    if i % 2 == 1:
      jumlah_ganjil += 1
      print(i)

  print(f"Jumlah bilangan ganjil dalam rentang {lower} hingga {upper} adalah {jumlah_ganjil}")

lower = int(input("Masukkan batas bawah: "))
upper = int(input("Masukkan batas atas: "))

hitung_ganjil(lower, upper)