# Tugas 4

## Soal Tugas 4 :
![1](https://github.com/PutriEndahP/PROGJAR_05111740000039/blob/master/tugas4/soal%20tugas%204.jpeg)

### Dokumentasi Protocol

#### Buatlah Dokumentasi dari Protocol tersebut, berisikan :

##### a. Ketentuan Membaca Format: 


##### b. Daftar Fitur:

  Terdapat tiga fitur di protocol ini, yaitu :
  
  * GET : Fitur yang digunakan untuk mengambil file.
  
  * PUT : Fitur yang digunakan untuk meletakkan file.
  
  * LS : Fitur yang digunakan untuk melihat list file dalam directory.

##### c. Cara Melakukan Request :

  Request dilakukan oleh client, dengan meng-inputkan string yang diminta. Request tersebut selanjutnya akan diterima oleh server dan     akan di proses lebih lanjut.
  
  Berikut ini merupakan source code dari client untuk memasukkan input :
  
  ```
    cmd = input(""+str("ftp@ ") + str(cur_dir) + " > ")
    s.send(createJSON('ok', cmd))
    s_cmd = cmd.split(" ")
    cm = s_cmd[0]

    try:
        fname = s_cmd[1]
    except:
        fname = ""
  ```
  Berikut penjelasannya :
  
  ``` cmd = input(""+str("ftp@ ") + str(cur_dir) + " > ") ``` Digunakan untuk menampilkan input di terminal.
  
  ``` s.send(createJSON('ok', cmd)) ``` Digunakan untuk mengirimkan string input sesuai dengan command yang dituliskan.
  
  ```  s_cmd = cmd.split(" ") ``` Digunakan untuk memecah string inputnya.
  
  ```  cm = s_cmd[0] ``` Untuk mendapatkan command inputnya.
  
  Request untuk mendapatkan list data :
  
  ``` 
    if cm == "ls":
        data= getRecv(s, 102400)

        for i in data['files']:
            size= i['size'] / 1000
            size= str(size)
            print(str(i['name'])+"\t\t"+size+" Kb")
  ```
  
  Command ls digunakan untuk mendapat list file dalam suatu directory. Kemudian client akan mendapatkan response dari server yang akan     dimasukkan ke variabel bernama data. Selanjutnya akan dilakukan looping data dari client. Ukuran datanya akan dirubah ke Kb dengan       dibagi 1000. Kemudian hasil akan di print. 
  
  Request untuk mendapat file :
  
  ```
    if cm == "get":
        if fname == ".":
            ssize = getRecv(s, 1024)
            s.send(createJSON('ok', 'ready to download'))
            for i in range(int(ssize)):
                fff_name = getRecv(s, 1024)
                s.send(createJSON('ok', 'ready to download'))
                with open(fff_name, 'wb') as f:
                    data = s.recv(1024)
                    while True:
                        f.write(data)
                        s.send(createJSON('ok', 'got part of file'))
                        data = s.recv(1024)
                        if data.decode("utf-8") == "$end$":
                            print(fff_name+" has been downloaded")
                            break
        else:
            should_try = getRecv(s, 1024)
            if should_try == "$present$":
                s.send(createJSON('ok', 'ok'))
                with open(fname, 'wb') as f:
                    data = s.recv(1024)
                    while True:
                        f.write(data)
                        s.send(createJSON('ok', 'got part of file'))
                        data = s.recv(1024)
                        if data.decode("utf-8") == "$end$":
                            print(fname+" has been downloaded")
                            break
            else:
                print(should_try)
  ```
  
  Command get untuk mendapatkan file dari suatu directory. Untuk mendapatkan semua file dalam sebuah directory bisa menggunakan command   ``` get [.] ```. Tapi jika ingin mendapatkan satu file saja dalam suatu directory menggunakan command ``` get [namafile] ```. Kemudian    server akan mengirimkan request dan client akan mencetak file yang diminta.
  
  Request untuk meletakkan file :
  
  ```
  if cm == "put":
        if fname == ".":
            path = os.getcwd()
            all_files = [f for f in os.listdir(path)
                         if os.path.isfile(os.path.join(path, f))]
            ssize = len(all_files)
            s.send(createJSON('ok', ssize))
            n = getRecv(s, 1024)
            for a_file in all_files:
                s.send(createJSON('ok', a_file))
                n = getRecv(s, 1024)
                with open(str(a_file), "rb") as f:
                    l = f.read(1024)
                    while (l):
                        s.send(l)
                        n = getRecv(s, 1024)
                        l = f.read(1024)
                    s.send(str.encode("$end$"))
                print(str(a_file)+' was uploaded to server')
        else:
            if fname == "":
                s.send(createJSON('ok', 'notOk'))
                print("provide a filename")
            elif os.path.exists(fname):
                s.send(createJSON('ok', 'ok'))
                cur_path = os.getcwd()
                n = getRecv(s, 1024)
                with open(str(fname), "rb") as f:
                    l = f.read(1024)
                    while (l):
                        s.send(l)
                        n = getRecv(s, 1024)
                        l = f.read(1024)
                    s.send(str.encode("$end$"))
                print(str(fname)+' was uploaded to server')
            else:
                s.send(createJSON('ok', 'notOk'))
                print("No Such file ", fname)
  ```
  
  Command put digunakan untuk meletakkan file ke suatu directory. Dengan command ``` put [filename] ``` maka server akan memproses         permintaan client dan meletakkan file tertentu yang sudah dipilih. Sedangkan jika tidak ada file yang akan di letakkan maka client       akan mencetak pesan bahwa tidak ada file atau " No Such File ".

##### d. Apa Respon yang Didapat : 




