from f10 import meminta_consumable

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
f = open("consumable_tmp.csv","r")
raw_lines = f.readlines()
f.close()
lines = [raw_line.replace("\n","") for raw_line in raw_lines]

def cnvrt_jumlah_tahun_to_int(array_data):
    arr_cpy = array_data[:]
    arr_cpy[3] = int(arr_cpy[3])
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
start = input(">>> ")
if start == "minta":
    meminta_consumable(datas)

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
f=open("consumable_tmp.csv","w")
f.write(datas_as_string)
f.close()
##################### (end) #######################