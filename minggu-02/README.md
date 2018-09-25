# Thomas Prayudhi Triutomo
# Minggu ke dua

# IF (Kondisi/Percabangan)
Percabangan/pengambilan keputusan adalah pengkondisian yang terjadi ketika aplikasi berjalan, kemudian ada aksi-aksi tertentu atau kondisi tertentu sehingga aplikasi harus bereaksi terhadap hal itu. Atau dalam bahasa pemrograman umum dikenal dengan IF, THEN, ELSE.


| Statement | Deskripsi |
| ---------------------------- | ------------------------------ |
| IF | Mengandung expresi boolean dan diikuti oleh satu atau banyak statement | 
| IF ELSE ELIF | IF bisa diikuti oleh optional statemen yaitu ELSE, yang akan dieksekusi ketika ekspresi boolean bernilai FALSE | 
| NESTED IF atau IF bersarang | Kita bisa menggunakan IF, ELSE IF di dalam IF, ELSE IF lainnya | 


```x = int(input("Please enter an integer: "))
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')```

maka ketika di running hasilnya ```More```
