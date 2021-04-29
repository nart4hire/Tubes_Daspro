# from textwrap import wrap
#
# f = open('pi.txt', 'r')
# hex_pi = f.read().replace('\n', '')
# hexapi = wrap(hex_pi, 8)
# f.close()
#
# f = open('pihex.txt', 'w')
# for hexes in hexapi:
#     f.write('0x' + hexes + '\n')
# f.close()

# f = open('pihex.txt', 'r')
# hexapi = f.read().split('\n')
# i = 0
# for passes in hexapi:
#     print(passes)
#     j = 0
#     i += 1
#     for hexes in hexapi[i:]:
#         print(hexes)
#         j += 1
#         if passes == hexes:
#             print('same at ' + str(i) + ' ' + str(j))
# f.close()
