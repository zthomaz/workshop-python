# Thomas Prayudhi
# Minggu ke tujuh

## 	OOP di Python

### Kelas
Kelas menyediakan sarana untuk menggabungkan data dan fungsi bersama. Membuat kelas baru menciptakan jenis objek baru, yang memungkinkan instance baru dari jenis itu dibuat. Setiap instance kelas dapat memiliki atribut yang melekat padanya untuk mempertahankan statusnya. Instance kelas juga dapat memiliki metode (ditentukan oleh kelasnya) untuk memodifikasi statusnya.

Dibandingkan dengan bahasa pemrograman lainnya, mekanisme kelas Python menambahkan kelas dengan minimal sintaks dan semantik baru. Ini adalah campuran dari mekanisme kelas yang ditemukan di C ++ dan Modula-3. Kelas Python menyediakan semua fitur standar Pemrograman Berorientasi Objek: mekanisme pewarisan kelas memungkinkan beberapa kelas dasar, kelas turunan dapat mengesampingkan metode apa pun dari kelas dasar atau kelasnya, dan metode dapat memanggil metode kelas dasar dengan nama yang sama . Objek dapat berisi jumlah dan jenis data yang sewenang-wenang. Seperti benar untuk modul, kelas mengambil bagian dari sifat dinamis Python: mereka dibuat saat runtime, dan dapat dimodifikasi lebih lanjut setelah pembuatan.

Dalam terminologi C ++, biasanya anggota kelas (termasuk anggota data) bersifat publik (kecuali lihat di bawah Variabel Pribadi), dan semua fungsi anggota adalah virtual. Seperti dalam Modula-3, tidak ada singkatan untuk mereferensikan anggota objek dari metodenya: fungsi metode dideklarasikan dengan argumen pertama eksplisit yang mewakili objek, yang diberikan secara implisit oleh panggilan. Seperti dalam Smalltalk, kelas itu sendiri adalah objek. Ini menyediakan semantik untuk mengimpor dan mengganti nama. Tidak seperti C ++ dan Modula-3, tipe built-in dapat digunakan sebagai kelas dasar untuk ekstensi oleh pengguna. Juga, seperti di C ++, sebagian besar operator built-in dengan sintaks khusus (operator aritmatika, subscripting, dll.) Dapat didefinisikan ulang untuk instance kelas.

(Kurang terminologi yang diterima secara universal untuk berbicara tentang kelas, saya akan menggunakan istilah Smalltalk dan C ++ sesekali. Saya akan menggunakan istilah Modula-3, karena semantik berorientasi objeknya lebih dekat dengan Python daripada C ++, tapi saya berharap bahwa beberapa pembaca telah mendengarnya.)

### Nama dan Obyek
Objek memiliki individualitas, dan beberapa nama (dalam berbagai cakupan) dapat terikat ke objek yang sama. Ini dikenal sebagai aliasing dalam bahasa lain. Ini biasanya tidak dihargai pada pandangan pertama Python, dan dapat dengan aman diabaikan ketika berhadapan dengan tipe dasar yang tidak dapat diubah (angka, string, tupel). Namun, aliasing memiliki efek yang mungkin mengejutkan pada semantik kode Python yang melibatkan objek yang dapat berubah seperti daftar, kamus, dan sebagian besar jenis lainnya. Ini biasanya digunakan untuk kepentingan program, karena alias bertindak seperti pointer dalam beberapa hal. Sebagai contoh, melewati suatu objek adalah murah karena hanya pointer yang dilewatkan oleh implementasi; dan jika fungsi memodifikasi objek yang dilewatkan sebagai argumen, pemanggil akan melihat perubahan - ini menghilangkan kebutuhan untuk dua mekanisme pengalihan argumen yang berbeda seperti dalam Pascal.

#### Lingkup Python dan Namespaces
Sebelum memperkenalkan kelas, pertama-tama saya harus memberi tahu Anda sesuatu tentang aturan lingkup Python. Definisi kelas memainkan beberapa trik rapi dengan ruang nama, dan Anda perlu mengetahui ruang lingkup dan ruang nama berfungsi untuk memahami apa yang sebenarnya terjadi. Kebetulan, pengetahuan tentang subjek ini berguna untuk programmer Python maju.

Mari mulai dengan beberapa definisi.

Namespace adalah pemetaan dari nama ke objek. Kebanyakan ruang nama saat ini diterapkan sebagai kamus Python, tetapi itu biasanya tidak terlihat dengan cara apa pun (kecuali untuk kinerja), dan mungkin akan berubah di masa mendatang. Contoh ruang nama adalah: kumpulan nama bawaan (berisi fungsi seperti abs (), dan nama pengecualian bawaan); nama-nama global dalam sebuah modul; dan nama-nama lokal dalam doa fungsi. Dalam arti set atribut suatu objek juga membentuk namespace. Yang penting untuk diketahui tentang ruang nama adalah bahwa sama sekali tidak ada hubungan antara nama di ruang nama yang berbeda; misalnya, dua modul yang berbeda dapat mendefinisikan fungsi yang dimaksimalkan tanpa kebingungan - pengguna modul harus menambahkannya dengan nama modul.

