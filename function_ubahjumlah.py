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


#fungsi Jumlah untuk mengganti elemen dengan menambahkan input jumlah pada elemen lama lalu merubahnya pada data Gadget atau Consumable
def jumlahGeneral(gadget_consumable, IdInput, Jumlah):
    for i in range(1, len(gadget_consumable)):
        if gadget_consumable[i][0] == IdInput:
            gadget_consumable[i][3] = int(gadget_consumable[i][3]) + Jumlah

            if gadget_consumable[i][3] >= 0 and Jumlah<0 :
                print(str(Jumlah), str(gadget_consumable[i][1]), "berhasil dibuang. Stok sekarang = ", str(gadget_consumable[i][3]))
            
            elif gadget_consumable[i][3] >= 0 and Jumlah>=0 :
                print(str(Jumlah), str(gadget_consumable[i][1]), "berhasil ditambahkan. Stok sekarang = ", str(gadget_consumable[i][3]))
            
            elif gadget_consumable[i][3] <0:
                gadget_consumable[i][3] = int(gadget_consumable[i][3]) - Jumlah
                print(str(Jumlah), str(gadget_consumable[i][1]), "Gagal dibuang karena stok kurang. Stok sekarang = ", str(gadget_consumable[i][3]), "<", str(Jumlah))
    
    return gadget_consumable  





#============Fungsi Utama==============

def ubahjumlah(gadget, consumable):
    IdInput = input("Masukan ID Item : ")
    Jumlah = int(input("Masukan Jumlah : "))
    print(" ")
    if isIdValid(IdInput):
        if IdInput[0] == "G":
            if isIdAda(gadget, IdInput):
                gadget = jumlahGeneral(gadget, IdInput, Jumlah)
            else:
                print("Tidak ada Item dengan ID tersebut")
        else:
            if isIdAda(consumable, IdInput):
                consumable = jumlahGeneral(consumable, IdInput, Jumlah)
            else:
                print("Tidak ada Iitem dengan ID tersebut")
    else:
        print("Item tidak berhasil dihapus karena input ID tidak valid")
    return [gadget, consumable]


'''
tesgadget = [["id", "nama", "deskripsi", "jumlah", "rarity", "tahun ditemukan"], ["G001", "Amos", "des1", "2", "A", "2000"], ["G002", "Amber", "des2", "88", "G", "2000"], ["G002", "Krystal", "des3", "2", "A", "2010"]]
tesconsumable = [["id", "nama", "deskripsi", "jumlah", "rarity"], ["C01", "stroberry", "des1", "3", "C"]]

ubahJumlah(tesgadget, tesconsumable)
print(tesgadget)
print(tesconsumable)
'''