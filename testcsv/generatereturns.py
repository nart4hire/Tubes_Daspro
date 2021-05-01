import datetime
import random


def sort_date(data):
    matrix.sort(key=lambda entry: datetime.datetime.strptime(entry[3], '%d/%m/%Y'))
    return matrix


def csv_to_matrix(file):
    data = file.read()

    count = 0
    index_nline = []
    for char in data:
        if char == '\n':
            index_nline.append(count)
        count += 1

    matrix = []
    prev = -1
    for index in index_nline:
        matrix.append(data[prev + 1:index])
        prev = index

    for i in range(len(matrix)):
        line = matrix[i]
        count = 0
        index_comma = []
        for char in line:
            if char == ';':
                index_comma.append(count)
            count += 1
        lst = []
        prev = -1
        for index in index_comma:
            lst.append(line[prev + 1:index])
            prev = index
            if prev == index_comma[-1]:
                lst.append(line[prev + 1:])
        matrix[i] = lst

    return matrix[1:]


f = open('gadget_borrow_history.csv', 'r')
matrix = csv_to_matrix(f)
f.close()

f = open('gadget_return_history.csv', 'a')
matrix = sort_date(matrix)

for line in matrix:
    if line[5] != 'False':
        borrow_date = datetime.datetime.strptime(line[3], '%d/%m/%Y')
        time_change = datetime.timedelta(days=random.randint(1, 14))
        return_date = datetime.datetime.strftime(borrow_date + time_change, '%d/%m/%Y')
        returned = 'All' if line[5] == 'True' else line[5]
        code = 'R' + line[1].lstrip('U')\
               + line[2].lstrip('G') + '{:03d}'.format(int(line[4] if returned == 'All' else returned))
        f.write('{};{};{};{}\n'.format(code, line[0], return_date, returned))
