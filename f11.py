from datetime import datetime


def sort_date(matrix):
    matrix.sort(key=lambda line: datetime.strptime(line[3], '%d/%m/%Y'), reverse=True)
    return matrix


def name_from_id(reff, name_id):
    for entries in reff:
        if entries[0] == name_id:
            return entries[2]
    return 'Name not found!'


def item_from_id(reff, item_id):
    for entries in reff:
        if entries[0] == item_id:
            return entries[1]
    return 'Item not found!'


def riwayatpinjam(users, items, data):
    again = True
    matrix = sort_date(data[1:])
    times = 0
    while again is True:
        for i in range(5):
            if i + (5 * times) == len(matrix) or matrix[i + (5 * times)][3] == '01/01/0001':
                print('\nData sudah habis!')
                break
            name = name_from_id(users, matrix[i + (5 * times)][1])
            item = item_from_id(items, matrix[i + (5 * times)][2])
            if matrix[i + (5 * times)][5] == 'True':
                returned = 'Dikembalikan Semua'
            elif matrix[i + (5 * times)][5] == 'False':
                returned = 'Belum Dikembalikan'
            else:
                returned = 'Dikembalikan Sebagian ({})'.format(matrix[i + (5 * times)][5])
            print('\nID Peminjaman      : {}'.format(matrix[i + (5 * times)][0]))
            print('Nama Peminjam      : {}'.format(name))
            print('Nama Gadget        : {}'.format(item))
            print('Tanggal Peminjaman : {}'.format(matrix[i + (5 * times)][3]))
            print('Jumlah             : {}'.format(matrix[i + (5 * times)][4]))
            print('Status Peminjaman  : {}'.format(returned))
        while True:
            if len(matrix) - 5 * times >= 5:
                f_more = input('\nCetak lima lagi? (y/n): ').lower()
                if f_more == 'y' or f_more == 'n':
                    again = False if f_more == 'n' else True
                    break
            else:
                ulang = input('\nUlang print dari awal? (y/n)').lower()
                if ulang == 'y' or ulang == 'n':
                    again = False if ulang == 'n' else True
                    times = 0
                    break
            print('\nMasukan tidak valid! Masukkan input yang valid!\n')
        times += 1
