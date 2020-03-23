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

##### d. Apa Respon yang Didapat : 

