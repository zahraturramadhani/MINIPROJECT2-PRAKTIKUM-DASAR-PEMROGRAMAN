# Login sederhana menggunakan Nama, Nim, dan Password
# Masukkan Nama Anda
Nama = str(input("Masukkan Nama Anda:"))

# Masukkan NIM Anda dan wajib menggunakan angka
while True:
            try:
                NIM = int(input("Masukkan NIM Anda:"))
                break  # Keluar dari loop jika NIM valid (berupa integer)
            except ValueError:
                print('=========== NIM harus berupa angka! Silahkan Input NIM Anda Kembali!!! ===========')

# Masukan Password yang terdiri dari 8 angka dan tidak boleh lebih
while True:
            try:
                Password = input('Masukkan Password Anda (8 Angka): ')
                if len(Password) != 8 or not Password.isdigit():  
                    raise ValueError
            except ValueError:
                print('===========Password yang Anda masukkan salah===========')
                print('===========Password harus terdiri dari 8 angka===========')
                continue  
            break # Keluar dari loop jika Password valid

print(f"Hello!, Selamat Datang {Nama} dengan NIM {NIM} dan password {Password}")
print("\n")  # Menambahkan Space line baru

print("===================================")
print("|PROGRAM PERHITUNGAN CUTI KARYAWAN|")
print("===================================")
print("Selamat Datang Di Aplikasi Ini!!!!!")
print("\n")

from prettytable import PrettyTable
table_karyawan = PrettyTable()
table_karyawan.field_names = ["Nama Karyawan", "Id Karyawan", "Total Cuti", "Total Cuti yang Telah Di ambil"]

table_karyawan.add_row(["Alex", 2409116001, "12", "3"])
table_karyawan.add_row(["Rani", 2409116002, "12", "0"])
table_karyawan.add_row(["Danang", 2409116003, "12", "6"])
table_karyawan.add_row(["Kintan", 2409116004, "12", "1"])
table_karyawan.add_row(["Ibnu", 2409116005, "12", "5"])

print(table_karyawan)

karyawan_list = [
    {"Nama": "Alex", "Id": 2409116001, "Total Cuti": "12", "Total Cuti Diambil": "3"},
    {"Nama": "Rani", "Id": 2409116002, "Total Cuti": "12", "Total Cuti Diambil": "0"},
    {"Nama": "Danang", "Id": 2409116003, "Total Cuti": "12", "Total Cuti Diambil": "6"},
    {"Nama": "Kintan", "Id": 2409116004, "Total Cuti": "12", "Total Cuti Diambil": "1"},
    {"Nama": "Ibnu", "Id": 2409116005, "Total Cuti": "12", "Total Cuti Diambil": "5"},
]
    
# Membuat fungsi untuk 2 mode login yaitu admin dan user
# Fungsi untuk menu admin
def admin():
    print("Anda login sebagai Admin.")
    menu_admin()

# Fungsi untuk menu user
def user():
    print("Anda login sebagai User.")
    menu_user() 

# Membuat fungsi untuk apakah anda login sebagai admin atau user
def admin_atau_user():
    while True:
        print("*************************************************")
        print("Selamat datang di perusahaan Astra International ")
        print("*************************************************")
        print("Anda sebagai Admin atau User:")
        print("[1]. Admin")
        print("[2]. User ")
        pilihan = input("Silakan Pilih Mode Login: ")
        
        if pilihan == "1":
            admin()  
            break  
        elif pilihan == "2":
            user() 
            break  
        else:
            print("Mode Login Tidak Ada, Silakan Coba Kembali!!!")


# Menu untuk mode admin
def menu_admin():
        while True:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("=================MENU ADMIN==================")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("[1]. Tambah karyawan")
            print("[2]. Lihat Daftar Karyawan")
            print("[3]. Ubah Cuti Karyawan")
            print("[4]. Hapus Karyawan")
            print("[5]. Keluar atau Kembali ke Mode Login")
            menu = input("Silakan Pilih Menu Yang Anda Inginkan:")
            if menu == "1":
                tambah_karyawan()
            elif menu == "2":
                lihat_karyawan()
            elif menu == "3":
                update_karyawan()
            elif menu == "4":
                hapus_datakaryawan()
            elif menu == "5":
                mode_login = input ("Apakah Anda ingin keluar atau kembali ke mode login? (keluar/kembali):")
                if mode_login == "keluar":
                    print("================================================================")
                    print("**********Terimakasih Telah Menggunakan Program Ini!!!**********")
                    print("================================================================")
                    exit()
                elif mode_login == "kembali":
                    admin_atau_user()
                else:
                    print("Maaf input tidak sesuai, silakan coba lagi!!!!")
            else:
                print("Maaf Menu Ini Tidak Ada, Silakan Coba Lagi")
