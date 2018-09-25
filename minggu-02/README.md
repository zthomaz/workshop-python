# Thomas Prayudhi Triutomo
# Minggu ke dua

## IF ( Kondisi/Percabangan )
Percabangan/pengambilan keputusan adalah pengkondisian yang terjadi ketika aplikasi berjalan, kemudian ada aksi-aksi tertentu atau kondisi tertentu sehingga aplikasi harus bereaksi terhadap hal itu. Atau dalam bahasa pemrograman umum dikenal dengan IF, THEN, ELSE.


| Statement | Deskripsi |
| ---------------------------- | ------------------------------ |
| IF | Mengandung expresi boolean dan diikuti oleh satu atau banyak statement | 
| IF ELSE ELIF | IF bisa diikuti oleh optional statemen yaitu ELSE, yang akan dieksekusi ketika ekspresi boolean bernilai FALSE | 
| NESTED IF atau IF bersarang | Kita bisa menggunakan IF, ELSE IF di dalam IF, ELSE IF lainnya | 


```
x = int(input("Please enter an integer: "))
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')
 ```
maka ketika di running hasilnya ```More```

## FOR ( PERULANGAN )
Terdapat dua jenis perualangan dalam bahasa pemrograman python, yaitu perulangan dengan for dan while.
Perulangan for disebut counted loop (perulangan yang terhitung), sementara perulangan while disebut uncounted loop (perulangan yang tak terhitung). Perbedaannya adalah perulangan for biasanya digunakan untuk mengulangi kode yang sudah diketahui banyak perulangannya. Sementara while untuk perulangan yang memiliki syarat dan tidak tentu berapa banyak perulangannya.
```
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))
 ```
 maka hasilnya ketika di running ```cat 3 window 6 defenestrate 12```
```
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

for w in words[:]:  # Loop over a slice copy of the entire list.
    if len(w) > 6:
        words.insert(0, w)
print(words)
```
Maka ketika dirunning
```
cat 3
window 6
defenestrate 12
['defenestrate', 'cat', 'window', 'defenestrate']
```

## Range Function
Jika kita perlu melakukan perulangan dengan urutan angka, maka fungsi range sangat berguna. Ini menghasilkan progresi aritmetika:
```
for i in range(5):
    print(i)
```
maka ketika dirunning hasilnya
```
0
1
2
3
4
```
Contoh lain
```
range(5, 10)
   5, 6, 7, 8, 9

range(0, 10, 3)
   0, 3, 6, 9

range(-10, -100, -30)
  -10, -40, -70
```



