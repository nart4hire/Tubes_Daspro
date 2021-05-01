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
    'Amulet', 'Saber', 'Whip', 'Greataxe', 'Robe', 'Hairpin', 'Crossbow', 'Tome'
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
        chance = random.randrange(10)
        item = item_list[random.randrange(len(item_list))]
        material = material_list[random.randrange(len(material_list))]
        prefix = prefix_list[random.randrange(len(prefix_list))]
        attribute = attribute_list[random.randrange(len(attribute_list))]
        year = random.randint(1, 1500)
        if 0 <= chance <= 5:
            if random.randrange(10) > 1:
                name = material + ' ' + item
                desc = 'A/an {} that is made of {}. Other than that ' \
                       'it appears to have no special effects.'.format(item, material)
                count = random.randint(10, 199)
                rarity = 'B'
            else:
                name = item
                desc = 'Just a/an normal {}. It has no special effects.'.format(name)
                count = random.randint(100, 999)
                rarity = 'C'
        elif 6 <= chance <= 8:
            name = prefix + ' ' + material + ' ' + item
            desc = 'A/an {} {} that is made of {}. It has {} ' \
                   'origins and though no one knows what its ' \
                   'special effects are. Maybe its creator made it on a whim.'.format(prefix, item, material, prefix)
            count = random.randint(5, 30)
            rarity = 'A'
        else:
            name = prefix + ' ' + material + ' ' + item + ' of ' + attribute
            desc = 'A/an {} {} that is made of {}. It radiates ' \
                   '{} energy and when used will imbue its actions ' \
                   'with the attribute of {}. Very rare!'.format(prefix, item, material, prefix, attribute)
            count = random.randint(1, 9)
            rarity = 'S'
        return [name, desc, count, rarity, year]
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
        f = open('gadget.csv', 'r')
    elif divvy == 2:
        f = open('consumable.csv', 'r')
    try:
        lines = f.read().split('\n')
    except UnboundLocalError:
        print("Error")
        return None
    for line in lines[1:-1]:
        past.append(line.split(';'))
    idx = int(lines[-2].split(';')[0].lstrip('C').lstrip('G').lstrip('0'))
    f.close()

    if divvy == 1:
        f = open('gadget.csv', 'a')
    elif divvy == 2:
        f = open('consumable.csv', 'a')
    counts = 0
    while idx != 999:
        counts += 1
        thing = make_item(divvy)
        if not (check(thing, past)):
            idx += 1
            past.append(thing)
            if divvy == 1:
                f.write(
                    'G{:03d};{};{};{};{};{}\n'.format(idx, thing[0], thing[1], thing[2], thing[3], thing[4])
                )
            elif divvy == 2:
                f.write(
                    'C{:03d};{};{};{};{}\n'.format(idx, thing[0], thing[1], thing[2], thing[3])
                )
    print(counts)
    f.close()


if __name__ == '__main__':
    x = int(input())
    make_csv(x)
