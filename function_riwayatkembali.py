from datetime import datetime


def sort_date(matrix):  # sort secara descending
    matrix.sort(key=lambda line: datetime.strptime(line[2], '%d/%m/%Y'), reverse=True)
    return matrix


def name_from_id(reff, name_id):  # mengambil nama dari id user
    for entries in reff:
        if entries[0] == name_id:
            return entries[2]
    return 'Name not found!'


def item_from_id(reff, item_id):  # mengambil gadget dari id gadget
    for entries in reff:
        if entries[0] == item_id:
            return entries[1]
    return 'Item not found!'


def iden_from_ref(s_list, reference):  # Mendapat user id, gadget id, dan jumlah
    for entries in s_list:
        if entries[0] == reference:
            return entries[1], entries[2], entries[4]


def riwayatkembali(users, items, taken, returned):  # fungsi utama
    again = True  # pelacak print ulang
    matrix = sort_date(returned[1:])  # membuat tabel tersortir
    times = 0  # penghitung augmenter i
    while again is True:
        for i in range(5):
            if i + (5 * times) == len(matrix):
                print('\nData sudah habis!')
                break  # Kondisional untuk data habis
            referral = matrix[i + (5 * times)][1]  # kode transaksi peminjaman
            user_id, gadget_id, total = iden_from_ref(taken, referral)  # mendapat user id, gadget id, dan jumlah
            name = name_from_id(users, user_id)
            item = item_from_id(items, gadget_id)
            if matrix[i + (5 * times)][3] == 'All':  # Mendapat Kuantitator Pengembalian
                returned = 'Semua'
            else:
                returned = '{} out of {}'.format(matrix[i + (5 * times)][3], total)
            # Memprint Registry
            print('\nID Pengembalian      : {}'.format(matrix[i + (5 * times)][0]))
            print('Nama Peminjam        : {}'.format(name))
            print('Nama Gadget          : {}'.format(item))
            print('Tanggal Pengembalian : {}'.format(matrix[i + (5 * times)][2]))
            print('Jumlah Pengembalian  : {}'.format(returned))
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
