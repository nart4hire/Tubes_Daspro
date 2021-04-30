import random

# id, nama, deskripsi, jumlah, rarity, tahun_ditemukan
# id, nama, deskripsi, jumlah, rarity

attribute_list = [
    'Light', 'Darkness', 'Water', 'Fire', 'Lightning', 'Wind', 'Earth',
    'Ice', 'Venom', 'Magma', 'Life', 'Death', 'Time', 'Space', 'Wood'
]

prefix_list = [
    'Divine', 'Evil', 'Corrupted', 'Blessed', 'Magical',
    'Spiritual', 'Poisonous', 'Dwarven', 'Elven',
    'Explosive', 'Grand', 'Chaotic', 'Abyssal'
]

material_list = [
    'Steel', 'Copper', 'Iron', 'Emerald',
    'Silver', 'Gold', 'Platinum',
    'Ruby', 'Sapphire', 'Jade', 'Topaz'
]

item_list = [
    'Crown', 'Tiara', 'Sword', 'Shield', 'Bow', 'Cloak', 'Grail', 'Key',
    'Cleats', 'Armor', 'Pauldrons', 'Circlet', 'Ring', 'Bracelet', 'Necklace',
    'Amulet', 'Saber', 'Whip', 'Greataxe', 'Robe', 'Hairpin', 'Crossbow'
]

cons_list = [
    'Apples', 'Candies', 'Pears', 'Arrows', 'Sigils', 'Potions', 'Salmon', 'Carps',
    'Peaches', 'Bread Cloves', 'Mushrooms', 'Pills', 'Pearls', 'Beads', 'Liquids', 'Essences',
    'Milk Cartons', 'Juices', 'Smoothies', 'Energy Drinks', 'Cupcakes', 'Panties'
]

suffix_list = [
    'Healing', 'Restoration', 'Rejuvenation', 'Tempering', 'Fulfilling', 'Immortality',
    'Death', 'Memorization', 'Invigoration', 'Focus', 'Telekinesis', 'Flying', 'Warding',
    'Entrancement', 'Infatuation', 'Incitement'
]


def check(item, matrix):
    for items in matrix:
        if items[1] == item[1]:
            return True
    return False



def make_item(divvy):
    if divvy == 1:
        if random.randrange(10) > 1:
            prefix = ''
        else:
            prefix = prefix_list[random.randrange(len(prefix_list))]
        material = material_list[random.randrange(len(material_list))]
        item = item_list[random.randrange(len(item_list))]
        name = prefix + ' ' + material + ' ' + item
        if random.choice([True, False]) is True:
            attribute = attribute_list[random.randrange(len(attribute_list))]
            name = name + ' of {}'.format(attribute)
            desc = 'A/an {} {} made of {}. It has the {} attribute, ' \
                   'and has \'{}\' origins.'.format(prefix, item, material, attribute, prefix)
        else:
            desc = 'A/an {} {} made of {}. It doesn\'t have an attribute, ' \
                   'and has \'{}\' origins.'.format(prefix, item, material, prefix)
        return name, desc
    elif divvy == 2:
        chance = random.randrange(10)
        cons = cons_list[random.randrange(len(cons_list))]
        material = material_list[random.randrange(len(material_list))]
        prefix = prefix_list[random.randrange(len(prefix_list))]
        suffix = suffix_list[random.randrange(len(suffix_list))]
        if 0 <= chance <= 5:
            if random.randrange(10) > 1:
                name = material + ' ' + cons
                desc = '{} that seem to be made of {}. Other than that ' \
                       'they appear to have no special effects.'.format(cons, material)
                count = random.randint(10, 199)
                rarity = 'B'
            else:
                name = cons
                desc = 'Just normal {}. They have no special effects.'.format(name)
                count = random.randint(100, 999)
                rarity = 'C'
        elif 6 <= chance <= 8:
            name = prefix + ' ' + material + ' ' + cons
            desc = '{} {} that are seemingly made of {}. They radiate ' \
                   '{} energy and their effects are unknown though ' \
                   'one might surmise them from its name.'.format(prefix, cons, material, prefix)
            count = random.randint(5, 30)
            rarity = 'A'
        else:
            name = prefix + ' ' + material + ' ' + cons + ' of ' + suffix
            desc = '{} {} that are seemingly made of {}. They radiate ' \
                   '{} energy and when used/consumed will have the ' \
                   'effect of {}. Very rare!'.format(prefix, cons, material, prefix, suffix)
            count = random.randint(1, 9)
            rarity = 'S'
        return [name, desc, count, rarity]


def make_csv(divvy):
    past = []
    if divvy == 1:
        f = open('gadget.csv', 'a')
        f.write('id,nama,deskripsi,jumlah,rarity,tahun_ditemukan\n')
    elif divvy == 2:
        f = open('consumable.csv', 'r')
        lines = f.read().split('\n')
        for line in lines[1:-1]:
            past.append(line.split(','))
        idx = int(lines[-2].split(',')[0].lstrip('C').lstrip('G').lstrip('0'))
        f.close()
        f = open('consumable.csv', 'a')
        counts = 0
        while idx != 999:
            counts += 1
            consumable = make_item(divvy)
            if not(check(consumable, past)):
                idx += 1
                past.append(consumable)
                f.write(
                    'C{:03d},{},{},{},{}\n'.format(idx, consumable[0], consumable[1], consumable[2], consumable[3])
                )
        print(counts)
        f.close()


# for i in range(10000):
#     b = names_list[random.randint(0, 25)]
#     c = 'G{:03d}'.format(random.randint(0, 999))
#     d = '{:02d}/{:02d}/{}'.format(random.randint(1, 28), random.randint(1, 12), random.randint(2000, 2020))
#     e = random.randint(1, 999)
#     tf = random.choice([True, False])
#     a = 'T' + c + datetime.strptime(d, '%d/%m/%Y').strftime('%m%y') + '{:03d}'.format(e)
#     f.write('{},{},{},{},{},{}\n'.format(a, b, c, d, e, tf))
#
# f.close()

if __name__ == '__main__':
    make_csv(2)
