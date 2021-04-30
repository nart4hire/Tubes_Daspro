from datetime import datetime


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
            if char == ',':
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


def sort_date(matrix):
    matrix.sort(key=lambda line: datetime.strptime(line[3], '%d/%m/%Y'), reverse=True)
    return matrix


def riwayatambil():
    f = open('testcsv/consumable_history.csv', 'r')
    g = open('testcsv/consumable.csv', 'r')
    history = sort_date(csv_to_matrix(f))
    gadgets = csv_to_matrix(g)

    again = True
    n = 0
    while again is True:
        for i in range(n, n + 5):
            print('ID pengambilan :' + )
        if input('Lihat 5 berikut? (Y/N) :') != 'Y':
            again = False

        n += 5
    f.close()


if __name__ == '__main__':
    riwayatambil()