print("\n") # Menambahkan space line

# Menambah data karyawan
def tambah_karyawan():
    while True:
        try:
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print("======================TAMBAH KARYAWAN=======================")
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

            Nama = str(input("Masukkan Nama karyawan:"))
            Id_karyawan = int(input("Masukkan Id Karyawan:"))
            total_cuti = input("Masukkan Total Cuti:")
            total_cuti_diambil = input("Masukkan total cuti yang Telah diambil:")

            Karyawan_baru = {
                "Nama": Nama,
                "Id": Id_karyawan,
                "Total Cuti": total_cuti,
                "Total Cuti Diambil": total_cuti_diambil
            }

            karyawan_list.append(Karyawan_baru)
            table_karyawan.add_row([Nama, Id_karyawan, total_cuti, total_cuti_diambil])
            print("----------------------KARYAWAN BERHASIL DITAMBAHKAN--------------------------")
            print("\n") # Menambahkan space line
            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
            print("----------------------Data karyawan setelah penambahan:-----------------------")
            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
            print(table_karyawan)
    
            pilihan = input("Apakah ingin menambahkan data karyawan lagi? (ya/tidak): ")
            if pilihan == "tidak":
                break
        except ValueError:
            print("Input Tidak Valid. Silahkan Coba Kembali!!!")


# Menampilkan daftar karyawan
def lihat_karyawan():
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print("================================DATA KARYAWAN================================")
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print(table_karyawan)

print("\n") # Menambahkan Space Line

# Memperbaharui jumlah cuti karyawan
def update_table_karyawan():
    table_karyawan.clear() 
    table_karyawan.field_names = ["Nama Karyawan", "Id Karyawan", "Total Cuti", "Total Cuti yang Telah Di ambil"] 
    for karyawan in karyawan_list:
        table_karyawan.add_row([karyawan['Nama'], karyawan['Id'], karyawan['Total Cuti'], karyawan['Total Cuti Diambil']])   


def update_karyawan():
    while True:
        lihat_karyawan()
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print("================================UPDATE KARYAWAN================================")
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

        Id_karyawan = int(input("Masukkan Id karyawan:"))
        karyawan_ditemukan = False

        for karyawan in karyawan_list:
            if karyawan['Id'] == Id_karyawan:
                karyawan_ditemukan = True
                total_cuti_diambil = int(input("Masukkan total cuti yang telah diambil yang ingin diperbarui:"))
                karyawan['Total Cuti Diambil'] = total_cuti_diambil
                print("\n") # Menambahkan space line
                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                print("-----------------------Data Karyawan Berhasil Diperbarui----------------------")
                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                print("\n")

                # Pembaruan tabel karyawan setelah perubahan
                update_table_karyawan()

        # Menampilkan tabel karyawan setelah pembaruan
        lihat_karyawan()
                
        if not karyawan_ditemukan:
            print("Maaf Id Karyawan Tidak Ditemukan")
        pilihan = input("Apakah Anda ingin memperbarui data karyawan lain? (ya/tidak) ")
        if pilihan == "tidak":
            break
print("\n") # Menambahkan space line

# Menghapus data karyawan
def hapus_datakaryawan():
    while True:
        lihat_karyawan()
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print("================================HAPUS DATA KARYAWAN================================")
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        
        try:
            Id_karyawan = int(input("Masukkan Id karyawan yang ingin dihapus:"))
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka.")
            continue
        
        karyawan_ditemukan = False
    
        for karyawan in karyawan_list:
            if karyawan['Id'] == Id_karyawan:
                karyawan_ditemukan = True
                karyawan_list.remove(karyawan) 
                print(f"Id Karyawan {Id_karyawan} dengan Nama {karyawan['Nama']} telah dihapus")

                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                print("------------------------Data karyawan setelah penghapusan-----------------------:")
                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                print("\n")
                # Pembaruan tabel karyawan setelah perubahan
                update_table_karyawan()

                # Menampilkan tabel karyawan setelah pembaruan
                lihat_karyawan()
                break
        if not karyawan_ditemukan:
            print("Id Karyawan tidak ditemukan")
                
        pilihan = input("Apakah Anda Ingin Menghapus Data Karyawan Lagi? (ya/tidak):")
        if pilihan == "tidak":
            break
