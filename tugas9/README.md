# Tugas 9

## Soal :

1. Pull update terakhir

2. Jalankan kedua model tersebut

    - Server_async_http.py di port 45000

    - Server_thread_http.py di port 46000

3. Ujicobalah dengan apache benchmark untuk 1000 request dan konkurensi yang bervariasi

4. Buatlah tabel untuk melaporkan hasilnya

### Dengan Parameter :

| Jumlah Request | Konkurensi | 
| :-------------: | :-------------: |
| 1000 | 1, 10, 30, 50, 100, 500, 1000 | 

### Server_async_http (PORT 45000)

| No Test | Currency Level | Time taken for test [seconds] | Complete request | Failed request | Total transferred [bytes] | Request per second [#/sec] {mean} | Time per request [ms] (means) | Transfer rate [Kbytes/sec] |
| :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: |
| 1 | 1 | 155.786 | 1000 | 0 | 122000 | 6.42 | 155.786 | 0.76 |
| 1 | 1 | 155.786 | 1000 | 0 | 122000 | 6.42 | 155.786 | 0.76 |

