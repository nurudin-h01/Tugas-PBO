import sqlite3
from abc import ABC, abstractmethod

class abstrak(ABC):
 
  def tambah_akun_pembeli(self):
    pass

  def tambah_akun_petani(self):
    pass

  def login_petani(self):
    pass
  
  def login_pembeli(self):
    pass



    
    
        
databaseName = 'Produksi.db'


conn = sqlite3.connect(databaseName)
conn.execute("CREATE TABLE IF NOT EXISTS jamur (idjamur integer primary key autoincrement,namajamur text, hargabibit integer, hargajual integer, username text)")
conn.execute("CREATE TABLE IF NOT EXISTS kumbung (idkumbung integer primary key autoincrement, namakumbung text, alamatkumbung text, username text)")
conn.execute("CREATE TABLE IF NOT EXISTS penjualan (idproduksi integer primary key autoincrement, tanggal text, namakumbung text ,namajamur text, jumlah integer, username text)")
conn.execute("CREATE TABLE IF NOT EXISTS pengeluaran (idpengeluaran integer primary key autoincrement, tanggal text, namakumbung text, keterangan text, biaya text, username text)")
conn.execute("CREATE TABLE IF NOT EXISTS pengguna (idpengguna integer primary key autoincrement, role text, nama text, username text, password text)")
conn.execute("CREATE TABLE IF NOT EXISTS pemesanan (idpesan integer primary key, pembeli text, namajamur text, jumlah integer, petani text)")
databaseName1 = 'Pengeluaran.db'



class Daftar(abstrak):
  def __init__(self,username = 0, password = 0, role = 0,nama = 0):
    self.role = role
    self.nama = nama
    self.username = username
    self.password = password
  def tambah_akun_pembeli(self):
    conn.execute("select * from pengguna ")
    conn.execute("insert into pengguna(role, nama, username, password) values (?,?,?,?)", ('Pembeli',self.nama,self.username,self.password))
    conn.commit()
    print("Data Berhasil ditambah")
  def tambah_akun_petani(self):
    conn.execute("select * from pengguna ")
    conn.execute("insert into pengguna(role, nama, username, password) values (?,?,?,?)", ('Petani',self.nama,self.username,self.password))
    conn.commit()
    print("Data Berhasil ditambah")
  def login_pembeli(self):
    cursor = conn.cursor().execute("select * from pengguna where role = ? and username = ? and password =?", ("Pembeli",self.username,self.password))
    exist = cursor.fetchone()
    if exist is None:
      print("Data tidak ada")
    else:
      cursor = conn.cursor().execute("select * from pengguna where role = ? and username = ? and password =?", ("Pembeli",self.username,self.password))
      for row in cursor:
        user = row[2]
      a = Beranda()
      a.menu_pembeli(self.username,user)
  def login_petani(self):
    cursor = conn.cursor().execute("select * from pengguna where role = ? and username = ? and password =?", ("Petani",self.username,self.password))
    exist = cursor.fetchone()
    if exist is None:
      print("Data tidak ada")
    else:
      cursor = conn.cursor().execute("select * from pengguna where role = ? and username = ? and password =?", ("Petani",self.username,self.password))
      for row in cursor:
        user = row[2]
      a = Beranda()
      a.menu_petani(self.username,user)
      

class Jamur():
    def __init__(self, nama = 0, harga = 0, hargajual = 0):
        self.nama = nama
        self.harga = harga
        self.hargajual = hargajual
    def menampilkan_data(self,akun):
        cursor = conn.cursor().execute("select * from jamur where username = ?",(akun,))
        print('\n{:<15}{:<15}{:<}'.format('Nama Jamur','harga bibit','harga jual'))
        for row in cursor:
            print('\n{:<15}{:<15}{:<}'.format(row[1],row[2],row[3]))
    def menambah_data(self,akun):
        conn.execute("select * from jamur ")
        conn.execute("insert into jamur(namajamur, hargabibit, hargajual, username) values (?,?,?,?)", (self.nama,self.harga,self.hargajual,akun))
        conn.commit()
        print("Data Berhasil ditambah")
    def mengubah_data(self, akun):
        conn.execute("update jamur set hargabibit = ?, hargajual = ? where namajamur = ? and username = ?", (self.harga,self.hargajual,self.nama,akun))
        conn.commit()
        print("Data Berhasil diubah")
    def menghapus_data(self, akun):
        conn.execute("delete from jamur where namajamur = ? and username = ?", (self.nama,akun))
        conn.commit()
        print("Data Berhasil dihapus")
    
            
