Pertama2 maap kalo banyak salah atau susah dibaca codenya (AUFA) .
-----------------------------------------------------
1. Fungsi yang dah dibuat bisa dicoba di test_program..
2. Pada test_program.. semua saat read dan write filenya ada _tmp diakhir
3. Pada id, ky id_user(U001),id_gadget(G001),dan semacamnya. Fungsi gw jadi tanpa
ada 00. U001 -> U1.
Alesannya diubah biar pas user mau input suatu id_item bisa banyak yang kevalid.
	Contoh : 
	id_item : U00000000000001 -> {convert} -> U1
	id_item : U00000000001234 -> {convert} -> U1234  	

4. Pada tanggal format yang gw bikin 3/2/2020, bukan 03/02/2020

5. pada f9, bisa ngembaliin cicil. Kalo sudah semua dikembalikan, pada
file gadget_borrow_history bagian is_returned berubah ke TRUE

6. pada f10, ketika sudah ngambil, jumlah akan berkurang di data file consumable 

	