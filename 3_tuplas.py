guilherme = ('Guilherme', 37, 1981)
daniela = ('Daniela', 31, 1987)

# guilherme.append(65)  # dará erro pois Tuplas são imutáveis, não é possível adicionar ou remover elementos

usuarios = [guilherme, daniela]  # uma Lista de Tuplas
print(usuarios)
print("-----------------------------------")

usuarios.append(('Paulo', 39, 1979))  # a lista 'usuarios' aceita append(), assim adicionamos uma nova Tupla dentro da Lista
print(usuarios)
print(usuarios[0])  # a lista posição 0 traz a 1ª Tupla
print("-----------------------------------")

# usuarios[0][0] = 'Guilherme Silveira'  # dará erro pois Tupla são imutáveis, não alteram o valor

# Agora se fizer uma Tupla com Listas dentro, continuaremos não podendo editar a Tupla. Porém, o objeto da lista será
# mutável, pois Listas são mutáveis. Exemplo:

tupla = (["Vini", 18], ["Panai", 19])  # uma Tupla com Listas
print(tupla)
print(tupla[0])  # printar apenas a primeira Lista da Tupla
tupla[0][1] = 20  # alterando o valor 1 da lista, de '18' para '20'
print(tupla)
tupla[0].append("Algo a mais")  # adicionando um novo elemento na lista
print(tupla)
tupla[0].pop()  # removendo o ultimo elevento da lista 1 com o pop()
print(tupla)