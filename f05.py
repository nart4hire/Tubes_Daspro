''' Consumable.csv
id;nama;deskripsi;jumlah;rarity
C001;Enchanted Golden Apple;DON’T EAT IT;1;S
C023;Sunsettia;meh;22;B
'''
''' Gadget.csv
id;nama;deskripsi;jumlah;rarity;tahun_ditemukan
G001;Amos' Bow;bla bla;1;S;2001
G666;Amber;bla lba laaa;12;B;201 
'''



#fungsi cek validasi input Id (jenis barang yang akan ditambahkan, gadget atau consumable)
def isIdValid(Id):
    if Id[0] == "G" or Id[0]=="C":
        hasilidValid = True
    else:
        hasilidValid = False
    return hasilidValid


#fungsi cek validasi input ID (apakah sudah digunakan atau belum)
def isIdAda(gadget_consumable, Idinput):
    hasilIdAda = False
    for i in range(1, len(gadget_consumable)):
        if gadget_consumable[i][0]==Idinput:
            hasilIdAda = True
    return hasilIdAda


#fungsi cek validasi input Nama (apakah sudah digunakan atau belum)
def isNamaAda(gadget_consumable, NamaInput):
    hasilNamaAda = False
    for i in range(1, len(gadget_consumable)):
        if gadget_consumable[i][1] == NamaInput:
            hasilNamaAda = True
    return hasilNamaAda


#input deskripsi selalu benar


#fungsi cek validasi input jumlah (>0)
def isJumlahValid(JumlahInput):
    hasilJumlahValid = True
    if JumlahInput <= 0:
        hasilJumlahValid = False
    else:
        hasilJumlahValid = True
    return hasilJumlahValid


#fungsi cek validasi input rarity (C, B, A, S)
def isRarityValid(RarityInput):
    hasilRarityValid = True
    if RarityInput == "C" or RarityInput=="B" or RarityInput=="A" or RarityInput=="S":
        hasilRarityValid = True
    else:
        hasilRarityValid = False
    return hasilRarityValid


#fungsi cek validasi input tahun (>0)
def isTahunValid(TahunInput):
    hasilTahunValid = True
    if TahunInput <= 0:
        hasilTahunValid = False
    else:
        hasilTahunValid = True
    return hasilTahunValid


#=======================fungsi sub utama============================

#fungsi menambahkan item pada data Gadget jika input ID diawali huruf "G"
def tambahitemGadget (IdInput, gadget):
    nama = str(input("Masukan nama : "))                            #input nama
    if isNamaAda(gadget, nama):                                     #cek apakah ada nama yg sama
        print("Masukan tidak Valid karena Nama item sudah ada")     #YA ada nama yang sama -> gagal
    else:                                                           #TIDAK -> lanjut input
        deskripsi = str(input("Masukan Deskripsi : "))              #input deskripsi (tidak dicek)
        jumlah = int(input("Masukan Jumlah : "))                    #input Jumlah
        if isJumlahValid(jumlah):                                   #cek jumlah valid >0 ?
            rarity = str(input("Masukan Rarity : "))                #YA Jumlah valid -> input Rarity
            if isRarityValid(rarity):                               #cek rarity valid (C, B, A, S) ?
                tahun = int(input("Masukan Tahun Ditemukan : "))    #YA Rarity valid -> input tahun
                if isTahunValid(tahun):                             #cek tahun vaid >0 ?
                    arraygadget = [nama, deskripsi, jumlah, rarity, tahun]      #YA tahun valid -> buat array dari input
                    arraygadget.insert(0, IdInput)                              #tambahkan parameter IDinput di awal array baru
                    gadget = gadget.append(arraygadget)                         #append array (yang sudah digabung dgn ID) dengan data Gadget
                    print("Item berhasil ditambahkan")                          #print pesan berhasil
                else:
                    print("Gagal menambahkan item karena masukan Tahun Tidak Valid")
            else:
                print("Gagal menambahkan item karena masukan Rarity Tidak Valid")
        else:
            print("Gagal menambahkan item karena masukan jumlah tidak valid")
    return gadget



#fungsi menambah item pada data consumable jika input ID diawali "C"
def tambahitemConsumable (IdInput, consumable):
    nama = str(input("Masukan nama : "))
    if isNamaAda(consumable, nama):
        print("Masukan tidak Valid karena Nama item sudah ada")
    else:
        deskripsi = str(input("Masukan Deskripsi : "))
        jumlah = int(input("Masukan Jumlah : "))
        if isJumlahValid(jumlah):
            rarity = str(input("Masukan Rarity : "))
            if isRarityValid(rarity):
                arrayconsumable = [nama, deskripsi, jumlah, rarity]
                arrayconsumable.insert(0, IdInput)
                consumable = consumable.append(arrayconsumable)
                print("Item berhasil ditambahkan")
            else:
                print("Gagal menambahkan item karena masukan Rarity Tidak Valid")
        else:
            print("Gagal menambahkan item karena masukan jumlah tidak valid")
    return consumable



#============Fungsi Utama===============

def tambahitem(gadget, consumable):
    IdInput = input("Masukkan ID : ")
    if isIdValid(IdInput):
        if IdInput[0] == "G":
            if isIdAda(gadget, IdInput):
                print("Gagal menambahkan item karena ID sudah ada")
            else:
                gadget = tambahitemGadget(IdInput, gadget)
        else:
            if isIdAda(consumable, IdInput):
                print("Gagal menambahkan item karena ID sudah ada")
            else: 
                consumable = tambahitemConsumable(IdInput, consumable)
    else:
        print("Gagal menambahkan item")
    return[gadget, consumable]
        

   



















tesgadget = [["id", "nama", "deskripsi", "jumlah", "rarity", "tahun ditemukan"], ["G001", "Amos", "des1", "2", "A", "2000"], ["G002", "Amber", "des2", "88", "G", "2000"], ["G002", "Krystal", "des3", "2", "A", "2010"]]
tesconsumable = [["id", "nama", "deskripsi", "jumlah", "rarity"], ["C01", "stroberry", "des1", "3", "C"]]

tambahitem(tesgadget, tesconsumable)
print(tesgadget)
print(tesconsumable)