class Kumbung():
    def __init__(self, nama = 0, alamat = 0):
        self.nama = nama
        self.alamat = alamat
    def menampilkan_data(self, akun):
        cursor = conn.cursor().execute("select * from kumbung where username = ?",(akun,))
        print('\n{:<15}{:<}'.format('Nama Kumbung','Alamat Kumbung'))
        for row in cursor:
            print('\n{:<15}{:<}'.format(row[1],row[2]))
    def menambah_data(self,akun):
        conn.execute("select * from kumbung ")
        conn.execute("insert into kumbung(namakumbung, alamatkumbung, username) values (?,?,?)", (self.nama,self.alamat,akun))
        conn.commit()
        print("Data Berhasil ditambah")
    def mengubah_data(self, akun):
        conn.execute("update kumbung set alamatkumbung = ? where namakumbung = ? and username = ?", (self.alamat,self.nama,akun))
        conn.commit()
        print("Data Berhasil diubah")
    def menghapus_data(self, akun):
        conn.execute("delete from kumbung where namakumbung = ? and username = ? ", (self.nama,akun))
        conn.commit()
        print("Data Berhasil dihapus")
        
      

            
class Penjualan():
    def __init__(self, tanggal = 0, nama = 0, jamur = 0, jumlah = 0):
        self.tanggal = tanggal
        self.nama = nama
        self.jamur = jamur
        self.jumlah = jumlah
    def menampilkan_penjualan(self,akun):
        cursor = conn.cursor().execute("select * from penjualan where username = ?",(akun,))
        print('\n{:<20}{:<20}{:<20}{:<}'.format('tanggal','nama kumbung','nama jamur','jumlah'))
        for row in cursor:
            print('\n{:<20}{:<20}{:<20}{:<}'.format(row[1],row[2],row[3],row[4]))
    def menambahkan_penjualan(self, akun):
        conn.execute("select * from penjualan ")
        conn.execute("insert into penjualan(tanggal, namakumbung, namajamur, jumlah, username) values (?,?,?,?,?)", (self.tanggal,self.nama,self.jamur,self.jumlah,akun))
        conn.commit()
        print("Data Berhasil ditambah")
    def mengubah_penjualan(self, akun):
        conn.execute("update penjualan set namajamur = ?, jumlah = ? where tanggal = ? and namakumbung = ? and username = ?", (self.jamur,self.jumlah,self.tanggal,self.nama,akun))
        conn.commit()
        print("Data Berhasil diubah")
    def menghapus_penjualan(self,akun):
        conn.execute("delete from penjualan where tanggal = ? and namakumbung = ? and username = ?", (self.tanggal,self.nama,akun))
        conn.commit()
        print("Data Berhasil dihapus")
    def pesan(self, akun):
        cursor = conn.cursor().execute("select * from penjualan where namajamur= ?", (self.jamur,))
        exist = cursor.fetchone()
        if exist is None:
          print("Data tidak ada")
        else:
          cursor = conn.cursor().execute("select * from penjualan inner join jamur on penjualan.namajamur = jamur.namajamur and penjualan.username = jamur.username where penjualan.namajamur= ?", (self.jamur,))
          print('\n{:<15}{:<15}{:<15}{:<15}{:<15}{:<}'.format('tanggal','kumbung','nama jamur','jumlah','harga','pemilik'))
          for row in cursor:
              print('\n{:<15}{:<15}{:<15}{:<15}{:<15}{:<}'.format(row[1],row[2],row[3],row[4],row[8],row[5]))
          pilihan = str(input('Ingin memesan? (Iya/Tidak)'))
          if pilihan == "Iya":
            petani = str(input('Masukkan nama petani = '))
            jumlah = int(input('Masukkan jumlah jamur = '))
            a = Pemesanan(akun,self.jamur,jumlah,petani)
            a.menambah_data()
          
          
    
    @staticmethod
    def hasil(jumlah,jual,bibit):
      return((jumlah*jual)-(jumlah*bibit))
    
    def seleksi(self,akun):
        cursor = conn.execute("select * from penjualan inner join kumbung on penjualan.namakumbung = kumbung.namakumbung inner join jamur on penjualan.namajamur = jamur.namajamur where penjualan.tanggal like ? and penjualan.username = ?",(self.tanggal,akun))
        print('\n{:<20}{:<20}{:<20}{:<20}{:<20}{:<20}{:<}'.format('tanggal','nama kumbung','nama jamur','jumlah','alamat','harga bibit','harga jual'))
        keuntungan = 0
        for row in cursor:
           print('\n{:<20}{:<20}{:<20}{:<20}{:<20}{:<20}{:<}'.format(row[1],row[2],row[3],row[4],row[8],row[11],row[12]))
           a = Penjualan.hasil(row[4],row[12],row[11])
           keuntungan = keuntungan + a
        pengeluaran = 0
        cursor2 = conn.cursor().execute("select * from pengeluaran where tanggal like ? and username = ?",(self.tanggal,akun))
        print('\n\n')
        print('\n{:<15}{:<15}{:<20}{:<}'.format('Tanggal','Nama Kumbung','Pengeluaran','Jumlah'))
        for row in cursor2:
            pengeluaran = pengeluaran + int(row[4])
            print('\n{:<15}{:<15}{:<20}{:<}'.format(row[1],row[2],row[3],row[4]))
        total = keuntungan - pengeluaran
        print ('\nkeuntungan kotor anda sebesar', keuntungan, "\n")
        print ('\npengeluaran anda sebesar', pengeluaran, "\n")    
        if total>0:
            print ('\nkeuntungan bersih setelah dikurangi pengeluaran ', total)
        else:
            print ('\nanda mengalami kerugian sebesar ', total)

    
            
