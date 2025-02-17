# capstone1

## Student Grades Management System ##

Program ini adalah sistem manajemen nilai siswa berbasis terminal yang memungkinkan pengguna untuk menambahkan, membaca, memperbarui, dan menghapus data siswa. Data yang disimpan mencakup ID siswa, nama, serta nilai mata pelajaran Matematika, Sains, dan Bahasa Inggris, dengan perhitungan nilai rata-rata otomatis.

### Fitur Utama ###

**1. Read Student Data**

- Melihat semua data siswa yang tersedia.

- Mencari siswa berdasarkan ID.

**2. Create Student Data**

- Menambahkan data siswa baru dengan validasi agar tidak ada ID duplikat.

- Memastikan nilai yang dimasukkan berada dalam rentang 0-100.

- Menghitung nilai rata-rata dari tiga mata pelajaran.

**3. Update Student Data**

- Memperbarui data siswa berdasarkan ID.

- Memungkinkan perubahan pada nama dan nilai mata pelajaran.

- Memperbarui nilai rata-rata setelah perubahan nilai.

**4. Delete Student Data**

- Menghapus data siswa berdasarkan ID.

- Konfirmasi sebelum penghapusan.

**5. Exit**

- Keluar dari program dengan pesan terima kasih.

### Struktur Kode ###

**1. show_main_menu()**

- Menampilkan menu utama dan meminta pengguna memilih opsi.

**2. create_student(students)**

- Memungkinkan pengguna menambahkan siswa baru.

- Melakukan validasi ID agar tidak ada duplikasi.

- Memastikan nilai dalam rentang 0-100.

- Menghitung nilai rata-rata sebelum menyimpan data.

- Meminta konfirmasi sebelum menyimpan.

**3. display_students(students)**

- Menampilkan daftar siswa dalam format tabel.

- Menampilkan pesan jika tidak ada data yang tersedia.

**4. read_student_menu(students)**

- Memberikan opsi untuk melihat semua data atau mencari siswa berdasarkan ID.

- Menampilkan data dalam format tabel.

**5. update_student(students)**

- Memungkinkan pengguna mengubah data siswa berdasarkan ID.

- Opsi perubahan: nama atau nilai mata pelajaran.

- Memastikan nilai yang dimasukkan valid sebelum diperbarui.

- Memperbarui nilai rata-rata setelah perubahan nilai.

**6. delete_student(students)**

- Memungkinkan pengguna menghapus siswa berdasarkan ID.

- Memastikan data yang akan dihapus benar sebelum konfirmasi.

- Memberikan pilihan untuk membatalkan penghapusan.

**7. main()**

- Fungsi utama yang menjalankan program.

- Menampilkan menu utama dan memproses pilihan pengguna hingga program dihentikan.

### Cara Menjalankan Program ###

Jalankan script Python ini menggunakan perintah:

python nama_file.py

Pilih opsi sesuai kebutuhan:

1 untuk membaca data siswa.

2 untuk menambahkan siswa baru.

3 untuk memperbarui data siswa.

4 untuk menghapus data siswa.

5 untuk keluar dari program.

Validasi & Error Handling

Memastikan ID unik saat menambahkan siswa.

Memvalidasi input angka untuk nilai mata pelajaran.

Memberikan pesan kesalahan jika pengguna memasukkan pilihan yang tidak valid.

Contoh Output

Student Grades Management System
1. Read Student Data
2. Create Student Data
3. Update Student Data
4. Delete Student Data
5. Exit
Select menu (1-5): 2

=== Show Create Data Menu (Add Data) ===
1. Add New Student
2. Exit
Select option (1-2): 1
Enter Student ID: 101
Input other data:
Enter Student Name: Alice
Enter Math Grade (0-100): 90
Enter Science Grade (0-100): 85
Enter English Grade (0-100): 88

Data to be saved:
ID: 101
Name: Alice
Math: 90
Science: 85
English: 88
Average: 87.67

Save Data? (y/n): y
Data successfully saved

Kontributor : -

Program ini dikembangkan oleh: Syahirah Putri Aisyah.
