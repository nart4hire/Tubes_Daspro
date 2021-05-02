
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
    boolean = ["False","True"]
    for i in range (len(datas)):
        if id_peminjam == datas[i][1] and (str(datas[i][5]).capitalize()=="False" or str(datas[i][5]).capitalize() not in boolean) :
            borrowed.append(datas[i][2])
            row_gadgets.append(i)
    for i in range (len(datas)):
        idx_gadgets.append(i+1)
    return (borrowed,idx_gadgets,row_gadgets)
##################### (end) #######################

# Fungsi ini buat dapet row ke - n  di file gadget.csv dari gadget yang dipilih user 
##################### (start) #######################
def row_gadget_in_gadget_csv (datas,id_item):
    row = 0
    for i in range (len(datas)):
        if id_item == datas[i][0]:
            row = i
    return row
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

# Fungsi jumlah_gadget_borrowed, mengambil jumlah gadget yang dipinjam user [file gadget_borrow_history.cv ]
##################### (start) #######################
def jumlah_gadget_borrowed (datas,id_gadget,id_peminjam):
    jmlh_gadget = -1
    jmlh_gadget_returned = 0
    for i in range (len(datas)):
        boolean = ["True","False"]
        if id_peminjam == datas[i][1] and id_gadget == datas[i][2] and str(datas[i][5]).capitalize() == "False":
            jmlh_gadget_returned = 0
        elif id_peminjam == datas[i][1] and id_gadget == datas[i][2] and str(datas[i][5]).capitalize() not in boolean:
            jmlh_gadget_returned = datas[i][5]
    for i in range (len(datas)):
        if id_peminjam == datas[i][1] and id_gadget == datas[i][2]:
            jmlh_gadget = datas[i][4]
    return jmlh_gadget,jmlh_gadget_returned
##################### (end) #######################

# Fungsi returned_gadget, menjumlah total yang sudah pernah dikembalikan user
##################### (start) #######################
def returned_gadget (datas,id_peminjam,id_gadget,total_returned):
    total = 0
    for i in range (len(datas)):
        if id_peminjam == datas[i][1] and id_gadget == datas[i][3]:
            total += datas[i][4]
    total -= total_returned
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
    if len(gadgets_borrowed) == 0:
        print("Tidak ada gadget yang Anda pinjam")
        return [datas1,datas2,datas3]
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

    jumlah_gadget = jumlah_gadget_borrowed(datas2,id_gadget_borrowed,id_peminjam)[0] # Mendapatkan jumlah_peminjaman
    print("\nAnda sudah meminjam "+nama_gadget+" sebanyak : " + str(jumlah_gadget)) # Menampilkan jumlah_peminjaman

    total_returned = jumlah_gadget_borrowed(datas2,id_gadget_borrowed,id_peminjam)[1]
    print("Jumlah yang sudah Anda kembalikan : "+ str(total_returned)) # Menampilkan total dari jumlah_pengembalian

    sisa_gadget = jumlah_gadget - int(total_returned) # Mendapatkan jumlah gadget yang masih perlu dikembalikan oleh user
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
    jumlah_gadget_returned = jumlah_pengembalian
    ##################### (end) #######################


    # Update perubahan is_returned [file gadget_borrow_history.cv]
    ##################### (start) #######################
    row_gadgets = id_gadgets_borrowed(datas2,id_peminjam)[2] # Mendapatkan list row ke - n tiap gadget
    row_asking_gadget = row_gadgets[nomor_peminjaman-1] # Mendapatkan row ke - n dari gadget yang user minta
    boolean = ["False","True"]
    if str(datas2[row_asking_gadget][5]).capitalize() =="False":   
        if sisa_gadget - jumlah_pengembalian == 0:
            print("\nItem "+ str(nama_gadget)+ " (x" + str(jumlah_pengembalian)+") telah dikembalikan")
            print("Gadget telah dikembalikan sepenuhnya")
            datas2[row_asking_gadget][5] = True # Mengubah is_returned menjadi TRUE, karena jumlah yang dikembalikan sudah sama dengan yang dipinjam
            jumlah_pengembalian = "All"
        else:
            print("\nItem "+ str(nama_gadget)+ " (x" + str(jumlah_pengembalian)+") telah dikembalikan")
            datas2[row_asking_gadget][5] = str(jumlah_pengembalian)
    elif str(datas2[row_asking_gadget][5]).capitalize() not in boolean:
        if sisa_gadget - jumlah_pengembalian == 0:
            print("\nItem "+ str(nama_gadget)+ " (x" + str(jumlah_pengembalian)+") telah dikembalikan")
            print("Gadget telah dikembalikan sepenuhnya")
            datas2[row_asking_gadget][5] = True # Mengubah is_returned menjadi TRUE, karena jumlah yang dikembalikan sudah sama dengan yang dipinjam
            jumlah_pengembalian = "All"
        else:
            print("\nItem "+ str(nama_gadget)+ " (x" + str(jumlah_pengembalian)+") telah dikembalikan")
            datas2[row_asking_gadget][5] = str(int(datas2[row_asking_gadget][5]) + jumlah_pengembalian)
    ##################### (end) #######################
 
    # Update stok gadget
    ##################### (start) #######################
    row_in_gadget_csv = row_gadget_in_gadget_csv(datas1,id_gadget_borrowed)
    datas1[row_in_gadget_csv][3] += jumlah_gadget_returned
    ##################### (end) #######################

    # Menambahkan data baru returned [file gadget_returned_history.cv ]
    ##################### (start) #######################
    new_id_history_returned =generate_id_transaksi(datas3) # membuat id transaksi terbaru
    new_data_history_kembali = []
    tmp_new_data_history_kembali = [new_id_history_returned,id_peminjam,real_tanggal,id_gadget_borrowed,jumlah_pengembalian]
    new_data_history_kembali.append(tmp_new_data_history_kembali)
    datas3 += new_data_history_kembali
    ##################### (end) #######################
    return [datas1,datas2,datas3]
