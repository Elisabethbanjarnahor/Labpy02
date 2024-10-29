def kalkulator():
  """Fungsi untuk menghitung operasi aritmatika sederhana"""

  angka1 = float(input("Masukkan angka pertama: "))
  angka2 = float(input("Masukkan angka kedua: "))
  operator = input("Masukkan operator (+, -, *, /): ")

  if operator == '+':
    hasil = angka1 + angka2
  elif operator == '-':
    hasil = angka1 - angka2
  elif operator == '*':
    hasil = angka1 * angka2
  elif operator == '/':
    if angka2 == 0:
      print("Tidak dapat membagi dengan nol.")
    else:
      hasil = angka1 / angka2
  else:
    print("Operator tidak valid.")

  if 'hasil' in locals():
    print("Hasil:", hasil)

kalkulator()