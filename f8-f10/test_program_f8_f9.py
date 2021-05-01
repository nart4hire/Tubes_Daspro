from f8 import meminjam_gadget
from f9 import mengembalikan_gadget
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
# gadget.csv yg dibaca
##################### (start) #######################
f = open("gadget_tmp.csv","r")
raw_lines = f.readlines()
f.close()
lines = [raw_line.replace("\n","") for raw_line in raw_lines]

def cnvrt_jumlah_tahun_to_int(array_data):
    arr_cpy = array_data[:]
    arr_cpy[3] = int(arr_cpy[3])
    arr_cpy[5] = int(arr_cpy[5])
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
    real_value = cnvrt_jumlah_tahun_to_int(array_data)
    datas.append(real_value)
##################### (end) #######################

# gadget_borrow_history.csv yg dibaca
##################### (start) #######################
g = open("gadget_borrow_history_tmp.csv","r")
raw_lines_g = g.readlines()
g.close()
lines_g = [raw_line.replace("\n","") for raw_line in raw_lines_g]

def cnvrt_jumlah_to_int(array_data):
    arr_cpy = array_data[:]
    arr_cpy[4] = int(arr_cpy[4])
    return arr_cpy

def cnvrt_line_data_g(line):
    raw_array_data = my_split(line)
    array_data = [data.strip() for data in raw_array_data]
    return array_data   

raw_header_g = lines_g.pop(0)
header_g = cnvrt_line_data_g(raw_header_g)

datas_g=[]
for line in lines_g:
    array_data_g = cnvrt_line_data_g(line)
    real_value_g = cnvrt_jumlah_to_int(array_data_g)
    datas_g.append(real_value_g)
##################### (end) #######################

# gadget_return_history_tmp.csv yang dibaca
##################### (start) #######################
r = open("gadget_return_history_tmp.csv","r")
raw_lines_r = r.readlines()
r.close()
lines_r = [raw_line.replace("\n","") for raw_line in raw_lines_r]

def cnvrt_jumlah_peminjaman_to_int(array_data):
    arr_cpy = array_data[:]
    arr_cpy[4] = int(arr_cpy[4])
    return arr_cpy

def cnvrt_line_data_r(line):
    raw_array_data = my_split(line)
    array_data = [data.strip() for data in raw_array_data]
    return array_data   

raw_header_r = lines_r.pop(0)
header_r = cnvrt_line_data_r(raw_header_r)

datas_r=[]
for line in lines_r:
    array_data_r = cnvrt_line_data_r(line)
    real_value_r = cnvrt_jumlah_peminjaman_to_int(array_data_r)
    datas_r.append(real_value_r)
##################### (end) #######################

start = input(">>> ")
print()
id_user = "U1"
if start == "pinjam":
    meminjam_gadget(datas,datas_g,id_user)
elif start == "kembalikan":
    mengembalikan_gadget(datas,datas_g,datas_r,id_user)


def convert_datas_r_to_string():
  string_data = ",".join(header_r) + "\n"
  for arr_data in datas_r:
    arr_data_all_string = [str(var) for var in arr_data]
    string_data += ",".join(arr_data_all_string)
    string_data += "\n"
  return string_data

datas_r_as_string = convert_datas_r_to_string()
r = open("gadget_return_history_tmp.csv","w")
r.write(datas_r_as_string)
r.close()


def convert_datas_g_to_string():
  string_data = ",".join(header_g) + "\n"
  for arr_data in datas_g:
    arr_data_all_string = [str(var) for var in arr_data]
    string_data += ",".join(arr_data_all_string)
    string_data += "\n"
  return string_data

datas_g_as_string = convert_datas_g_to_string()
g = open("gadget_borrow_history_tmp.csv","w")
g.write(datas_g_as_string)
g.close()



##################### (start) #######################
def convert_datas_to_string():
  string_data = ",".join(header) + "\n"
  for arr_data in datas:
    arr_data_all_string = [str(var) for var in arr_data]
    string_data += ",".join(arr_data_all_string)
    string_data += "\n"
  return string_data

datas_as_string = convert_datas_to_string()
f=open("gadget_tmp.csv","w")
f.write(datas_as_string)
f.close()
##################### (end) #######################