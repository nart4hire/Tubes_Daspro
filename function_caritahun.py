''' Gadget.csv
id;nama;deskripsi;jumlah;rarity;tahun_ditemukan
G001;Amos' Bow;bla bla;1;S;2001
G666;Amber;bla lba laaa;12;B;201 
'''

#tesgadget = [["id", "nama", "deskripsi", "jumlah", "rarity", "tahun ditemukan"], ["G001", "Amos", "des1", "2", "A", "2000"], ["G002", "Amber", "des2", "88", "G", "2000"], ["G002", "Krystal", "des3", "2", "A", "2010"]]

def caritahun(gadget):
    found=False
    tahuninput = int(input("Masukkan tahun : "))
    kategori = input("Masukkan kategori : ")
    print(" ")
    print("Hasil Pencarian : ")
    print(" ")
    if kategori == "<" :                                            
        for i in range (1, len(gadget)):
            if int(gadget[i][5]) < tahuninput:
                found=True
                print("ID : ", gadget[i][0])
                print("Nama : ", gadget[i][1])
                print("Deskripsi : ", gadget[i][2])
                print("Jumlah : ", gadget[i][3])
                print("Rarity : ", gadget[i][4])
                print("Tahun ditemukan : ", gadget[i][5])
                print(" ") 

    if kategori == ">" : 
        for i in range (1, len(gadget)):
            if int(gadget[i][5]) > tahuninput:
                found=True
                print("ID : ", gadget[i][0])
                print("Nama : ", gadget[i][1])
                print("Deskripsi : ", gadget[i][2])
                print("Jumlah : ", gadget[i][3])
                print("Rarity : ", gadget[i][4])
                print("Tahun ditemukan : ", gadget[i][5])
                print(" ") 

    if kategori == ">=" : 
        for i in range (1, len(gadget)):
            if int(gadget[i][5]) >= tahuninput:
                found=True
                print("ID : ", gadget[i][0])
                print("Nama : ", gadget[i][1])
                print("Deskripsi : ", gadget[i][2])
                print("Jumlah : ", gadget[i][3])
                print("Rarity : ", gadget[i][4])
                print("Tahun ditemukan : ", gadget[i][5])
                print(" ") 

    if kategori == "<=" : 
        for i in range (1, len(gadget)):
            if int(gadget[i][5]) <= tahuninput:
                found=True
                print("ID : ", gadget[i][0])
                print("Nama : ", gadget[i][1])
                print("Deskripsi : ", gadget[i][2])
                print("Jumlah : ", gadget[i][3])
                print("Rarity : ", gadget[i][4])
                print("Tahun ditemukan : ", gadget[i][5])
                print(" ")    

    if kategori == "=" : 
        for i in range (1, len(gadget)):
            if int(gadget[i][5]) == tahuninput:
                found=True
                print("ID : ", gadget[i][0])
                print("Nama : ", gadget[i][1])
                print("Deskripsi : ", gadget[i][2])
                print("Jumlah : ", gadget[i][3])
                print("Rarity : ", gadget[i][4])
                print("Tahun ditemukan : ", gadget[i][5])
                print(" ") 

    if found==False:                                                                    #kondisi jika fungsi isTahunAda == False (tidak ada data dengan tahun ditemukan = tahun input), maka program hanya menampilkan pesan "tidak ada"                                                  
        print("Tidak ada gadget yang ditemukan")



#caritahun(tesgadget)                                                          #test untuk coder