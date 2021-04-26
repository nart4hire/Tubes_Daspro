
# Fungsi id_gadgets_borrowed ngehasilin beberapa values
# 1. list borrowed, list gadgets yang dipinjam user. 
# Contoh borrowed = ["G002","G666"]
# 2. list idx_gadgets, kegunaanya buat membantu validasi dalam memasukan nomor peminjaman. 
# Contoh idx_gadgets = [1,2] 
# 3. list row_gadgets, kegunannya nyimpen ke row berapa tiap gadgets yang user pinjem [file gadget_borrow_history.cv]
##################### (start) #######################
def id_gadgets_borrowed (datas,id_peminjam):
    borrowed = []
    idx_gadgets = []
    row_gadgets = []
    for i in range (len(datas)):
        if id_peminjam == datas[i][1] and datas[i][5]=="FALSE":
            borrowed.append(datas[i][2])
            row_gadgets.append(i)
    for i in range (len(datas)):
        idx_gadgets.append(i+1)
    return (borrowed,idx_gadgets,row_gadgets)
##################### (end) #######################

# Fungsi nama_gadgets, mengambil nama gadget yang user pinjam [file gadget.cv ]
##################### (start) #######################
def nama_gadgets (datas,borrowed):
    list_nama_gadget = []
    for i in range (len(borrowed)):
        for j in range (len(datas)):
            if borrowed[i] == datas[j][0]:
                list_nama_gadget.append(datas[j][1])
    return list_nama_gadget
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
##################### (end) #######################

# Fungsi cnvrt_tanggal
# Contoh : 03/020/002020 -> 3/20/2020
##################### (start) #######################
def cnvrt_tanggal (tanggal):
    tmp = []
    real_tanggal = ""
    for i in  (tanggal):
        tmp.append(int(i))
    real_tanggal = real_tanggal + str(tmp[0]) + "/"+ str(tmp[1]) + "/"+ str(tmp[2])
    return (real_tanggal)
##################### (end) #######################
# Fungsi jumlah_gadget_borrowed, mengambil jumlah gadget yang dipinjam user [file gadget_borrow_history.cv ]
##################### (start) #######################
def jumlah_gadget_borrowed (datas,id_gadget,id_peminjam):
    jmlh_gadget = -1
    for i in range (len(datas)):
        if id_peminjam == datas[i][1] and id_gadget == datas[i][2]:
            jmlh_gadget = datas[i][4]
    return jmlh_gadget
##################### (end) #######################

# Fungsi returned_gadget, menjumlah total yang sudah pernah dikembalikan user
##################### (start) #######################
def returned_gadget (datas,id_peminjam,id_gadget):
    total = 0
    for i in range (len(datas)):
        if id_peminjam == datas[i][1] and id_gadget == datas[i][3]:
            total += datas[i][4]
    return total
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

