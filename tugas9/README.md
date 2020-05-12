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
| 1 | 1 | 5.636 | 1000 | 0 | 122000 | 177.44 | 5.636 | 21.14 |
| 2 | 10 | 13.491 | 1000 | 0 | 122000 | 74.12 | 134.911 | 8.83 |
| 3 | 30 | 4.590 | 1000 | 0 | 122000 | 217.88 | 137.691 | 25.96 |
| 4 | 50 | 7.609 | 1000 | 0 | 122000 | 131.42 | 380.466 | 15.66 |
| 5 | 100 | 4.643 | 1000 | 0 | 122000 | 215.37 | 464.327 | 25.66 |
| 6 | 500 | 0.468 | 1000 | 121 | 15372 | 2138.17 | 233.845 | 32.10 |
| 7 | 1000 | 1.762 | 1000 | 425 | 51850 | 576.40 | 1762.410 | 28.73 |

### Server_thread_http (PORT 46000)

| No Test | Currency Level | Time taken for test [seconds] | Complete request | Failed request | Total transferred [bytes] | Request per second [#/sec] {mean} | Time per request [ms] (means) | Transfer rate [Kbytes/sec] |
| :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: |
| 1 | 1 | 1305.479 | 1000 | 0 | 122000 | 0.77 | 1305.479 | 0.09 |
| 2 | 10 | 1009.472 | 1000 | 0 | 122000 | 0.99 | 10094.723 | 0.12 |
| 3 | 30 | 909.832 | 1000 | 0 | 122000 | 1.10 | 27294.966 | 0.13 |
| 4 | 50 | 882.385 | 1000 | 0 | 122000 | 1.13 | 44119.229 | 0.14 |
| 5 | 100 | 1105.757 | 1000 | 0 | 122000 | 0.90 | 110575.702 | 0.11 |
| 6 | 500 | 28.436 | 1000 | 299 | 36478 | 35.17 | 14217.987 | 1.25 |
| 7 | 1000 | 146.968 | 1000 | 539 | 65758 | 6.80 | 146968.344 | 0.44 |
