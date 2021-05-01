functions = [
    'register', 'login', 'carirarity', 'caritahun', 'tambahitem', 'hapusitem',
    'ubahjumlah', 'pinjam', 'kembalikan', 'minta', 'riwayatpinjam', 'riwayatkembali'
    'riwayatambil', 'save', 'help', 'exit'
]


def get_root_func(function):
    if '(' in function:
        return function[:function.index('(')]
    return function


def get_func_index(function):
    if function in functions:
        return functions.index(function)
    return None

