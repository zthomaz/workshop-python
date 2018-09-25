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
Kita bida mengkombinasikan range() dan len()
```
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])
```
maka ketika di running 
```
0 Mary
1 had
2 a
3 little
4 lamb
```

## Break, Continue dan Else pada perulangan
**BREAK** adalah sebuah pernyataan yang akan membuat sebuah program berhenti atau keluar dari suatu blok pengulangan. Dan semua kode setelah pernyataan break akan diabaikan. Pernyataan break ini dapat kita gunakan pada pengulangan while dan for
Berbeda dengan pernyataan break, pernyataan **CONTINUE** akan melakukan pengulangan mulai dari awal lagi. Dan akan mengabaikan semua kode yang tersisa pada loop untuk menuju awal loop lagi
Contoh **Break**
```
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')
```
maka hasilnya ketika di running
```
2 is a prime number
3 is a prime number
4 equals 2 * 2
5 is a prime number
6 equals 2 * 3
7 is a prime number
8 equals 2 * 4
9 equals 3 * 3
```
Contoh **Continue**
```
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found a number", num)
 ```
maka hasilnya ketika di running
```
Found an even number 2
Found a number 3
Found an even number 4
Found a number 5
Found an even number 6
Found a number 7
Found an even number 8
Found a number 9
```
## Pass Statement
Pernyataan **pass** tidak melakukan apa-apa. Ini dapat digunakan ketika pernyataan diperlukan secara sintaksis tetapi program tidak memerlukan tindakan.
```
while True:
    pass  # Busy-wait for keyboard interrupt (Ctrl+C)
```

## Defining Function
Kita dapat membuat fungsi yang menulis deret Fibonacci ke batas yang kita inginkan
```
def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
fib(2000)
```
maka hasilnya ketika di running
``` 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 ```
contoh lain
```
def fib2(n):  # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)    # see below
        a, b = b, a+b
    return result
f100 = fib2(100)    # call it
f100                # write the result
```
maka hasilnya ketika dirunning
``` [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] ```

## Nilai Default Argument
```
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)
```

