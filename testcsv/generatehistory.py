import random
from datetime import datetime

alphabet = list(map(chr, range(97, 123))) + list(map(chr, range(65, 91)))


def make_csv(divvy):
    if divvy == 1:
        f = open('gadget_borrow_history.csv', 'w')
        f.write('id;id_peminjam;id_gadget;tanggal_peminjaman;jumlah;is_returned\n')

        for i in range(101):
            b = 'U{:03d}'.format(random.randint(1, 101))
            c = 'G{:03d}'.format(random.randint(0, 999))
            d = '{:02d}/{:02d}/{}'.format(random.randint(1, 28), random.randint(1, 12), random.randint(2000, 2020))
            e = random.randint(10, 100)
            i_r = random.choice([True, False]) if random.randrange(10) > 4 else (random.randrange(e - 2) + 1)
            a = 'T' + b.lstrip('U') + c.lstrip('G') + '{:03d}'.format(e)
            f.write('{};{};{};{};{};{}\n'.format(a, b, c, d, e, i_r))

        f.close()
    elif handle == 2:
        f = open('consumable_history.csv', 'w')
        f.write('id,id_pengambil,id_consumable,tanggal_peminjaman,jumlah\n')

        for i in range(101):
            b = 'U{:03d}'.format(random.randint(1, 101))
            c = 'C{:03d}'.format(random.randint(0, 999))
            d = '{:02d}/{:02d}/{}'.format(random.randint(1, 28), random.randint(1, 12), random.randint(2000, 2020))
            e = random.randint(1, 999)
            a = 'T' + b.lstrip('U') + c.lstrip('C') + '{:03d}'.format(e)
            f.write('{},{},{},{},{}\n'.format(a, b, c, d, e))

        f.close()
    return None


handle = int(input('1 for gadget, 2 for consumable'))
make_csv(handle)
