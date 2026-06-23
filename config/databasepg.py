import psycopg2
from psycopg2.pool import SimpleConnectionPool
from psycopg2.extras import RealDictCursor
from contextlib import contextmanager

# 1. Konfigurasi Database PostgreSQL
# Di aplikasi produksi, bagian ini sebaiknya diambil dari file .env atau config terpusat
PG_CONFIG = {
    "dbname": "pyigniter",
    "user": "mint",
    "password": "moro",
    "host": "localhost",      # Ubah ke IP Server Cloud jika remote
    "port": "5432"
}

# 2. Inisialisasi Connection Pool (Min 1 koneksi, Max 10 koneksi terbukaa)
try:
    pg_pool = SimpleConnectionPool(1, 10, **PG_CONFIG)
except Exception as e:
    print(f"Gagal menginisialisasi PostgreSQL Connection Pool: {e}")
    pg_pool = None

@contextmanager
def pg_session():
    """
    Context manager untuk mengelola koneksi dan cursor PostgreSQL secara otomatis.
    Menggunakan RealDictCursor agar hasil fetch berbentuk dictionary.
    """
    if pg_pool is None:
        raise Exception("PostgreSQL Connection Pool tidak tersedia.")
        
    # Ambil 1 koneksi dari pool
    conn = pg_pool.getconn()
    # Gunakan RealDictCursor agar kolom otomatis menjadi key di dictionary (seperti RealDictCursor sebelumnya)
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    try:
        yield cursor
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cursor.close()
        # Kembalikan koneksi ke pool (bukan dihancurkan/close permanen), agar bisa dipakai query lain
        pg_pool.putconn(conn)
