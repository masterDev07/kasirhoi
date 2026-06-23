import sqlite3
from pathlib import Path
from contextlib import contextmanager


"""
from pathlib import Path
from contextlib import contextmanager
# 1. Ganti import sqlite3 menjadi pysqlcipher3
from pysqlcipher3 import dbapi2 as sqlite

db_sqlite="pos_lokal.db"
# 2. Naik satu level ke root proyek, lalu arahkan ke file database
DB_PATH = CONFIG_DIR.parent / f"{db_sqlite}"

# 2. Tentukan kunci enkripsi database Anda
# Catatan: Di aplikasi produksi, simpan sandi ini di file .env atau config terenkripsi!
DB_KEY = "SandiRahasiaKasirAnda123!"

@contextmanager
def db_session():
    #Context manager untuk mengelola koneksi SQLCipher secara otomatis.
    # 3. Hubungkan menggunakan modul sqlite dari pysqlcipher3
    conn = sqlite.connect(str(DB_PATH), timeout=20)
    
    # 4. WAJIB: Jalankan perintah PRAGMA key tepat setelah koneksi terbuka
    conn.execute(f"PRAGMA key = '{DB_KEY}';")
    
    conn.row_factory = sqlite.Row
    cursor = conn.cursor()
    try:
        yield cursor
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cursor.close()
        conn.close()
        
        
# TAMBAHAN
@contextmanager
def db_session():
    # 1. Buka koneksi database
    conn = sqlite3.connect(DB_PATH, timeout=20)
    
    # 2. Atur row_factory TEPAT setelah koneksi terbuka (Sebelum membuat kursor)
    conn.row_factory = sqlite3.Row
    
    # 3. Baru buat kursornya
    cursor = conn.cursor()
    
    # 4. Jalankan optimasi kecepatan WAL melalui kursor
    cursor.execute("PRAGMA journal_mode=WAL;")
    cursor.execute("PRAGMA synchronous=NORMAL;")
    
    # Lanjutkan dengan blok try-except-yield seperti biasa...

"""


# 1. Cari lokasi folder 'config/' saat ini
CONFIG_DIR = Path(__file__).resolve().parent

db_sqlite="pos_lokal.db"
# 2. Naik satu level ke root proyek, lalu arahkan ke file database
DB_PATH = CONFIG_DIR.parent / f"{db_sqlite}"

@contextmanager
def db_session():
    """Context manager untuk mengelola koneksi SQLite secara otomatis."""
    # Menambahkan timeout agar mengurangi risiko 'database is locked' saat skala besar
    conn = sqlite3.connect(str(DB_PATH), timeout=20)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    try:
        yield cursor
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cursor.close()
        conn.close()


def execute_query(DB_PATH, query, params=(), fetchone=False):
    conn = sqlite3.connect(str(DB_PATH), timeout=20)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    try:
        cursor.execute(query, params)
        if fetchone:
            return cursor.fetchone()
        return cursor.fetchall()
    finally:
        conn.close() # Menjamin koneksi tertutup meski ada error


def execute_update(DB_PATH, query, params=()):
    conn = sqlite3.connect(DB_PATH, timeout=20)
    cursor = conn.cursor()
    try:
        cursor.execute(query, params)
        conn.commit() # Simpan perubahan
        return cursor.rowcount # Mengembalikan jumlah baris yang berubah
    finally:
        conn.close()
