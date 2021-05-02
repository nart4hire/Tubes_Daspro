# Fungsi cnvrt_id_item, kegunanaanya
# Misal diinput G0000000000001 cnvrt menjadi G1
def cnvrt_id_item (id_item):
    tmp = []
    tmp_id = ""
    for i in id_item:
        tmp.append(i)
    for i in range (1,(len(tmp))):
        tmp_id += tmp[i]
    tmp_id = int(tmp_id)
    if tmp_id < 10:
        tmp_id = "00" + str(tmp_id)
    elif 10<=tmp_id<100:
        tmp_id = "0" + str(tmp_id)
    elif tmp_id >= 100:
        tmp_id = str(tmp_id)
    real_id = tmp[0]+tmp_id
    return real_id

# Fungsi  find_id_item nyari row ke - n dari gadget yang diinput dan 
# kegunaan check buat nyari apakah gadget ada di data gadget.cv
##################### (start) #######################
def find_id_item(id_item,datas):
    tmp = -1
    check = False
    for i in range (len(datas)):
        if id_item == datas[i][0]:
            tmp = i
            check = True
    return(tmp,check)
##################### (end) #######################

# Fungsi is_returned mencari nilai is_returned pada gadget yang dicari
# Jika is_returned = True, maka gadget sudah dikembalikan
##################### (start) #######################
def is_returned(id_item,datas,id_peminjam):
    tmp = 0
    for i in range (len(datas)):
        if id_item == datas[i][2] and id_peminjam == datas[i][1]:
            tmp = i
    return datas[tmp][5]
##################### (end) #######################

# Fungsi id_item_not_in_borrow_history, nyari apakah ada gadget yg diminta
# ada di file gadget_borrow_history.cv. Gunanya buat mengetahui perlukah mengetahui nilai is_returned pada file gadget_borrow_history.cv.
# Contohnya : ketika meminjam gadget, perlu mengetahui apakah gadget sudah ada yang minjam atau belum. Dengan fungsi ini,
# bila di file gadget_borrow_history.cv belom sama sekali ada yang minjem, maka tidak perlu dijalankan fungsi is_returned
##################### (start) #######################
def id_item_not_in_borrow_history (id_item,datas):
    check = True
    for i in range (len(datas)):
        if id_item == datas[i][2]:
            check = False
    return check
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
        if int(tanggal[2]) <= 0:
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
##################### (end) #######################

# Fungsi cnvrt_tanggal
# Contoh : 3/2/002020 -> 03/02/2020
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
    if tmp[2] <10:
        tmp[2] = "000"+str(tmp[2])
    elif 10<= tmp[2] <100:
        tmp[2] = "00"+str(tmp[2])
    elif 100<= tmp[2] <1000:
        tmp[2] = "0"+str(tmp[2])
    elif tmp[2] >=1000:
        tmp[2] = str(tmp[2])
    real_tanggal = real_tanggal + tmp[0] + "/"+ tmp[1] + "/"+ tmp[2]
    return (real_tanggal)
##################### (end) #######################

# Fungsi stok_gadget
##################### (start) #######################
def stok_gadget (datas,id_item):
    stok = 0
    for i in range (len(datas)):
        if id_item == datas[i][0]:
            stok = datas[i][3]
    return stok
##################### (end) #######################

# Fungsi generate id transaksi 
##################### (start) #######################
def generate_id_transaksi (datas):
    tmp = datas[-1][0]
    tmp2 = []
    tmp_id = ""
    for i in tmp:
        tmp2.append(i)
    for i in range (1,(len(tmp2))):
        tmp_id += tmp2[i]
    tmp_id = int(tmp_id) + 1
    id_transaksi = tmp2[0]+str(tmp_id)
    return id_transaksi
##################### (end) #######################


