import hashlib
import random

first_names = [
    'Ava', 'Beatrice', 'Courtney', 'Dave', 'Ethan', 'Faris',
    'George', 'Hamilton', 'Ignis', 'Jean', 'Katnis',
    'Laetitia', 'Maureen', 'Nobita', 'Ophelia', 'Priscilla',
    'Quake', 'Randal', 'Sven', 'Tabatha', 'Ursula', 'Victoria',
    'William', 'Xander', 'Yaeger', 'Zaccheus'
]

last_names = [
    'Adams', 'Brooks', 'Collins', 'Davis', 'Edwards', 'Freeman',
    'Gibson', 'Harrison', 'Irving', 'Johnson', 'Kennedy',
    'Lewis', 'Miller', 'Nichols', 'Owens', 'Pace',
    'Queen', 'Robinson', 'Sullivan', 'Taylor', 'Ufford',
    'Valdez', 'Walker', 'Xenos', 'Yaleman', 'Zimmerman'
]

alphabet = list(map(chr, range(65, 91)))


def gen_id(last_id):
    first = first_names[random.randrange(len(first_names))]
    last = last_names[random.randrange(len(last_names))]
    if random.randrange(10) > 7:
        name = '{} {}. {}'.format(first, alphabet[random.randrange(len(alphabet))], last)
    else:
        name = '{} {}'.format(first, last)
    if random.randrange(10) > 4:
        username = first + str(random.randrange(100000))
    else:
        username = last + str(random.randrange(100000))
    p = str(random.randrange(1000)) + alphabet[random.randrange(len(alphabet))]
    word = str(random.randrange(1000)) + alphabet[random.randrange(len(alphabet))]
    password = p + word
    current_id = 'U{:03d}'.format(last_id + 1)
    role = 'user'
    address = 'User St. No.{}, Imaginary Country'.format(last_id + 1)
    return [current_id, username, name, address, password, role]


f = open('user.csv', 'r')
file = f.read().split('\n')
for i in range(len(file) - 1):
    lst = file[i].split(';')
    file[i] = lst[2]
f.close()

f = open('user.csv', 'a')
idx = 0
count = 0
while idx < 100:
    iden = gen_id(idx)
    if iden[2] not in file:
        for item in iden:
            f.write(item)
            f.write(';' if item != iden[-1] else '\n')
        file.append(iden[2])
        idx += 1
    count += 1
f.close()