class Pengeluaran():
    def __init__(self, tanggal = 0, nama = 0, keterangan = 0, biaya = 0):
        self.tanggal = tanggal
        self.nama = nama
        self.keterangan = keterangan
        self.biaya = biaya
    def menampilkan_pengeluaran(self,akun):
        cursor = conn.cursor().execute("select * from pengeluaran where username = ?", (akun,))
        for row in cursor:
            print('\n{:<15}{:<15}{:<20}{:<}'.format('Tanggal','Nama Kumbung','Pengeluaran','Jumlah'))
            print('\n{:<15}{:<15}{:<20}{:<}'.format(row[1],row[2],row[3],row[4]))
    def menambahkan_pengeluaran(self,akun):
        conn.execute("select * from pengeluaran ")
        conn.execute("insert into pengeluaran(tanggal, namakumbung, keterangan, biaya, username) values (?,?,?,?,?)", (self.tanggal,self.nama,self.keterangan,self.biaya,akun))
        conn.commit()
        print("Data Berhasil ditambah")
    def mengubah_pengeluaran(self,akun):
        conn.execute("update pengeluaran set keterangan = ?, biaya =? where tanggal = ? and namakumbung = ? and username = ?", (self.keterangan,self.biaya,self.tanggal,self.nama,akun))
        conn.commit()
        print("Data Berhasil diubah")
    def menghapus_pengeluaran(self,akun):
        conn.execute("delete from pengeluaran where tanggal = ? and namakumbung = ? and username = ?", (self.tanggal,self.nama,akun))
        conn.commit()
        print("Data Berhasil dihapus")
    def seleksi():
        cursor = conn.execute("select * from pengeluaran where tanggal like = ?",(self.tanggal,))
        for row in cursor:
            print('\n{:<15}{:<15}{:<15}{:<}'.format(row[1],row[2],row[3],row[4]))
          
            
class Pemesanan():
    def __init__(self,pembeli = 0,jamur = 0,jumlah = 0,petani = 0):
      self.pembeli = pembeli
      self.jamur = jamur
      self.jumlah = jumlah
      self.petani = petani
    def menambah_data(self):
      conn.execute("select * from pemesanan ")
      conn.execute("insert into pemesanan(pembeli, namajamur, jumlah, petani) values (?,?,?,?)", (self.pembeli,self.jamur,self.jumlah,self.petani))
      conn.commit()
      print("Data Berhasil ditambah")
    def melihat_data(self,akun):
      cursor = conn.cursor().execute("select * from pemesanan where petani= ?", (akun,))
      exist = cursor.fetchone()
      if exist is None:
          print("Data tidak ada")
      else:
          cursor = conn.cursor().execute("select * from pemesanan where petani= ?", (akun,))
          print('\n{:<15}{:<15}{:<15}{:<}'.format('Pembeli','Nama jamur','Jumlah','Petani'))
          for row in cursor:
              print('\n{:<15}{:<15}{:<15}{:<}'.format(row[1],row[2],row[3],row[4]))
    def menghapus_data(self,akun):
      conn.execute("delete from pemesanan where petani = ?", (akun,))
      conn.commit()
      print("Data Berhasil dihapus")
          
      
      
        

