# Varibale biasa, dipake biar rada enak dibaca oleh orang lain
# kaya yang dari tutorial hehee

posisi_username_di_data = 1
posisi_password_di_data = 4

#[['id', 'username', 'nama', 'alamat', 'password', 'role']]
#[[ 1,    'admin',   'Admin', 'idk',    '12345',  'admin']]
#[[ 0,      '1',       '2',    '3',       '4',      '5'  ]] <-- ini yang gw dimaksud posisi, gw lupa versi bahasa programnya


# Fungsi check username di data dan posisi passwordnya 
##################### (start) #######################
def username_ada_di_data(login_username,datas):
    check = True
    for i in range (len(datas)):
        if login_username != datas[i][posisi_username_di_data]:
            check = False
        else:
            check = True
            break
    return (check,i)
##################### (end) #######################

# Fungsi login
def login_user (datas):
    not_login = True
    while not_login:
        login_username = input("Username : ")
        login_password=input("Password : ")

        # bikin varibale baru untuk menyimpan value pertama dan kedua dari fungsi username_ada_di_data
        username_benar = username_ada_di_data(login_username,datas)[0]
        posisi_password_user =  username_ada_di_data(login_username,datas)[1]
       

        if username_benar == False:
            not_login=True
            print("Username salah")
            break
        else:
            if login_password == datas[posisi_password_user][posisi_password_di_data]:
                not_login=False
                print()
                print("Halo",login_username,"Selamat datang di Kantong Ajaib\n")
                break
            else:
                not_login=True
                print("username atau password salah")
    return not_login
