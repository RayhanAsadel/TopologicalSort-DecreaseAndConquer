# Penyusunan Rencana Kuliah dengan Topological Sort
(Penerapan Decrease and Conquer)
> Topological Sort adalah suatu algoritma sorting yang dapat mengurutkan suatu elemen/node yang sebelumnya memiliki dependencies dan harus dikerjakan terlebih dahulu. Algoritma ini dalam kehidupan sehari-hari dapat dimisalkan seperti pengambilan prerequisite pada mata pelajaran/ mata kuliah, penjadwalan event scheduling, dan lain sebagainya.
Project ini merupakan bagian dari Tugas Kecil 2
mata kuliah Strategi Algoritma IF2121 Semester 2 2020/2021.

## Table of contents
* [Setup](#setup)
* [Features](#features)
* [Status](#status)
* [Author](#author)
* [Contact](#contact)

## Setup
Describe how to install / setup your local environement / how to run 13519196.py
* Pertama, pastikan terminal sudah terbuka pada folder src, jika sudah maka lakukan langkah-langkah berikut ini:
* Pastikan format isi dari file input txt adalah sebagai berikut.
<kode_kuliah_1>,<kode kuliah prasyarat - 1>, <kode kuliah prasyarat - 2>, <kode kuliah prasyarat - 3>.
<kode_kuliah_2>,<kode kuliah prasyarat - 1>, <kode kuliah prasyarat - 2>.
<kode_kuliah_3>,<kode kuliah prasyarat - 1>, <kode kuliah prasyarat - 2>, <kode kuliah prasyarat - 3>, <kode kuliah prasyarat - 4>.
<kode_kuliah_4>.

sebagai contoh

C1, C3.
C2, C1, C4.
C3.
C4, C1, C3.
C5, C2, C4.

Kesalahan dalam format file.txt akan membuat program tidak berjalan dengan benar.

* jika sudah memastikan format input text, maka bisa menjalankan 13519196.py dengan command:
* python 13519196.py
* masukan nama input file dengan format <namafile.txt>

## Status
Project is:  _finished_

## Author
Rayhan Asadel
13519196


