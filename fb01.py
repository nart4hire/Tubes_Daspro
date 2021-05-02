def make_pihexes():  # membuat list integer dari list heksadesimal pihex.txt
    f = open('pihex.txt', 'r')
    hexes = f.read()
    hex_list = []
    prev_idx = 0
    for i in range(len(hexes)):
        if hexes[i] == '\n':
            hex_list.append(int(hexes[prev_idx:i], 16))
            prev_idx = i + 1
    f.close()
    return hex_list


def make_database():  # untuk mengetes fungsi pihash()
    f = open('testcsv/user.csv', 'r')
    text = f.read()
    matrix = []
    entries = []
    prev_idx = 0
    for j in range(len(text)):
        if text[j] == ';':
            entries.append(text[prev_idx:j])
            prev_idx = j + 1
        elif text[j] == '\n':
            entries.append(text[prev_idx:j])
            matrix.append(entries)
            entries = []
            prev_idx = j + 1
    return matrix


def rotate(x, y):
    z = (((x & 0xffffffff) << (y & 0b00011111)) | ((x & 0xffffffff) >> (32 - (y & 0b00011111)))) & 0xffffffff
    return z


def lshift(x, y):
    z = (x & 0xffffffff) << (y & 0b00011111)
    return z


def rshift(x, y):
    z = (x & 0xffffffff) >> (y & 0b00011111)
    return z


def bit_opp1(x, y, z):
    f = ((x & y) ^ (y | z)) | (x ^ z)
    return f


def bit_opp2(x, y, z):
    f = ~(x & y) ^ (y & (x | z))
    return f


def map1(n):
    m = rotate(n, 2) ^ rshift(n, 29) ^ rotate(n, 13)
    return m


def map2(n):
    m = rotate(n, 17) ^ lshift(n, 28) ^ rotate(n, 3)
    return m


def map3(n):
    m = lshift(n, 7) ^ rotate(n, 18) ^ rshift(n, 19)
    return m


def map4(n):
    m = rshift(n, 23) ^ rotate(n, 8) ^ lshift(n, 11)
    return m


def mutate(bl, idx, constant, mutator):
    a = bl[(idx + 1) % 8]
    b = bl[(idx + 2) % 8]
    c = bl[(idx + 3) % 8]
    d = bl[(idx + 4) % 8]
    e = bl[(idx + 5) % 8]
    f = bl[(idx + 6) % 8]
    g = bl[(idx + 7) % 8]
    torso = bl[idx] + map1(d) + bit_opp1(a, b, c) + constant
    abdomen = d + map2(bl[idx]) + bit_opp2(e, f, g) + mutator
    h = (torso + abdomen) & 0xffffffff
    return h


def make_message_board(password):
    password = str(password)
    lst = [ord(x) for x in password]
    lst.append(128)
    for i in range(len(lst), 63):
        lst.append(0)
    lst.append(len(password) * 8)
    mb = []
    for i in range(0, 16):
        mb.append((lst[4 * i] << 24) + (lst[4 * i + 1] << 16) + (lst[4 * i + 2] << 8) + lst[4 * i + 3])
    for i in range(16, 64):
        mb.append((mb[i - 15] + map3(mb[i - 14]) + map4(mb[i - 9]) + mb[i - 2]) & 0xffffffff)
    return mb
  

def pihash(password):
    pihexes = make_pihexes()
    bases = pihexes[:8]
    m_board = make_message_board(password)
    xor_w = m_board[0]
    for chunks in m_board[1:]:
        xor_w ^= chunks
    a = (len(password) * 8 * ((xor_w & 7) + 1) + (~xor_w & 127))
    for i in range(64):
        k = i % 8
        bases[k] = mutate(bases, k, pihexes[a], m_board[i])
    hashed = ''.join(format(base, 'x') for base in bases)
    return hashed


def test():
    hashed = pihash(input('Input string that will be hashed :'))
    print(hashed)


if __name__ == '__main__':
    test()
