1. Tampilkan nama penjaga kantin yang beralamat di Tebet terurut berdasarkan abjad
SELECT nama
FROM PENGGUNA
WHERE no_ktp IN (SELECT no_ktp
FROM PENJAGA_KANTIN)
AND alamat LIKE 'Jl. Tebet%';
         nama
-----------------------
 Syifa Nur Aini
 Adelia Oktavia
 Dimas Aditya Ramadhan
(3 rows)


2. Tampilkan nama counter yang mempunyai total denda lebih dari 40.000

SELECT DISTINCT denda
FROM TRANSAKSI_PEMBAYARAN_TAGIHAN 
WHERE denda > 40000

3. Tampilkan nama counter yang dimiliki owner perempuan beserta menu yang dijual oleh
counter tersebut

/* NO KTP, NAMA, JENIS KELAMIN YG CEWEK */
SELECT no_ktp, nama, jenis_kelamin
FROM PENGGUNA
WHERE jenis_kelamin = 'P'

/* NO KTP PENGGUNA CEWEK */
SELECT no_ktp
FROM PENGGUNA
WHERE jenis_kelamin = 'P'

/* NO KTP OWNER CEWEK */
SELECT O.no_ktp
FROM OWNER O
WHERE O.no_ktp IN (SELECT no_ktp
FROM PENGGUNA
WHERE jenis_kelamin = 'P')

/* ??? */
SELECT nama, id
FROM COUNTER C
WHERE C.no_ktp_owner IN (SELECT no_ktp
FROM PENGGUNA
WHERE jenis_kelamin = 'P');

/* id: 2 7 8 11 */
SELECT nama, nama_menu
FROM COUNTER C, MENU M
WHERE C.no_ktp_owner IN (SELECT O.no_ktp
						 FROM OWNER O
						 WHERE O.no_ktp IN (SELECT no_ktp
					     					FROM PENGGUNA
											WHERE jenis_kelamin = 'P'))
AND M.id_counter = C.id;
      nama      |    nama_menu
----------------+-----------------
 Ayam Mas Fu'ad | Ayam Bakar
 Ayam Mas Fu'ad | Ayam Krispi
 Ayam Mas Fu'ad | Ayam Lada Hitam
 Ayam Mas Fu'ad | Tuna Lada Hitam
 Baso           | Mie Baso
 Minuman        | Jus Alpukat
 Minuman        | Jus Apel
 Minuman        | Jus Campur
 Minuman        | Jus Jambu
 Minuman        | Jus Jeruk
(10 rows)

/* 10 rows, tp gaada yg dijual sama ayam kremes (id: 11) */




4. Tampilkan 3 nama mahasiswa yang memiliki total harga pembelian tertinggi

/*DISTINCT MAHASISWA YG ADA DI TRANSAKSI_PEMBELIAN*/
SELECT npm
FROM MAHASISWA M
WHERE npm IN (
SELECT npm_mhs
FROM TRANSAKSI_PEMBELIAN
);

SELECT SUM(total_harga) as total
FROM TRANSAKSI_PEMBELIAN WH

SELECT DISTINCT npm_mhs
FROM TRANSAKSI_PEMBELIAN;

5. Tampilkan nama menu yang tidak pernah dibeli

SELECT M.nama_menu
FROM MENU M
WHERE M.nama_menu NOT IN (SELECT MYD.nama_menu 
						  FROM MENU_YANG_DIBELI MYD);

   nama_menu
----------------
 Ayam Rica-rica
 Soto Ayam
 Soto Daging
 Soto Babat
 Nasi Uduk
 Lotek
 Karedok
 Jus Jeruk
 Jus Jambu
 Jus Apel
 Jus Campur
 Top Up 5000
 Top Up 10000
 Top Up 20000
 Top Up 50000
 Top Up 100000
(16 rows)




6. Tampilkan total biaya yang harus dikeluarkan untuk membeli semua menu yang ada di
counter Soto

SELECT SUM ()

/* NAMA MENU & HARGA DI ID 4 */
SELECT SUM(harga)
FROM MENU M, COUNTER C 
WHERE harga IN 
(
SELECT harga
FROM MENU
WHERE M.id_counter = '4'
AND M.id_counter = C.id
);

/* UDAH BENER (TOTAL HARGA 5800) */
SELECT SUM(harga)
FROM MENU M, COUNTER C
WHERE harga IN 
(
SELECT harga
FROM MENU
WHERE M.id_counter = '4'
AND M.id_counter = C.id
);

  sum
-------
 58000
(1 row)







7. Tampilkan nama penjaga kantin yang melayani transaksi pembelian lebih dari 1 kali
pada tanggal 11 Maret 2019 terurut berdasarkan abjad
8. Tampilkan npm mahasiswa yang tidak pernah melakukan transaksi top-up ke counter
9. Tampilkan nama-nama mahasiswa yang pernah membeli semua menu yang pernah
dibeli mahasiswa bernama ‘ Achmad Terry ’. Boleh menampilkan Achmad Terry nya boleh
juga tidak.
10. Tampilkan semua nama mahasiswa beserta semua menu yang pernah dibeli dari
counter bernama ‘ Ayam Mas Fu'ad ’