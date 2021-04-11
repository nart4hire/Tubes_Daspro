
# Fungsi split ngambil dari google :v
##################### (start) #######################
def my_split(s, sep=" "):
    s = s.lstrip(sep)
    if sep in s:
        pos = s.index(sep)
        found = s[:pos]
        remainder = my_split(s[pos+1:])
        remainder.insert(0, found)
        return remainder
    else:
        return [s]
##################### (end) #######################

# Fungsi ubah nama biar kapital di awal kata
##################### (start) #######################
def real_nama (tmp_nama):
    splited_nama = my_split(tmp_nama)
    nama = ""
    for i in splited_nama:
        nama = nama + i.capitalize() + " "
    nama = nama.strip()
    return nama
##################### (end) #######################

# Varibale biasa, dipake biar rada enak dibaca oleh orang lain
# kaya yang dari tutorial hehee
posisi_nama_di_data = 2
posisi_id_di_data = 0

# kalo gk ngerti maksudnya apa, mungkin di bawah ini bisa bikin ngerti
#[['id', 'username', 'nama', 'alamat', 'password', 'role']] <-- nama valuenya
#[[ 1,    'admin',   'Admin', 'idk',    '12345',  'admin']] <-- valuenya
#[[ 0,      '1',       '2',    '3',       '4',      '5'  ]] <-- ini yang gw dimaksud posisi, gw lupa versi bahasa programnya kalo dalam matriks


# Fungsi check nama ada di data
##################### (start) #######################
def nama_ada_di_data(new_user_nama,datas):
    check = True
    for i in range (len(datas)):
        if new_user_nama != datas[i][posisi_nama_di_data]:
            check = False
        else:
            check = True
            break
    return check
##################### (end) #######################


# Fungsi register 
def register_user(datas):
    new_user_data = []
    not_registered = True
    while not_registered:
        # input new user data diri (start)
        new_user_nama = input("Masukan nama: ")
        new_user_nama = real_nama(new_user_nama)
        new_user_username = input("Masukan username: ")
        new_user_password = input("Masukan password: ")
        new_user_alamat = input("Masukan alamat: ")
        # input new user data diri (end)

        if nama_ada_di_data(new_user_nama,datas) == False:
            not_registered = False
            new_user_id = datas[-1][posisi_id_di_data] + 1
            new_user_role = "user"
            new_user = [new_user_id,new_user_username,new_user_nama,new_user_alamat,new_user_password,new_user_role]
                
            #input new user data ke datas (start)
            new_user_data.append(new_user)
            datas += new_user_data
            #inptu new user data ke datas berakhir

            print("\nUser " + new_user_username + "! Selamat datang di Kantong Ajaib")
            break
        else:
            not_registered=True
            print("\nNama sudah digunakan\n")
    return not_registered



