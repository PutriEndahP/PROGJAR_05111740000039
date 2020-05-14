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
| 1 | 1 | 0.356 | 1000 | 0 | 122000 | 2810.92 | 0.356 | 334.89 |
| 2 | 10 | 0.338 | 1000 | 0 | 122000 | 2958.54 | 3.380 | 352.48 |
| 3 | 30 | 0.337 | 1000 | 0 | 122000 | 2963.47 | 10.123 | 353.07 |
| 4 | 50 | 0.337 | 1000 | 0 | 122000 | 2967.71 | 16.848 | 353.57 |
| 5 | 100 | 0.341 | 1000 | 0 | 122000 | 2933.95 | 34.084 | 349.55 |
| 6 | 500 | 0.337 | 1000 | 0 | 122000 | 2965.22 | 168.621 | 353.28 |
| 7 | 1000 | 0.336 | 1000 | 0 | 122000 | 2978.69 | 335.718 | 354.88 |

### Server_thread_http (PORT 46000)

| No Test | Currency Level | Time taken for test [seconds] | Complete request | Failed request | Total transferred [bytes] | Request per second [#/sec] {mean} | Time per request [ms] (means) | Transfer rate [Kbytes/sec] |
| :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: |
| 1 | 1 | 234.483 | 1000 | 0 | 122000 | 4.26 | 234.483 | 0.51 |
| 2 | 10 | 90.827 | 1000 | 0 | 122000 | 11.01 | 908.269 | 1.31 |
| 3 | 30 | 104.181 | 1000 | 0 | 122000 | 9.60 | 3125.437 | 1.14 |
| 4 | 50 | 102.211| 1000 | 0 | 122000 | 9.78 | 5110.539 | 1.17 |
| 5 | 100 | 107.936 | 1000 | 0 | 122000 | 9.26 | 10793.580 | 1.10 |
| 6 | 500 | 99.281 | 1000 | 0 | 122000 | 10.07 | 49640.541 | 1.20 |
| 7 | 1000 | 111.526 | 1000 | 0 | 122000 | 8.97 | 111525.567 | 1.07 |
