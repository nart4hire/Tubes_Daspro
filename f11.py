from datetime import datetime


def sort_date(matrix):
    matrix.sort(key=lambda line: datetime.strptime(line[3], '%d/%m/%Y'), reverse=True)
    return matrix


def find_from_id(reff, item_id):
    for entries in reff:
        if entries[0] == item_id:
            return entries[1]
    return 'Item not found!'


def riwayatpinjam(items, data):
    again = True
    matrix = sort_date(data[1:])
    times = 0
    while again is True:
        for i in range(5):
            item = find_from_id(items, matrix[i + (5 * times)][2])
            print('\nID Peminjaman      : {}'.format(matrix[i + (5 * times)][0]))
            print('Nama Peminjam      : {}'.format(matrix[i + (5 * times)][1]))
            print('Nama Gadget        : {}'.format(item))
            print('Tanggal Peminjaman : {}'.format(matrix[i + (5 * times)][3]))
            print('Jumlah             : {}'.format(matrix[i + (5 * times)][4]))
        while True:
            f_more = input('\nCetak lima lagi? (y/n): ').lower()
            if f_more == 'y' or f_more == 'n':
                again = False if f_more == 'n' else True
                break
            print('\nMasukan tidak valid! Masukkan input yang valid!\n')
        times += 1
