import random
from datetime import datetime

names_list = [
    'Ava', 'Beatrice', 'Courtney', 'Dave', 'Ethan', 'Faris',
    'George', 'Hamilton', 'Ignis', 'Jean', 'Katnis',
    'Laetitia', 'Maureen', 'Nobita', 'Ophelia', 'Priscilla',
    'Quake', 'Randal', 'Sven', 'Tabatha', 'Ursula', 'Victoria',
    'William', 'Xander', 'Yaeger', 'Zaccheus'
]

alphabet = list(map(chr, range(97, 123))) + list(map(chr, range(65, 91)))


def make_csv(file, divvy):
    if divvy == 1:
        f = open(file, 'w')
        f.write('id,id_peminjam,id_gadget,tanggal_peminjaman,jumlah,is_returned\n')

        for i in range(10000):
            b = names_list[random.randint(0, 25)]
            c = 'G{:03d}'.format(random.randint(0, 999))
            d = '{:02d}/{:02d}/{}'.format(random.randint(1, 28), random.randint(1, 12), random.randint(2000, 2020))
            e = random.randint(1, 999)
            tf = random.choice([True, False])
            a = 'T' + c + datetime.strptime(d, '%d/%m/%Y').strftime('%m%y') + '{:03d}'.format(e)
            f.write('{},{},{},{},{},{}\n'.format(a, b, c, d, e, tf))

        f.close()
    elif handle == 2:
        f = open(file, 'w')
        f.write('id,id_pengambil,id_consumable,tanggal_peminjaman,jumlah\n')

        for i in range(10000):
            b = names_list[random.randint(0, 25)]
            c = 'C{:03d}'.format(random.randint(0, 999))
            d = '{:02d}/{:02d}/{}'.format(random.randint(1, 28), random.randint(1, 12), random.randint(2000, 2020))
            e = random.randint(1, 999)
            a = 'T' + c + datetime.strptime(d, '%d/%m/%Y').strftime('%m%y') + '{:03d}'.format(e)
            f.write('{},{},{},{},{}\n'.format(a, b, c, d, e))

        f.close()
    return None


filename = input()
handle = int(input('1 for gadget, 2 for consumable'))
make_csv(filename, handle)