# Fungsi meminjam gadget
##################### (start) #######################
# datas1 = data di gadget.cv
# datas2 = data di gadget_borrow_history.cv
# id_user = ngambil dari main program (saat proses login)
def meminjam_gadget(datas1,datas2,id_user):
    id_peminjam = id_user 
    # Validasi input id item
    # urutan validasinya
    # 1. gadget yang diminta ada atau tidak [file gadgdet.cv].
    # 2. Jika ada, check pernahkah user meminjam gadget di [file gadget_borrow_history.cv].
    # 3. jika ada, check apakah gadget sudah dikembalikan atau belom [file gadget_borrow_history.cv].
    # 4. jika sudah dikembalikan, maka bisa dipinjam. Kalo belom dikembalikan
    # Tidak bisa dipinjam
    ##################### (start) #######################
    not_valid_item = True
    while not_valid_item:
        id_item = input("Masukan ID item: ")
        id_item = cnvrt_id_item(id_item)
        # proses (1) start
        gadget_ada = find_id_item(id_item,datas1)[1] # ambil value true or false pada fungsi find_id_item
        if gadget_ada == False:
            print("\nGadget yang anda pinjam tidak ada")
            not_valid_item = True 
        elif gadget_ada == True:
        # proses (1) end
            # proses (2) start
            if id_item_not_in_borrow_history(id_item,datas2) == False:
                # proses (3) start
                if str(is_returned(id_item,datas2,id_peminjam)).capitalize() == "False" :
                    print("\nGadget yang Anda pilih sedang Anda pinjam, harus dikembalikan terlebih dahulu")
                    not_valid_item = True
                elif str(is_returned(id_item,datas2,id_peminjam)).capitalize() == "True":
                    if stok_gadget(datas1,id_item) == 0:
                        print("Stok gadget sedang abis")
                        not_valid_item = True
                    else:
                        not_valid_item = False
                # proses (3) end
            elif id_item_not_in_borrow_history(id_item,datas2)==True:
                if stok_gadget(datas1,id_item) == 0:
                    print("Stok gadget sedang abis")
                    not_valid_item = True
                else:
                    not_valid_item = False
            # proses (2) end
    ##################### (end) #######################

    # Validasi tanggal
    ##################### (start) #######################
    not_valid_tanggal = True
    while not_valid_tanggal:
        tanggal_peminjaman = input("Tanggal peminjaman : ")
        tmp_tanggal = tanggal_split(tanggal_peminjaman) # simpan sementara dalam bentuk yang sudah displit
        if valid_tanggal(tmp_tanggal) == True:
            not_valid_tanggal = False
        elif valid_tanggal(tmp_tanggal) == False:
            print("\nTanggal tidak valid!!!")
            print("Contoh input yang valid 03/04/2002\n")
            not_valid_tanggal = True
    # cnvrt tanggal menjadi format default (03/02/2020)
    raw_tanggal = tanggal_split(tanggal_peminjaman)
    real_tanggal = cnvrt_tanggal(raw_tanggal)
    ##################### (end) #######################

    # Validasi jumlah gadget yang dipinjam
    ##################### (start) #######################
    row_gadget = find_id_item(id_item,datas1)[0] # simpan value row ke - n yang sesuai dengan gadget yang ingin dipinjam
    not_valid_jumlah = True
    while not_valid_jumlah:
        jumlah_peminjaman = int(input("Jumlah peminjaman: "))
        if datas1[row_gadget][3] < jumlah_peminjaman:
            print("\nJumlah peminjaman melebihi jumlah yang tersedia")
            print("Jumlah yang tersedia : " + str(datas1[row_gadget][3])+"\n")
            not_valid_jumlah = True
        else:
            not_valid_jumlah = False
            print("\nItem " + str(datas1[row_gadget][1])+" (x" + str(jumlah_peminjaman) + ") berhasil dipinjam!!")
    ##################### (end) #######################
    
    # Proses memasukan data baru ke data gadget_borrow_history.cv
    ##################### (start) #######################
    new_id_history_borrow = generate_id_transaksi(datas2) # membuat id transaksi terbaru
    new_data_history_pinjam = []
    tmp_new_data_history_pinjam = [new_id_history_borrow,id_peminjam,id_item,real_tanggal,jumlah_peminjaman,"FALSE"]
    new_data_history_pinjam.append(tmp_new_data_history_pinjam)
    datas2 += new_data_history_pinjam
    ##################### (end) #######################

    # Update stok gadget
    ##################### (start) #######################
    datas1[row_gadget][3] -= jumlah_peminjaman
    ##################### (end) #######################
    
##################### (end) #######################