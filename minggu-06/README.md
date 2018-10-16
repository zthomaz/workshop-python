# Thomas Prayudhi
# Minggu ke enam

## 	Penanganan Error dan Exception

### Error
Error adalah kejadian pada program yang tidak sesuai dengan yang diharapkan karena kesalahan dari pengguna program. Error sifatnya terprediksi dan dapat ditangani kejadiannya. Pengertian error secara umum adalah ‘kesalahan’, akan tetapi pengartian Error juga dapat di kelompokkan menurut penggunaan kata-katanya, contohnya Error dalam pengertian ilmu komputer yaitu tidak sanggup menampilkan data (tidak dapat melanjutkan ke system berikutnya).

### Exception
Exception artinya adalah pengecualian, yang di maksud dengan exception adalah kondisi yang akan muncul, jika suatu program tidak sukses di jalankan, atau dengan kata lain, user tidak mengisi input sesuai syarat yang berlaku. Atau dengan defini lain exception adalah suatu konstruksi suatu bahasa khusus untuk menangani keadaan yang tidak terduga (biasanya adalah error); status keadaan error.
Selama program berjalan, dapat terjadi sesuatu hal yang menyebabkan error. Misalnya, array diberi nilai indeks yang melebihi nilai indeks yang sudah dideklarasikan, atau suatu operasi aritmatika yang membagi suatu bilangan dengan nol. Hal ini dapat mengakibatkan program berhenti tidak seperti yang diinginkan dan biasanya menampilkan pesan kesalahan yang tidak jelas.
Bahasa pemrograman harus menyediakan fasilitas untuk mendefinsikan eksepsi, mengenali kemunculan eksepsi dan menentukan kode-kode apa yang harus dieksekusi ketika eksepsi muncul.
Penentuan atas kode-kode apa yang harus dieksekusi disebut Penanganan Eksepsi (Exception Handling).

#### Exception Handling
Exception Handling Sebuah event yang akan menginterupsi alur proses program normal dari sebuah program. Error adalah suatu masalah yang harus diselesaikan namun error tidak harus selalu ditangani dengan exception handling (tetapi dengan exception itu akan mempermudah penanganan error).
Contoh pada exception handling di Java bekerja dengan cara mengubah alur eksekusi program, sambil melempar suatu objek tertentu sebagai informasi untuk alur yang baru
inilah yang dinamakan dengan exception atau error handling. Kode untuk Exception atau Error terdapat pada bagian CATCH. Sedangkan bila program berjalan tanpa error/pengecualian maka kode dalam TRY lah yang akan dieksekusi.
Sebetulnya banyak sekali ya exception itu, kalo pada contoh kode di atas kita menggunakan IO exception, yaitu input/ouput dalam pembacaan file (File.OpenRead). Contoh yang lain adalah:
Security Exception
Argument Exception
Argument Null Exception
Path Too Long Exception
Directory Not Found Exception
Unauthorized Access Exception
File Not Found Exception
Not Supported Exception
Untuk menghindari error kita dapat menggunakan TRY dan CATCH. Tapi perlu diingat, meski kita telah menggunakan TRY dan CATH, kita juga bisa menambahkan kode terakhir pamungkas yang disebut dengan blok ‘FINAL’,
Seperti ini model pada exception handling (contoh pada java)
Program yang tidak menggunakan exception handling:
–          Menjalankan perintah
–          Jika dalam menjalankan perintah menemui error
–          Program berhenti

Program yang menggunakan exception handling :
–          Menjalankan perintah
–          Jika dalam menjalankan perintah menemui error
–          Exception akan melemparkan error tersebut
–          Catch akan menerima dan memproses error tersebut
–          Program menjalankan perintah selanjutnya
Sehingga dengan menggunakan Exception Handling kita dapat mencegah terjadinya runtime error yang menyebabkan program kita berhenti ditengah tengah jalan.