print("\n") # Menambahkan space line


# Menu untuk User
def menu_user():
    while True:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("=================MENU USER==================")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("[1]. Lihat Data Diri Sendiri")
        print("[2]. Ambil Cuti Karyawan")
        print("[3]. Keluar/kembali ke mode login")
        menu = input("Silakan Pilih Menu Yang Anda Inginkan:")

        if menu == "1":
            lihat_data_diri_sendiri()
        elif menu == "2":
            ambil_cuti_karyawan()
        elif menu == "3":
                mode_login = input ("Apakah Anda ingin keluar atau kembali ke mode login? (keluar/kembali):")
                if mode_login == "keluar":
                    print("================================================================")
                    print("**********Terimakasih Telah Menggunakan Program Ini!!!**********")
                    print("================================================================")
                    exit()
                elif mode_login == "kembali":
                    admin_atau_user()
                else:
                    print("Maaf input tidak sesuai, silakan coba lagi!!!!")
        else:
            print("Pilihan Anda Tidak Valid. Silakan coba lagi!!!.")

# Melihat data diri sendiri 
def lihat_data_diri_sendiri():
    while True:
        try:
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print("================================LIHAT DATA DIRI SENDIRI================================")
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            Id_karyawan = int(input("Masukkan Id Anda:"))
            karyawan_ditemukan = False

            for karyawan in karyawan_list:
                if karyawan['Id'] == Id_karyawan:
                    karyawan_ditemukan = True
                    print("=====================================")
                    print(f"Nama Karyawan: {karyawan['Nama']}")
                    print(f"Id Karyawan: {karyawan['Id']}")
                    print(f"Total Cuti: {karyawan['Total Cuti']}")
                    print(f"Total Cuti yang Telah Diambil: {karyawan['Total Cuti Diambil']}")
                    print("=====================================")
                    break

            if not karyawan_ditemukan:
                print("Maaf, ID karyawan tidak ditemukan.")

            pilihan = input("Apakah Anda ingin lihat data anda kembali? (ya/tidak): ")
            if pilihan == "tidak":
                break
        except ValueError:
            print("Input tidak valid. Silakan masukkan ID yang benar.")

# Pengambilan Cuti Untuk User
def ambil_cuti_karyawan():
    while True:
        try:
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print("================================AMBIL CUTI================================")
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

            # Masukkan nama dan Id anda sebelum mengambil jatah cuti
            Nama_karyawan = input("Masukkan Nama Anda:")
            Id_karyawan = int(input("Masukkan Id Anda:"))
            karyawan_ditemukan = False

            for karyawan in karyawan_list:
                if karyawan['Id'] == Id_karyawan:
                    karyawan_ditemukan = True
                    jumlah_cuti = int(input("Masukkan jumlah cuti yang Anda ingin ambil:"))
                    total_cuti = int(karyawan['Total Cuti'])
                    total_cuti_diambil = int(karyawan['Total Cuti Diambil'])
                    sisa_cuti = total_cuti - total_cuti_diambil

                    if jumlah_cuti <= sisa_cuti:
                        karyawan['Total Cuti Diambil'] = str(total_cuti_diambil + jumlah_cuti) 
                        print(f"Selamat!!! {karyawan['Nama']} berhasil mengambil cuti sebanyak {jumlah_cuti} hari.")  
                        print(f"Sisa cuti Anda: {total_cuti - (total_cuti_diambil + jumlah_cuti)} hari.")
                    else:
                        print("Maaf Jumlah Cuti Yang Anda Ambil Melebihi Sisa Cuti Anda")
                    break
            
    
            if not karyawan_ditemukan: 
                print("Nama atau Id karyawan tersebut tidak ditemukan") 

            pilihan = input("Apakah Anda ingin mengambil cuti lagi? (ya/tidak): ")
            if pilihan == "tidak":        
                break   

        except ValueError:
            print("Input Tidak Valid. Silakan Coba Kembali!!!.") 

admin_atau_user()



