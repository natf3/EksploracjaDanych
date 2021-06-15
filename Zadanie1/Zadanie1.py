lista1 = [ 1, 2, 3, 'jeden', 'dwa', 'trzy', 99.1, 98.2, 97.3, 'a']
lista2 = []

for i in lista1:
    if type(i) != str:
        lista2.append(int(i))

print(lista2)