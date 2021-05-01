# load(pathname)->datas (membaca data csv)

def potong(string, mark):  # pseudosplit + datastrip, digunakan clean dan load
    arr = []
    temp = ""
    for i in string:
        if i != mark:
            temp += i
        else:
            arr.append(temp.strip())
            temp = ""
    arr.append(temp.strip())
    return arr


def clean(arr):  # digunakan fungsi load untuk cleansing array2d keseluruhan, menggunakan potong()
    data = []
    for i in arr:
        if (i[-1] != "\n"): i += "\n"
        data.append(potong(i[:-1], ';'))
    return data


def toInt(data, idxList):  # digunakan fungsi load untuk mengubah data pada idx tertentu menjadi int
    for i in idxList:
        for j in range(1, len(data)):
            data[j][i] = int(data[j][i])
    return data


def load(folder):
    # loading otomatis, tidak untuk dipanggil (sudah auto dipanggil diawal)

    # open
    raw_user = open(folder + r"\user.csv", "r")
    raw_gadget = open(folder + r"\gadget.csv", "r")
    raw_consumable = open(folder + r"\consumable.csv", "r")
    raw_consumable_history = open(folder + r"\consumable_history.csv", "r")
    raw_gadget_borrow_history = open(folder + r"\gadget_borrow_history.csv", "r")
    raw_gadget_return_history = open(folder + r"\gadget_return_history.csv", "r")

    # extract
    user = toInt(clean(raw_user.readlines()), [])
    gadget = toInt(clean(raw_gadget.readlines()), [3])
    consumable = toInt(clean(raw_consumable.readlines()), [3])
    consumable_history = toInt(clean(raw_consumable_history.readlines()), [4])
    gadget_borrow_history = toInt(clean(raw_gadget_borrow_history.readlines()), [4])
    gadget_return_history = toInt(clean(raw_gadget_return_history.readlines()), [])

    # close
    raw_user.close()
    raw_gadget.close()
    raw_consumable.close()
    raw_consumable_history.close()
    raw_gadget_borrow_history.close()
    raw_gadget_return_history.close()

    return [user, gadget, consumable, consumable_history, gadget_borrow_history, gadget_return_history]
