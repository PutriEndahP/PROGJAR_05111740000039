# Tugas 10

## Soal :

1. Pull update terbaru

2. Jalankan async_server.py pada port 9002, 9003, 9004, 9005 (lihat pada BackendList)

3. Jalankan file lb.py, jalankan di port 44444

4. Jalankan browser, akseslah http://localhost:44444/page.html

5. Lihatlah di log program, bahwa setiap request akan dilayani oleh backend yang bergantian

6. Lakukan performance test seperti pada tugas 9, bandingkan penggunaan load balancer dengan async_server dengan server_thread_http pada folder progjar5

7. Buatlah tabel hasilnya

### Pembahasan 

2. Jalankan async_server.py pada port 9002, 9003, 9004, 9005 (lihat pada BackendList)

![1](https://github.com/PutriEndahP/PROGJAR_05111740000039/blob/master/tugas10/screenshot/load%20balancer%20port%2044444/run_async_server.png)

3. Jalankan file lb.py, jalankan di port 44444

![2](https://github.com/PutriEndahP/PROGJAR_05111740000039/blob/master/tugas10/screenshot/load%20balancer%20port%2044444/run_lb.py.png)

4. Jalankan browser, akseslah http://localhost:44444/page.html

![3](https://github.com/PutriEndahP/PROGJAR_05111740000039/blob/master/tugas10/screenshot/load%20balancer%20port%2044444/gambar%20page.html.png)

5. Lihatlah di log program, bahwa setiap request akan dilayani oleh backend yang bergantian

![3](https://github.com/PutriEndahP/PROGJAR_05111740000039/blob/master/tugas10/screenshot/load%20balancer%20port%2044444/log%20program%20bergantian.png)

6. Lakukan performance test seperti pada tugas 9, bandingkan penggunaan load balancer dengan async_server dengan server_thread_http pada folder progjar5

#### Performance Test dengan Parameter :

| Jumlah Request | Konkurensi | 
| :-------------: | :-------------: |
| 1000 | 1, 10, 30, 50, 100, 500, 1000 | 

7. Buatlah tabel hasilnya

#### Tabel Server__async_http (PORT 45000)

| No Test | Currency Level | Time taken for test [seconds] | Complete request | Failed request | Total transferred [bytes] | Request per second [#/sec] {mean} | Time per request [ms] (means) | Transfer rate [Kbytes/sec] |
| :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: |
| 1 | 1 | 0.356 | 1000 | 0 | 122000 | 2810.92 | 0.356 | 334.89 |
| 2 | 10 | 0.338 | 1000 | 0 | 122000 | 2958.54 | 3.380 | 352.48 |
| 3 | 30 | 0.337 | 1000 | 0 | 122000 | 2963.47 | 10.123 | 353.07 |
| 4 | 50 | 0.337 | 1000 | 0 | 122000 | 2967.71 | 16.848 | 353.57 |
| 5 | 100 | 0.341 | 1000 | 0 | 122000 | 2933.95 | 34.084 | 349.55 |
| 6 | 500 | 0.337 | 1000 | 0 | 122000 | 2965.22 | 168.621 | 353.28 |
| 7 | 1000 | 0.336 | 1000 | 0 | 122000 | 2978.69 | 335.718 | 354.88 |

#### Server_thread_http (PORT 46000)

| No Test | Currency Level | Time taken for test [seconds] | Complete request | Failed request | Total transferred [bytes] | Request per second [#/sec] {mean} | Time per request [ms] (means) | Transfer rate [Kbytes/sec] |
| :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: |
| 1 | 1 | 234.483 | 1000 | 0 | 122000 | 4.26 | 234.483 | 0.51 |
| 2 | 10 | 90.827 | 1000 | 0 | 122000 | 11.01 | 908.269 | 1.31 |
| 3 | 30 | 104.181 | 1000 | 0 | 122000 | 9.60 | 3125.437 | 1.14 |
| 4 | 50 | 102.211| 1000 | 0 | 122000 | 9.78 | 5110.539 | 1.17 |
| 5 | 100 | 107.936 | 1000 | 0 | 122000 | 9.26 | 10793.580 | 1.10 |
| 6 | 500 | 99.281 | 1000 | 0 | 122000 | 10.07 | 49640.541 | 1.20 |
| 7 | 1000 | 111.526 | 1000 | 0 | 122000 | 8.97 | 111525.567 | 1.07 |

#### Load Balancer (PORT 44444)

| No Test | Currency Level | Time taken for test [seconds] | Complete request | Failed request | Total transferred [bytes] | Request per second [#/sec] {mean} | Time per request [ms] (means) | Transfer rate [Kbytes/sec] |
| :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: |

| 1 | 1 | 0.618 | 1000 | 0 | 122000 | 1617.77 | 0.618 | 192.74 |
| 2 | 10 | 0.317 | 1000 | 0 | 122000 | 3151.93 | 3.173 | 375.52 |
| 3 | 30 | 0.333 | 1000 | 0 | 122000 | 3004.74 | 9.984 | 357.99 |
| 4 | 50 | 0.326 | 1000 | 0 | 122000 | 3067.26 | 16.301 | 365.44 |
| 5 | 100 | 0.334 | 1000 | 0 | 122000 | 2996.26 | 33.375 | 356.98 |
| 6 | 500 | 0.331 | 1000 | 0 | 122000 | 3025.24 | 165.276 | 360.43 |
| 7 | 1000 | 0.331 | 1000 | 0 | 122000 | 3017.01 | 331.454 | 359.45 |
