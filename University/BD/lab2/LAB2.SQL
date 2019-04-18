1. Tampilkan nama customer dan nama penerima dengan nama layanan “OKE”. /*SUKSES, CONFIRMED W/ PH*/
SELECT DISTINCT nama_customer, nama_penerima
FROM CUSTOMER C, SHIPPING S, LAYANAN L
WHERE C.id_customer = S.id_customer
AND S.id_layanan = L.id_layanan
AND L.nama_layanan = 'OKE';

2. Tampilkan nomor resi dan nama status selama tanggal 28 November 2016 sampai 1 Desember 2016 
diurutkan berdasarkan tanggal.	/*SUKSES, CONFIRMED*/
SELECT nomor_resi, nama_status
FROM TRACKING T, STATUS S 
WHERE T.date_time BETWEEN '2016-11-28' AND '2016-12-01'
AND T.id_status = S.id_status
ORDER BY T.date_time;

3. Tampilkan nomor resi, nama kota asal, nama kota tujuan, nama mitra 
untuk semua shipping. /*SUKSES, CONFIRMED*/
SELECT nomor_resi, KA.nama_kota, KT.nama_kota, nama_mitra
FROM SHIPPING S, KOTA KA, KOTA KT, MITRA M
WHERE M.id_mitra = S.id_mitra
AND S.id_kota_asal = KA.id_kota
AND S.id_kota_tujuan = KT.id_kota;

4. Tampilkan jenis barang dan nama layanan untuk semua shipping dengan 
berat 2 kg, boleh menggunakan basic query maupun nested query. /*SUKSES*/
SELECT nama_barang, nama_layanan
FROM JENIS_BARANG JB, LAYANAN L, SHIPPING S
WHERE S.berat = '2'
AND L.id_layanan = S.id_layanan
AND JB.id_barang = S.id_jenis_barang;


5. Tampilkan jenis barang dan nama layanan untuk semua shipping 
dengan jenis layanan “Oke”. Untuk soal ini, wajib menggunakan nested query.
/**SUKSES*/
SELECT nama_barang, nama_layanan
FROM JENIS_BARANG JB, LAYANAN L, SHIPPING S
WHERE S.nomor_resi IN 
(SELECT nomor_resi FROM SHIPPING S, LAYANAN L
WHERE S.id_layanan = L.id_layanan
AND L.nama_layanan = 'OKE')
AND S.id_jenis_barang = JB.id_barang
AND S.id_layanan = L.id_layanan;

SELECT DISTINCT nama_barang, nama_layanan
FROM JENIS_BARANG JB, LAYANAN L, SHIPPING S
WHERE S.nomor_resi IN 
(SELECT nomor_resi FROM SHIPPING S, LAYANAN L
WHERE S.id_layanan = L.id_layanan
AND L.nama_layanan = 'OKE')
AND S.id_jenis_barang = JB.id_barang
AND S.id_layanan = L.id_layanan;


6. Tampilkan nomor resi yang statusnya belum “delivered”.
/*SUKSES*/ BEDA
/*YG SHIPPING*/
SELECT DISTINCT SHIP.nomor_resi
FROM SHIPPING SHIP
WHERE SHIP.nomor_resi NOT IN (SELECT SHIP.nomor_resi 
FROM TRACKING T, STATUS STAT
WHERE SHIP.nomor_resi = T.nomor_resi
AND T.id_status = STAT.id_status
AND STAT.nama_status = 'Delivered');

7. Tampilkan nomor resi dan berapa kali resi tersebut diupdate statusnya 
untuk semua nomor resi yang ada di tracking diurutkan berdasarkan jumlah
update secara menurun.
/* ??? */
SELECT nomor_resi, COUNT(nomor_resi)
FROM TRACKING
WHERE nomor_resi IN (SELECT DISTINCT nomor_resi
FROM TRACKING)
GROUP BY nomor_resi
ORDER BY COUNT(nomor_resi) DESC;

8. Tampilkan nomor resi dan total yang harus dibayarkan 
(total bayar = nilai barang + tarif sesuai layanan) untuk setiap 
nomor resi yang memiliki nilai barang.
/* ??? */
SELECT nomor_resi, tarif + nilai_barang AS total_bayar
FROM TARIF_LAYANAN TL, SHIPPING S
WHERE S.nilai_barang IS NOT NULL
AND S.id_layanan = TL.id_layanan
AND S.id_kota_tujuan = TL.id_kota_tujuan
AND S.id_kota_asal = TL.id_kota_asal;

9. Tampilkan nama kota dan nama mitra yang tidak pernah digunakan 
pada saat shipping.

Nama mitra yang tidak pernah digunakan pada saat shipping
SELECT nama_mitra
FROM MITRA M
WHERE M.id_mitra NOT IN(
SELECT DISTINCT id_mitra
FROM SHIPPING);

Nama kota yang tidak pernah digunakan pada saat shipping
SELECT nama_kota
FROM KOTA
WHERE id_kota NOT IN(
SELECT id_kota_tujuan FROM SHIPPING
UNION
SELECT id_kota_asal FROM SHIPPING);


10. Tampilkan nama mitra, jenis mitra, dan berapa kali mitra tersebut 
digunakan pada saat shipping untuk semua resi dengan jumlah lebih dari 2.

SELECT nama_mitra, jenis_mitra, COUNT(nama_mitra) AS digunakan_berapa_kali
FROM SHIPPING S, MITRA M
WHERE S.id_mitra = M.id_mitra
GROUP BY nama_mitra, jenis_mitra
HAVING COUNT(S.id_mitra) > 2;


REFERENSI:
https://stackoverflow.com/questions/1945722/selecting-between-two-dates-within-a-datetime-field-sql-server
https://www.tutorialspoint.com/sql/sql-sub-queries.htm
https://stackoverflow.com/questions/141562/sql-to-find-the-number-of-distinct-values-in-a-column