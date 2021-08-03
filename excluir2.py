#------------------------------
#
# Teste algorítmo para localizar o index da lista que contenha y 
#
#----------------------------
dado = dict()
lista = []
for i in range(9):
    dado = {'x': i, 'x-1': i-1}
    lista.append(dado)
x = 0
print(lista)
y = 3
while lista[x]['x'] != y:
    x += 1

print(f'igual à 3 na coluna {x}')