# datas1 = data di gadget.cv
# datas2 = data di gadget_borrow_history.cv
# datas3 = data di gadget_returned_history.cv
# id_user = ngambil dari main program (saat proses login)
def mengembalikan_gadget (datas1,datas2,datas3,id_user):
    id_peminjam = id_user
    gadgets_borrowed = id_gadgets_borrowed(datas2,id_peminjam)[0] # id_gadget yang dipinjam user (yang dipilih is_returned = FALSE)
    list_nama_gadget = nama_gadgets(datas1,gadgets_borrowed) # list dari nama gadget yang dipinjam

    # Pengulangan untuk menampilkan gadget yang dipinjam
    for i in range (len(gadgets_borrowed)):
        print(str(i+1)+". "+ list_nama_gadget[i])

    # Validasi nomor peminjaman
    ##################### (start) #######################
    not_valid_nomor = True
    while not_valid_nomor:
        idx_gadgets = id_gadgets_borrowed(datas2,id_peminjam)[1]
        nomor_peminjaman = int(input("\nMasukan nomor peminjaman: "))
        if nomor_peminjaman not in idx_gadgets:
            print("\nNomor peminjaman tidak valid!!!")
            not_valid_nomor = True
        else:
            not_valid_nomor = False
    ##################### (end) #######################

    # Validasi tanggal pengembalian
    ##################### (start) #######################
    not_valid_tanggal = True
    while not_valid_tanggal:
        tanggal_pengembalian = input("Tanggal pengembalian: ")
        tmp_tanggal = tanggal_split(tanggal_pengembalian) # simpan sementara dalam bentuk yang sudah displit
        if valid_tanggal(tmp_tanggal) == True:
            not_valid_tanggal = False
        elif valid_tanggal(tmp_tanggal) == False:
            print("\nTanggal tidak valid!!!")
            print("Contoh input yang valid 03/04/2002\n")
            not_valid_tanggal = True
    # cnvrt tanggal menjadi format default (3/2/2020)
    raw_tanggal = tanggal_split(tanggal_pengembalian)
    real_tanggal = cnvrt_tanggal(raw_tanggal)
    ##################### (end) #######################


    id_gadget_borrowed = gadgets_borrowed[nomor_peminjaman-1] # Mendapatkan value id_gadget yang sudah dipilih oleh user
    nama_gadget = list_nama_gadget[nomor_peminjaman-1] # Mendapatkan nama gadget yang sudah dipilih oleh user

    jumlah_gadget = jumlah_gadget_borrowed(datas2,id_gadget_borrowed,id_peminjam) # Mendapatkan jumlah_peminjaman
    print("\nAnda sudah meminjam "+nama_gadget+" sebanyak : " + str(jumlah_gadget)) # Menampilkan jumlah_peminjaman

    jumlah_gadget_returned = returned_gadget(datas3,id_peminjam,id_gadget_borrowed) # Mendapatkan total dari jumlah_pengembalian
    print("Jumlah yang sudah Anda kembalikan : "+ str(jumlah_gadget_returned)) # Menampilkan total dari jumlah_pengembalian

    sisa_gadget = jumlah_gadget - jumlah_gadget_returned # Mendapatkan jumlah gadget yang masih perlu dikembalikan oleh user
    print("Sisa jumlah gadget yang perlu Anda kembalikan : " + str(sisa_gadget)+"\n")

    # Validasi jumlah pengembalian
    ##################### (start) #######################
    not_valid_jumlah = True
    while not_valid_jumlah:
        jumlah_pengembalian = int(input("Jumlah pengembalian: "))
        if jumlah_pengembalian > sisa_gadget:
            print("\nJumlah yang dikembalikan melebihi jumlah yang Anda pinjam")
            not_valid_jumlah = True
        elif jumlah_pengembalian <= 0:
            print("\nJumlah yang harus dikembalikan minimum 1")
            not_valid_jumlah = True
        else:
            not_valid_jumlah = False
    ##################### (end) #######################

    # Menambahkan data baru returned [file gadget_returned_history.cv ]
    ##################### (start) #######################
    new_id_history_returned =generate_id_transaksi(datas3) # membuat id transaksi terbaru
    new_data_history_kembali = []
    tmp_new_data_history_kembali = [new_id_history_returned,id_peminjam,real_tanggal,id_gadget_borrowed,jumlah_pengembalian]
    new_data_history_kembali.append(tmp_new_data_history_kembali)
    datas3 += new_data_history_kembali
    ##################### (end) #######################

    # Update perubahan is_returned [file gadget_borrow_history.cv]
    ##################### (start) #######################
    row_gadgets = id_gadgets_borrowed(datas2,id_peminjam)[2] # Mendapatkan list row ke - n tiap gadget
    row_asking_gadget = row_gadgets[nomor_peminjaman-1] # Mendapatkan row ke - n dari gadget yang user minta
    if sisa_gadget - jumlah_pengembalian == 0:
        print("Terimakasih sudah mengembalikan :), gadget sudah kembali sepenuhnya")
        datas2[row_asking_gadget][5] = "TRUE" # Mengubah is_returned menjadi TRUE, karena jumlah yang dikembalikan sudah sama dengan yang dipinjam
    else:
        print("Terimakasih sudah mengembalikan :)")
    ##################### (end) #######################
 