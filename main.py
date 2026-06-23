# Menjalankan aplikasi
# if __name__ == "__main__":
    # import kasir_gudang
    # # Ini hanya simulasi jika dijalankan tanpa login window
    # app = kasir_gudang.KasirGudangApp("kasir1","kasir", "Slamet", None)
    # app.mainloop()

if __name__ == "__main__":
    from views.login_window import LoginWindow
    from models.sinkronisasi_model import background_sync_task,luncurkan_aplikasi_kasir

    app_login = LoginWindow(callback_sukses=luncurkan_aplikasi_kasir)        
    app_login.mainloop() 
