from datetime import datetime


def sort_date(matrix):  # sort secara descending
    matrix.sort(key=lambda line: datetime.strptime(line[3], '%d/%m/%Y'), reverse=True)
    return matrix


def name_from_id(reff, name_id):  # mengambil nama dari id user
    for entries in reff:
        if entries[0] == name_id:
            return entries[2]
    return 'Name not found!'


def item_from_id(reff, item_id):  # mengambil consumable dari id consumable
    for entries in reff:
        if entries[0] == item_id:
            return entries[1]
    return 'Item not found!'


def riwayatambil(users, items, data):  # fungsi utama
    again = True  # pelacak print ulang
    matrix = sort_date(data[1:])  # membuat tabel tersortir
    times = 0  # penghitung augmenter i
    while again is True:
        for i in range(5):
            if i + (5 * times) == len(matrix):
                print('\nData sudah habis!')
                break  # Kondisional untuk data habis
            name = name_from_id(users, matrix[i + (5 * times)][1])
            item = item_from_id(items, matrix[i + (5 * times)][2])
            # Memprint Registry
            print('\nID Pengambilan       : {}'.format(matrix[i + (5 * times)][0]))
            print('Nama Pengambil       : {}'.format(name))
            print('Nama Consumable      : {}'.format(item))
            print('Tanggal Pengambilan  : {}'.format(matrix[i + (5 * times)][3]))
            print('Jumlah               : {}'.format(matrix[i + (5 * times)][4]))
        while True:  # Melakukan cetak lagi jika 'y'
            if len(matrix) - 5 * times >= 5:
                f_more = input('\nCetak lima lagi? (y/n): ').lower()
                if f_more == 'y' or f_more == 'n':
                    again = False if f_more == 'n' else True
                    times += 1
                    break
            else:
                ulang = input('\nUlang print dari awal? (y/n)').lower()
                if ulang == 'y' or ulang == 'n':
                    again = False if ulang == 'n' else True
                    times = 0
                    break
            print('\nMasukan tidak valid! Masukkan input yang valid!\n')  # Jika jawaban diluar 'y' atau 'n'
