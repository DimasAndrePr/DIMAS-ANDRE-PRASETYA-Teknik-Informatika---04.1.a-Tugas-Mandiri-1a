# Tugas Mandiri 1A — Struktur Data

## Sistem Akademik

Repository ini berisi implementasi struktur data dalam bahasa Python berdasarkan studi kasus **Sistem Akademik**.

Program dibuat untuk menunjukkan penggunaan beberapa struktur data sesuai dengan kebutuhan pengolahan data mahasiswa, seperti penyimpanan data, fitur Undo, sistem antrean, dan pencarian berdasarkan NIM.

---

## Identitas

**Nama:** Dimas Andre Prasetya  
**NIM:** 1255011061  
**Program Studi:** Teknik Informatika  
**Mata Kuliah:** Struktur Data  
**Tugas:** Tugas Mandiri 1A

---

## Studi Kasus

Sistem akademik membutuhkan pengelolaan berbagai data mahasiswa, seperti NIM, nama, dan program studi.

Dalam sistem tersebut terdapat beberapa kebutuhan pengolahan data, antara lain:

- Penyimpanan data mahasiswa secara berurutan.
- Penambahan dan penghapusan data.
- Fitur Undo untuk membatalkan aktivitas terakhir.
- Sistem antrean pengolahan data mahasiswa.
- Pencarian data mahasiswa berdasarkan NIM.

Pemilihan struktur data dilakukan berdasarkan kebutuhan dari masing-masing operasi.

---

## Struktur Data yang Digunakan

| Kebutuhan | Struktur Data | Implementasi Python |
|---|---|---|
| Penyimpanan data mahasiswa secara berurutan | Array | `list` |
| Fitur Undo | Stack | `list` dengan `append()` dan `pop()` |
| Sistem antrean | Queue | `collections.deque` |
| Pencarian mahasiswa berdasarkan NIM | Hash Table | `dict` |

### Array

Array digunakan untuk menyimpan data mahasiswa secara berurutan dan memungkinkan akses data berdasarkan indeks.

Dalam Python, Array direpresentasikan menggunakan `list`.

### Stack

Stack digunakan untuk fitur Undo.

Operasi yang digunakan:

- `push` untuk menambahkan aktivitas.
- `pop` untuk mengambil aktivitas terakhir.

Stack menggunakan prinsip **LIFO (Last In First Out)**.

### Queue

Queue digunakan untuk mengatur antrean pengolahan data mahasiswa.

Operasi yang digunakan:

- `enqueue` untuk menambahkan data ke antrean.
- `dequeue` untuk mengambil data dari antrean.

Queue menggunakan prinsip **FIFO (First In First Out)**.

### Hash Table

Hash Table digunakan untuk pencarian data mahasiswa berdasarkan NIM.

Dalam Python, Hash Table dapat direpresentasikan menggunakan `dict`, dengan NIM sebagai `key`.

---

## Konsep Abstract Data Type (ADT)

ADT merupakan konsep yang menjelaskan data dan operasi yang dapat dilakukan tanpa bergantung pada bagaimana data tersebut diimplementasikan.

Contohnya adalah Stack ADT yang memiliki operasi `push` dan `pop`, tetapi implementasinya dapat menggunakan struktur data yang berbeda.

Pada project ini, konsep Stack dan Queue diterapkan menggunakan struktur data Python yang sesuai dengan kebutuhan program.

---

## Hubungan Struktur Data dan Algoritma

Struktur data digunakan untuk menyimpan dan mengatur data, sedangkan algoritma digunakan untuk memproses data tersebut.

Contohnya, pencarian mahasiswa berdasarkan NIM dapat dilakukan menggunakan struktur data Hash Table sehingga pencarian berdasarkan key dapat dilakukan secara efisien.

Pemilihan struktur data yang sesuai dapat memengaruhi cara kerja dan efisiensi algoritma yang digunakan.

---

## Kompleksitas Waktu

Beberapa operasi utama yang digunakan dalam program memiliki kompleksitas sebagai berikut:

| Struktur Data | Operasi | Kompleksitas |
|---|---|---|
| Array | Akses berdasarkan indeks | O(1) |
| Array | Insertion | O(1) – O(n) |
| Array | Searching | O(1) – O(n) |
| Array | Deletion | O(1) – O(n) |
| Stack | Push | O(1) |
| Stack | Pop | O(1) |
| Queue | Enqueue | O(1) |
| Queue | Dequeue | O(1) |
| Hash Table | Searching berdasarkan key | O(1) rata-rata |

Kompleksitas bergantung pada operasi yang dilakukan dan kondisi data.

---

## Implementasi Program

Program utama dibuat dalam satu file:

```text
Tugas-Mandiri-1a/
└── main.py