class Beranda():
    def menu_utama(self):
        Ulang = True
        while Ulang == True :
          print('\n===========================================================')
          print('Selamat datang di program penjualan dan pembukuan jamur')
          print('===========================================================')
          print("Menu \n 1. Daftar \n 2. Login ")
          pilihan = int(input('Pilihan anda = '))
          if pilihan == 1:
              print('\n===========================================================')
              print('Menu Daftar')
              print('===========================================================')
              print('Pilihan Menu \n 1. Daftar sebagai pembeli \n 2. Daftar sebagai petani \n 3. Keluar')
              pilihan = int(input('Pilihan anda = '))
              if pilihan == 1:
                  nama = str(input('Masukkan nama = '))
                  username = str(input('Masukkan username = '))
                  password = str(input('Masukkan password = '))
                  a = Daftar(username, password,"Pembeli",nama)
                  a.tambah_akun_pembeli()
              elif pilihan == 2:
                  nama = str(input('Masukkan nama = '))
                  username = str(input('Masukkan username = '))
                  password = str(input('Masukkan password = '))
                  a = Daftar(username, password,"Petani",nama)
                  a.tambah_akun_petani()
              elif pilihan == 3:
                  conn.close()
                  a = Beranda()
                  a.menu_utama()
          elif pilihan == 2:
              print('\n===========================================================')
              print('Menu Login')
              print('===========================================================')
              print("Login \n 1. Login sebagai pembeli \n 2. Login sebagai petani ")
              pilihan = int(input('Pilihan anda = '))
              if pilihan == 1:
                  username = str(input('masukkan username = '))
                  password = str(input('masukkan password = '))
                  a = Daftar(username,password)
                  a.login_pembeli()
              elif pilihan == 2:
                  username = str(input('masukkan username = '))
                  password = str(input('masukkan password = '))
                  a = Daftar(username,password)
                  a.login_petani()
              elif pilihan == 3:
                  conn.close()
                  a = Beranda()
                  a.menu_utama()
                                        
                
              
        
    def menu_petani(self,akun,user):
        Ulang1 = True
        while Ulang1 == True :
            print('\n===========================================================')
            print('Selamat datang',user)
            print('===========================================================')
            akun = akun
            print("Menu \n 1. Jamur \n 2. Kumbung \n 3. Penjualan \n 4. Pengeluaran \n 5. Kotak Masuk \n 6. Keluar")
            pilihan = int(input('Pilihan anda = '))
            if pilihan == 1:
                a = Beranda()
                a.menujamur(akun,user)
            elif pilihan == 2:
                a = Beranda()
                a.menukumbung(akun,user)
            elif pilihan == 3:
                a = Beranda()
                a.menupenjualan(akun,user)
            elif pilihan == 4:
                a = Beranda()
                a.menupengeluaran(akun,user)
            elif pilihan == 5:
                a = Pemesanan()
                a.melihat_data(akun)
                pilihan = str(input("Apakah Ingin menghapus kotak masuk? (Iya/Tidak)"))
                if pilihan == 'Iya' or pilihan == 'iya':
                  a = Pemesanan()
                  a.menghapus_data(akun)
            elif pilihan == 6:
                Ulang1 = False
                a = Beranda()
                a.menu_utama()
              
   
    
            

    def menu_pembeli(self,akun,user):
          Ulang2 = True
          while Ulang2 == True :
            print('\n===========================================================')
            print('Selamat datang',user)
            print('===========================================================')
            akun = akun
            print('1. Pesan jamur \n2. Keluar')
            pilihan = int(input('masukkan pilihan = '))
            if pilihan == 1:
              pesan = str(input('Masukkan nama jamur yang ingin dipesan = '))
              a = Penjualan(0,0,pesan,0)
              a.pesan(akun)
            else:
              Ulang2 = False
              a = Beranda()
              a.menu_utama()

            
    def menujamur(self, akun, user):
        print('\n===========================================================')
        print('Selamat datang ',user,'di menu jamur')
        print('===========================================================')
        print('Pilihan Menu \n 1. Melihat data jamur \n 2. Menambah data jamur \n 3. Mengubah data jamur \n 4. Menghapus data jamur')
        pilihan = int(input('Pilihan anda = '))
        if pilihan == 1:
            a = Jamur()
            a.menampilkan_data(akun)
        elif pilihan == 2:
            nama = str(input('Masukkan nama jamur = '))
            harga = int(input('Masukkan harga bibit = '))
            hargajual = int(input('Masukkan harga jual = '))
            a = Jamur(nama,harga,hargajual)
            a.menambah_data(akun)
        elif pilihan == 3:
            nama = str(input('Masukkan nama jamur = '))
            harga = int(input('Masukkan harga bibit = '))
            hargajual = int(input('Masukkan harga jual = '))
            a = Jamur(nama,harga,hargajual)
            a.mengubah_data(akun)
        elif pilihan == 4:
            nama = str(input('Masukkan nama jamur = '))
            a = Jamur(nama)
            a.menghapus_data(akun)

    def menukumbung(self,akun,user):
        print('\n===========================================================')
        print('Selamat datang',user,'di menu kumbung')
        print('===========================================================')
        print("Menu Kumbung \n 1. Melihat Data Kumbung \n 2. Menambah Data Kumbung \n 3. Mengubah Data Kumbung \n 4. Menghapus Data Kumbung")
        pilihan = int(input('Pilihan anda = '))
        if pilihan == 1:
            a = Kumbung()
            a.menampilkan_data(akun)
        elif pilihan == 2:
            nama = str(input('Masukkan nama Kumbung = '))
            alamat = str(input('Masukkan alamat Kumbung = '))
            a = Kumbung(nama,alamat)
            a.menambah_data(akun)
        elif pilihan == 3:
            nama = str(input('Masukkan nama Kumbung = '))
            alamat = str(input('Masukkan alamat Kumbung = '))
            a = Kumbung(nama,alamat)
            a.mengubah_data(akun)
        elif pilihan == 4:
            nama = str(input('Masukkan nama Kumbung = '))
            a = Kumbung(nama)
            a.menghapus_data(akun)


    def menupenjualan(self,akun,user):
        print('\n===========================================================')
        print('Selamat datang',user,'di menu penjualan')
        print('===========================================================')
        print("Menu Penjualan \n 1. Melihat Data Penjualan \n 2. Menambah Data Penjualan \n 3. Mengubah Data Penjualan \n 4. Menghapus Data Penjualan \n 5. Keuntungan")
        pilihan = int(input('Pilihan anda = '))
        if pilihan == 1:
            a = Penjualan()
            a.menampilkan_penjualan(akun)
        elif pilihan == 2:
            tanggal = str(input('Masukkan tanggal = '))
            nama = str(input('Masukkan nama Kumbung = '))
            jamur = str(input('Masukkan nama jamur = '))
            jumlah = int(input('Masukkan jumlah jamur = '))
            a = Penjualan(tanggal,nama,jamur,jumlah)
            a.menambahkan_penjualan(akun)
        elif pilihan == 3:
            tanggal = str(input('Masukkan tanggal = '))
            nama = str(input('Masukkan nama Kumbung = '))
            jamur = str(input('Masukkan nama jamur baru = '))
            jumlah = int(input('Masukkan jumlah jamur baru = '))
            a = Penjualan(tanggal,nama,jamur,jumlah)
            a.mengubah_penjualan(akun)
        elif pilihan == 4:
            tanggal = str(input('Masukkan tanggal = '))
            nama = str(input('Masukkan nama Kumbung = '))
            a = Penjualan(tanggal,nama)
            a.menghapus_penjualan(akun)
        elif pilihan == 5:
            tanggal = str(input('Masukkan bulan-tahun = '))
            tanggal = '%' + tanggal
            a = Penjualan(tanggal)
            a.seleksi(akun)


    def menupengeluaran(self,akun,user):
        print('\n===========================================================')
        print('Selamat datang',user,'di menu pengeluaran')
        print('===========================================================')
        print("Menu Pengeluaran \n 1. Melihat Data Pengeluaran \n 2. Menambah Data Pengeluaran \n 3. Mengubah Data Pengeluaran \n 4. Menghapus Data Pengeluaran")
        pilihan = int(input('Pilihan anda = '))
        if pilihan == 1:
            a = Pengeluaran()
            a.menampilkan_pengeluaran(akun)
        elif pilihan == 2:
            tanggal = str(input('Masukkan tanggal = '))
            nama = str(input('Masukkan nama Kumbung = '))
            keterangan = str(input('Masukkan keterangan = '))
            biaya = int(input('Masukkan Jumlah Pengeluaran  = '))
            a = Pengeluaran(tanggal,nama, keterangan, biaya)
            a.menambahkan_pengeluaran(akun)
        elif pilihan == 3:
            tanggal = str(input('Masukkan tanggal = '))
            nama = str(input('Masukkan nama Kumbung = '))
            keterangan = str(input('Masukkan keterangan baru= '))
            biaya = int(input('Masukkan Jumlah Pengeluaran baru = '))
            a = Pengeluaran(tanggal,nama,keterangan, biaya)
            a.mengubah_pengeluaran(akun)
        elif pilihan == 4:
            tanggal = str(input('Masukkan tanggal = '))
            nama = str(input('Masukkan nama Kumbung = '))
            a = Pengeluaran(tanggal,nama)
            a.menghapus_pengeluaran(akun)
            
if __name__ == "__main__":
    a = Beranda()
    a.menu_utama()


            

        
            
            
            
        
    
            
            
            
        

        
            
            
            
            
        

                    
            




