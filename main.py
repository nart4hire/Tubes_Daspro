from function_login import login_user
from function_register import register_user

# Fungsi split ngambil dari google :v
##################### (start) #######################
def my_split(s, sep=','):
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


# Baca file csv, ini ngikutin kaya di tutorial yang tersebar
##################### (start) #######################
f = open("user.csv","r")
raw_lines = f.readlines()
f.close()
lines = [raw_line.replace("\n","") for raw_line in raw_lines]

def cnvrt_id_to_int(array_data):
    arr_cpy = array_data[:]
    arr_cpy[0] = int(arr_cpy[0])
    return arr_cpy

def cnvrt_line_data(line):
    raw_array_data = my_split(line)
    array_data = [data.strip() for data in raw_array_data]
    return array_data   

raw_header = lines.pop(0)
header = cnvrt_line_data(raw_header)

datas=[]
for line in lines:
    array_data = cnvrt_line_data(line)
    real_value = cnvrt_id_to_int(array_data)
    datas.append(real_value)
##################### (end) #######################


# Hanya simple penggunaan dari fungsi yang udah diimport
##################### (start) #######################
print("Register or Login")
menu = input(">> ")

# Login
if menu == "Login" or menu == "login":
    register_sukses = False
    akses = True
    if login_user(datas) == False:
        akses = True
    else:
        akses = False
    
# Register
elif menu =="Register" or menu =="register":
    register_sukses = True
    if register_user(datas) == False:
        register_sukses = True
    else:
        register_sukses = False
    
##################### (end) #######################





# Save file, ngikutin juga kaya di tutorial
##################### (start) #######################
def convert_datas_to_string():
  string_data = ",".join(header) + "\n"
  for arr_data in datas:
    arr_data_all_string = [str(var) for var in arr_data]
    string_data += ",".join(arr_data_all_string)
    string_data += "\n"
  return string_data

datas_as_string = convert_datas_to_string()
f=open("user.csv","w")
f.write(datas_as_string)
f.close()
##################### (end) #######################


# Login ketika sudah register (iseng aja, gk tau kalo harus gini atau kagak)
# Ditaro disini, karena kan kalo register, ada data baru
# perlu disave dulu, makanya taro sesudah save file
if register_sukses == True:
    print("\nKUY LOGIN!!\n")
    login_user(datas)

