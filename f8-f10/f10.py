# Fungsi consum_found, mendapatkan berbagai macam value
# 1. check, mendapatkan nilai true jika id item yang dicari ada di data [ file consumable.csv]
# 2. row_consum, row ke - n dari id item yang dicari user
##################### (start) #######################
def consum_found (datas,id_item):
    check = False
    row_consum = -1
    for i in range (len(datas)):
        if id_item == datas[i][0]:
            check = True
            row_consum = i
    return (check,row_consum)
##################### (end) #######################

# Fungsi cnvrt_id_item, kegunanaanya
# Misal diinput C0000000000001 cnvrt menjadi C1
##################### (start) #######################
def cnvrt_id_item (id_item):
    tmp = []
    tmp_id = ""
    for i in id_item:
        tmp.append(i)
    for i in range (1,(len(tmp))):
        tmp_id += tmp[i]
    tmp_id = int(tmp_id)
    real_id = tmp[0]+str(tmp_id)
    return real_id
##################### (end) #######################

# Fungsi-Fungsi untuk validasi tanggal
##################### (start) #######################

# Fungsi split tanggal, buat ngebantu validasi tanggal yang diinput
def tanggal_split(s, sep='/'):
    s = s.lstrip(sep)
    if sep in s:
        pos = s.index(sep)
        found = s[:pos]
        remainder = tanggal_split(s[pos+1:])
        remainder.insert(0, found)
        return remainder
    else:
        return [s]

# Fungsi cek tahun kabisat
def kabisat (tahun):
    kabisat = False
    if (tahun % 4) == 0:
        if (tahun % 100) == 0:
            if (tahun % 400) == 0:
                kabisat = True
            else:
                kabisat = False
        else:
            kabisat = True
    else:
        kabisat = False
    return kabisat

# Fungsi cek input tanggal bener atau salah
def valid_tanggal(tanggal):
    valid = True
    if len(tanggal) != 3:
        valid = False
    else:
        bulan_31=[1,3,5,6,7,8,10,12] # ini coma list bulan ke - n yang mempunyai tanggal 31
        if int(tanggal[1])>12 or int(tanggal[1])<0: # cek validasi bulan
            valid=False
        else:
            if int(tanggal[1]) in bulan_31: # cek apakah bulan yang diinput termasuk bulan yang memiliki tanggal sampai 31
                if int(tanggal[0])<0 or int(tanggal[0])>31: # cek apakah tanggal valid
                    valid = False
            elif int(tanggal[1]) not in bulan_31 and int(tanggal[1])!=2: # cek apakah bulan yang diinput tidak termasuk bulan yang memiliki tanggal sampai 31
                if int(tanggal[0])<0 or int(tanggal[0])>30: # cek apakah tanggal valid
                    valid = False 
            elif int(tanggal[1]) == 2: # cek apakah bulan yang diinput bulan february
                if kabisat(int(tanggal[2])) == True: # cek apakah tahun kabisat
                    if int(tanggal[0])<0 or int(tanggal[0])>29: 
                        valid = False
                elif kabisat(int(tanggal[2])) == False:
                    if int(tanggal[0])<0 or int(tanggal[0])>28:
                        valid = False
    return (valid)

# Fungsi ini biar tanggal sesuai spesifikasi tugas
##################### (start) #######################
def cnvrt_tanggal (tanggal):
    tmp = []
    real_tanggal = ""
    for i in  (tanggal):
        tmp.append(int(i))
    for i in range (2):
        if tmp[i] <10:
            tmp[i] = "0" + str(tmp[i])
        else:
            tmp[i] = str(tmp[i])
    real_tanggal = real_tanggal + tmp[0] + "/"+ tmp[1] + "/"+ str(tmp[2])
    return (real_tanggal)
##################### (end) #######################

def meminta_consumable (datas):
    # Validasi id item
    ##################### (start) #######################
    not_valid_id_item = True
    while not_valid_id_item:
        id_item = input("Masukkan ID item: ")
        id_item = cnvrt_id_item(id_item)
        row_consum = consum_found(datas,id_item)[1]
        if (consum_found(datas,id_item)[0] == True):
            if datas[row_consum][3] != 0:
                not_valid_id_item = False
            elif datas[row_consum][3] == 0:
                print("\nConsumable yang Anda minta sedang kosong")
                not_valid_id_item = True
        else:
            print("\nID item yang Anda minta tidak ada")
            not_valid_id_item = True
    ##################### (end) #######################

    # Validasi jumlah
    ##################### (start) #######################    
    not_valid_jumlah = True
    while not_valid_jumlah:
        jumlah = int(input("Jumlah : "))
        if jumlah > datas[row_consum][3]:
            print("\nJumlah yang Anda minta melebihi jumlah yang tersedia")
            print("Jumlah yang tersedia : "+ str(datas[row_consum][3])+"\n")
            not_valid_jumlah = True
        elif jumlah <=0:
            print("\nMinimal jumlah yang diminta adalah 1")
            not_valid_jumlah = True
        else:
            not_valid_jumlah = False
    ##################### (end) #######################

    # Validasi tanggal
    ##################### (start) #######################
    not_valid_tanggal = True
    while not_valid_tanggal:
        tanggal_permintaan = input("Tanggal permintaan : ")
        tmp_tanggal = tanggal_split(tanggal_permintaan) # simpan sementara dalam bentuk yang sudah displit
        if valid_tanggal(tmp_tanggal) == True:
            not_valid_tanggal = False
        elif valid_tanggal(tmp_tanggal) == False:
            print("\nTanggal tidak valid!!!")
            print("Contoh input yang valid 03/04/2002\n")
            not_valid_tanggal = True
    # Ubah bentuk tanggal biar sesuai dengan spesifikasi tubes
    raw_tanggal = tanggal_split(tanggal_permintaan)
    real_tanggal = cnvrt_tanggal(raw_tanggal)
    tanggal_permintaan = real_tanggal
    ##################### (end) #######################
    nama_consum = datas[row_consum][1]
    print("\nItem "+str(nama_consum)+" (x"+str(jumlah) + ") telah berhasil diambil" )

    # Update tentang jumlah consumable tersisa
    datas[row_consum][3] -= jumlah


