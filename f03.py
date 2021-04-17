''' Gadget.csv
id;nama;deskripsi;jumlah;rarity;tahun_ditemukan
G001;Amos' Bow;bla bla;1;S;2001
G666;Amber;bla lba laaa;12;B;201 
'''

tesgadget = [["id", "nama", "deskripsi", "jumlah", "rarity", "tahun ditemukan"], ["G001", "Amos", "des1", "2", "A", "2000"], ["G002", "Amber", "des2", "88", "G", "2000"], ["G002", "Krystal", "des3", "2", "A", "2010"]]

def carirarity(gadget):
    rarity = input("Masukkan Rarity : ")                #asumsi input rarity selalu BENAR
    print("Hasil Pencarian : ")
    print(" ")                                          #untuk spasi baris saja biar rapi
    for i in range (1, len(gadget)):                    #loop mengecek tiap data sebanyak jumlah data
        if gadget[i][4] == rarity:                      # gadget[i][4] => mengakses matriks data gadget ke-i untuk kolom ke-4 : rarity
            print("ID : ", gadget[i][0])
            print("Nama : ", gadget[i][1])
            print("Deskripsi : ", gadget[i][2])
            print("Jumlah : ", gadget[i][3])
            print("Rarity : ", gadget[i][4])
            print("Tahun ditemukan : ", gadget[i][5])
            print(" ")                          #untuk spasi baris saja biar rapi

carirarity(tesgadget)