By the way, saya menggunakan atribut kata untuk setiap nama mengikuti titik - misalnya, dalam ekspresi z.real, nyata adalah atribut dari objek z. Secara tegas, referensi untuk nama dalam modul adalah referensi atribut: dalam ekspresi modname.funcname, modname adalah objek modul dan funcname adalah atributnya. Dalam hal ini terjadi pemetaan langsung antara atribut modul dan nama global yang didefinisikan dalam modul: mereka berbagi namespace yang sama! [1]

Atribut dapat bersifat hanya-baca atau dapat ditulis. Dalam kasus terakhir, penugasan ke atribut dimungkinkan. Atribut modul dapat ditulis: Anda dapat menulis modname.the_answer = 42. Atribut yang dapat dihapus juga dapat dihapus dengan pernyataan del. Sebagai contoh, del modname.the_answer akan menghapus atribut the_answer dari objek yang dinamai oleh modname.

Namespaces dibuat pada momen yang berbeda dan memiliki masa kehidupan yang berbeda. Namespace yang berisi nama built-in dibuat ketika interpreter Python dijalankan, dan tidak pernah dihapus. Namespace global untuk modul dibuat ketika definisi modul dibaca; biasanya, ruang nama modul juga bertahan sampai juru bahasa berhenti. Pernyataan yang dieksekusi oleh permintaan tingkat tinggi dari penerjemah, baik dibaca dari file skrip atau secara interaktif, dianggap sebagai bagian dari modul yang disebut __main__, sehingga mereka memiliki namespace global sendiri. (Nama bawaan sebenarnya juga ada dalam modul; ini disebut builtins.)

Namespace lokal untuk fungsi dibuat ketika fungsi dipanggil, dan dihapus ketika fungsi mengembalikan atau memunculkan eksepsi yang tidak ditangani dalam fungsi. (Sebenarnya, melupakan akan menjadi cara yang lebih baik untuk menggambarkan apa yang sebenarnya terjadi.) Tentu saja, rekursif panggilan masing-masing memiliki namespace lokal mereka sendiri.

Lingkup adalah wilayah tekstual program Python di mana namespace dapat diakses secara langsung. "Langsung dapat diakses" di sini berarti bahwa referensi yang tidak memenuhi syarat untuk nama berusaha untuk menemukan nama di ruang nama.

Meskipun ruang lingkup ditentukan secara statis, cakupannya digunakan secara dinamis. Kapan saja selama eksekusi, setidaknya ada tiga lingkup bersarang yang namespace-nya dapat diakses secara langsung:

ruang lingkup paling dalam, yang dicari pertama kali, berisi nama-nama lokal
lingkup dari setiap fungsi melampirkan, yang dicari dimulai dengan lingkup melampirkan terdekat, mengandung non-lokal, tetapi juga nama-nama non-global
cakupan berikutnya-ke-akhir berisi nama global modul saat ini
ruang lingkup terluar (dicari terakhir) adalah namespace yang berisi nama-nama bawaan
Jika nama dideklarasikan secara global, semua referensi dan tugas akan langsung masuk ke ruang tengah yang berisi nama global modul. Untuk variabel rebind ditemukan di luar ruang lingkup paling dalam, pernyataan nonlokal dapat digunakan; jika tidak dideklarasikan nonlocal, variabel-variabel tersebut bersifat read-only (sebuah upaya untuk menulis ke variabel tersebut hanya akan membuat variabel lokal baru dalam ruang lingkup paling dalam, meninggalkan variabel luar yang bernama identik tidak berubah).

Biasanya, lingkup lokal referensi nama-nama lokal dari fungsi (tekstual) saat ini. Di luar fungsi, lingkup lokal merujuk pada ruangnama yang sama dengan lingkup global: ruang nama modul. Definisi kelas menempatkan namespace lain di lingkup lokal.

Penting untuk menyadari bahwa lingkup ditentukan secara tekstual: ruang lingkup global dari fungsi yang didefinisikan dalam modul adalah ruang nama modul, tidak peduli dari mana atau oleh apa alias fungsi tersebut dipanggil. Di sisi lain, pencarian nama yang sebenarnya dilakukan secara dinamis, pada saat dijalankan - namun, definisi bahasa berkembang ke resolusi nama statis, pada waktu "kompilasi", jadi jangan bergantung pada resolusi nama dinamis! (Faktanya, variabel lokal sudah ditentukan secara statis.)

Sebuah quirk khusus dari Python adalah bahwa - jika tidak ada pernyataan global yang berlaku - tugas untuk nama selalu masuk ke ruang lingkup terdalam. Tugas tidak menyalin data - mereka hanya mengikat nama ke objek. Hal yang sama berlaku untuk penghapusan: pernyataan del x menghapus pengikatan x dari namespace yang direferensikan oleh lingkup lokal. Bahkan, semua operasi yang memperkenalkan nama-nama baru menggunakan lingkup lokal: khususnya, pernyataan impor dan definisi fungsi mengikat modul atau nama fungsi dalam lingkup lokal.

Pernyataan global dapat digunakan untuk menunjukkan bahwa variabel tertentu hidup dalam lingkup global dan harus rebound di sana; pernyataan nonlokal menunjukkan bahwa variabel tertentu hidup dalam lingkup melampirkan dan harus rebound di sana.