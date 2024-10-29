Nama   :ELISABETH BANJARNAHOR
NIM    :312410525
Kelas  :TI.24.A5
Matkul : Bahasa Pemrograman


# Kasus 1: Program Pemesanan Tiket Bioskop.

Buat program yang menghitung harga tiket bioskop. Tiket reguler berharga Rp50.000, sedangkan tiket VIP berharga Rp100.000. Jika user memiliki kartu member, mereka mendapatkan diskon 20% dari harga tiket. Program ini harus meminta tipe tiket dan status. member dari user, lalu menghitung total harga yang harus dibayar.
Petunjuk:
Gunakan if else dan operator ternary.


## Flowchart pemograman


"python"
```ruby
def hitung_harga_tiket():
    jenis_tiket = input("Masukkan jenis tiket (reguler/VIP): ").lower()
    status_member = input("Apakah Anda memiliki kartu member? (ya/tidak): ").lower()

    harga_reguler = 50000
    harga_vip = 100000

    harga_awal = harga_reguler if jenis_tiket == 'reguler' else harga_vip
    diskon = 0.2 if status_member == 'ya' else 0
    harga_akhir = harga_awal * (1 - diskon)

    print("Total harga yang harus dibayar: Rp", harga_akhir)

hitung_harga_tiket()
```

penjelasan Codingan:

def: Menandai awal dari definisi sebuah fungsi.
hitung_harga_tiket(): Adalah nama yang kita berikan untuk fungsi tersebut. Nama ini harus unik dan mencerminkan apa yang dilakukan oleh fungsi tersebut.
jenis_tiket = input("Masukkan jenis tiket (reguler/VIP): ").lower()

```input()```: Fungsi ini digunakan untuk meminta pengguna memasukkan data dari keyboard. Dalam hal ini, kita meminta pengguna untuk memasukkan jenis tiket yang diinginkan.
```.lower()```: Fungsi ini digunakan untuk mengubah semua huruf dalam input menjadi huruf kecil. Jadi, baik pengguna mengetik "reguler" atau "Reguler", hasilnya akan sama.
```ruby
status_member = input("Apakah Anda memiliki kartu member? (ya/tidak): ").lower()
```

Sama seperti baris sebelumnya, kita meminta pengguna memasukkan status keanggotaannya dan mengubah semua huruf menjadi huruf kecil.
```ruby
harga_reguler = 50000 dan harga_vip = 100000
```

Di sini kita mendefinisikan harga dasar untuk masing-masing jenis tiket. Jadi, jika pengguna memilih tiket reguler, maka harga awalnya adalah Rp50.000.
```ruby
harga_awal = harga_reguler if jenis_tiket == 'reguler' else harga_vip
``` 

Baris ini digunakan untuk menentukan harga awal berdasarkan jenis tiket yang dipilih pengguna.
```ruby
diskon = 0.2 if status_member == 'ya' else 0
```

Di sini kita menentukan besarnya diskon. Jika pengguna memiliki kartu member (menjawab "ya"), maka diskonnya adalah 20% (0.2). Jika tidak, maka tidak ada diskon (0).
```ruby
harga_akhir = harga_awal * (1 - diskon)
```

Kita menghitung harga akhir dengan cara mengurangi harga awal dengan besar diskon
```ruby
print("Total harga yang harus dibayar: Rp", harga_akhir)
```

Fungsi ```print()``` digunakan untuk menampilkan hasil perhitungan ke layar.
```hitung_harga_tiket()```
Baris terakhir ini digunakan untuk memanggil fungsi ```hitung_harga_tiket()``` yang telah kita definisikan sebelumnya.

## screenshot hasil code 


# Kasus 2: Program Kalkulator Sederhana

Buat program kalkulator yang menerima dua angka dan satu operator aritmatika dari pengguna (penjumlahan, pengurangan, perkalian, atau pembagian). Program akan menghitung hasil sesuai dengan operator yang dipilih.
Petunjuk:
Gunakan if elif else untuk menentukan operasi aritmatika.


## flowchart pemograman


``python``
```ruby
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
```

## penjelasan setiap code

```def kalkulator()```:
Ini adalah baris untuk mendefinisikan sebuah fungsi bernama kalkulator. Fungsi ini akan berisi kumpulan perintah yang akan dijalankan ketika fungsi ini dipanggil.

### Fungsi untuk menghitung operasi aritmatika sederhana

Ini adalah dokumentasi (docstring) yang menjelaskan tujuan dari fungsi kalkulator.
```ruby
angka1 = float(input("Masukkan angka pertama: "))
```
Baris ini meminta pengguna untuk memasukkan angka pertama dan menyimpannya dalam variabel angka1. Fungsi float() digunakan untuk mengubah input pengguna menjadi bilangan desimal.
```ruby
angka2 = float(input("Masukkan angka kedua: "))
```
Sama seperti di atas. 
```ruby
operator = input("Masukkan operator (+, -, *, /): ")
```
Baris ini meminta pengguna untuk memasukkan operator yang ingin digunakan (+, -, *, atau /) dan menyimpannya dalam variabel operator
```ruby
if operator == '+':
```
Ini adalah awal dari sebuah kondisi if. Jika operator yang dipilih adalah '+', maka program akan menjalankan perintah di dalam blok if ini.
```ruby
hasil = angka1 + angka2
```
Jika kondisi if benar, maka hasil penjumlahan angka1 dan angka2 akan disimpan dalam variabel hasil
```ruby
elif operator == '-':
```
Ini adalah kondisi elif (kependekan dari else if). Jika kondisi if sebelumnya salah, tetapi operator adalah '-', maka program akan menjalankan perintah di dalam blok elif ini.
```ruby
hasil = angka1 - angka2
```
Jika kondisi elif benar, maka hasil pengurangan angka1 dan angka2 akan disimpan dalam variabel hasil
```ruby
elif operator == '*' dan elif operator == '/':
```
Kondisi elif ini bekerja dengan cara yang sama seperti sebelumnya, tetapi untuk operasi perkalian dan pembagian
```ruby
if angka2 == 0:
```
Dalam kasus pembagian, program akan memeriksa apakah angka2 bernilai 0. Jika iya, maka tidak dapat dilakukan pembagian karena pembagian dengan nol tidak terdefinisi.
```ruby
print("Hasil:", hasil)
```
Jika variabel hasil sudah memiliki nilai (artinya, operasi telah dilakukan dengan benar), maka program akan mencetak hasil perhitungan.
kalkulator()
Baris terakhir ini memanggil fungsi kalkulator() sehingga semua perintah di dalam fungsi akan dijalankan.


## screenshot hasil code 
