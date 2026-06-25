# 🛒 Kasirhoi - High Performance Hybrid POS System

Transaksi penjualan membutuhkan aplikasi yang mendukung kecepatan, desain modern, dan performa maksimal. **Kasirhoi** hadir sebagai solusi sistem manajemen kasir dan pengelolaan stok barang (Point of Sale) berperforma tinggi yang didesain khusus agar bisnis Anda tidak pernah terganggu, bahkan saat server pusat mengalami kendala.

Aplikasi ini menggunakan arsitektur hybrid yang mengintegrasikan data secara mulus antara dua database berperforma terbaik: **SQLite** (lokal) dan **PostgreSQL** (pusat).

---

## ✨ Fitur Unggulan

### 🛡️ Arsitektur Anti-Down
* **Zero Downtime**: Transaksi tetap berjalan 100% lancar meskipun server PostgreSQL pusat mengalami gangguan dalam waktu yang lama.
* **Silent Background Sync**: Pengiriman data transaksi dilakukan secara senyap (*silent*) dan berkala untuk memastikan seluruh data sukses terunggah ke server.

### ⚖️ Integrasi Perangkat Keras
* **Koneksi Serial Timbangan**: Terintegrasi langsung dengan perangkat timbangan digital via jalur serial untuk akurasi pengukuran berat produk yang presisi.

### 📊 Manajemen Laporan Lengkap
* **Struk Kasir**: Cetak nota belanja instan untuk pelanggan.
* **X-Report**: Laporan shifts berjalan untuk pemantauan tengah hari.
* **Z-Report**: Laporan penutupan harian untuk finalisasi pembukuan keuangan.

### 🎨 Desain & Antarmuka Modern
* **UI/UX Intuitif**: Tampilan antarmuka yang modern, bersih, dan sangat mudah digunakan bahkan oleh pengguna awam sekalipun.

---

## 🏗️ Arsitektur Database

Kasirhoi menggabungkan kekuatan dua database untuk efisiensi maksimal:
1. **SQLite (Local Database)**: Menangani kecepatan baca-tulis transaksi lokal di toko secara instan tanpa hambatan jaringan.
2. **PostgreSQL (Central Database)**: Berfungsi sebagai pusat agregasi data besar, laporan multi-cabang, dan penyimpanan jangka panjang.

---

## 🚀 Memulai (Quick Start)

### Prasyarat
* Python 3.x
* PostgreSQL Server

### Instalasi Dependencies
Klona repositori ini dan instal seluruh pustaka yang diperlukan melalui file `requirements.txt`:

```bash
git clone https://github.com
cd kasirhoi
pip install -r requirements.txt
```



### Konfigurasi Database
1. Pastikan server PostgreSQL Anda sudah aktif.
2. Lakukan *dump* struktur skema awal jika diperlukan:
   ```bash
   pg_dump -U postgres -h localhost -d kasirhoi_db -s > schema.sql
   ```

![Demo Aplikasi Kasirhoi](video_image/kasirhoi_video.mp4)

---

## 💻 Lisensi & Distribusi
Aplikasi ini dikembangkan dengan proteksi keamanan jaringan tinggi serta sistem validasi tanggal lisensi otomatis via server internet (UTC).
