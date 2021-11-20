zakupy = {'Piekarnia': ['chleb', 'bułki', 'pączke'], 'Warzywniak': ['marchew','seler','rukola']}

x = 0
for sklep, lista in zakupy.items():
    print(f'Idę do {sklep.upper()}, aby kupić: {lista}')
    x += len(lista)

print(f'W sumię kupię {x} przedmiotów')
print("pierwszy commit")
print("drugi commit")
