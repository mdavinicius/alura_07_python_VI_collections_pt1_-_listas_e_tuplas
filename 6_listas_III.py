# enumerar os elementos de uma lista com loop for
idades = [15, 87, 32, 65, 56, 32, 49, 37]
contador = 0

for n in idades:
    print("{} - {}".format(contador, n))
    contador += 1
print("-----------------------------------")

# enumerar os elementos de uma lista com loop for e range
for i in range(len(idades)):
    print("{} - {}".format(i, idades[i]))
print("-----------------------------------")

# a função enumerate() já faz esse trabalho de enumerar uma lista, colocando cada elemento em uma tupla
lista = list(enumerate(idades))
print(lista)
print("-----------------------------------")

# fazendo uma iteração na lista numerada com o enumarete()
for i in enumerate(idades):
    print(i)
print("-----------------------------------")

# chamando as duas variáveis da Tupla, é possível desempacota-la e trazer seus elementos separadamente
for indice, idade in enumerate(idades):
    print(indice, 'x', idade)
print("-----------------------------------")

# criando uma Lista de Tuplas com 3 elementos em cada Tupla e printando cada um deles
usuarios = [
    ("Guilherme", 37, 1981),
    ("Daniela", 31, 1987),
    ("Paulo", 39, 1979)
]

for n in usuarios:
    print(n)
print("-----------------------------------")

# definimos as variaveis da Tupla, podemos imprimir apenas parte dela
for nome, idade, ano in usuarios:
    print(nome)
print("-----------------------------------")

# essa é outra forma de desempacotar. O '_' ignora os valores correspondentes. Então em uma Tupla de 3 elementos, estou printando o elemento do meio
for _, idade, _, in usuarios:
    print(idade)
print("-----------------------------------")

# com o sorted() retornamos a lista ordenada do menor para o maior
print(sorted(idades))
print("-----------------------------------")

# com o reverse(sorted()) armazenamos na memoria a listas do maior para o menor
print((reversed(sorted(idades))))
print("-----------------------------------")

# transformando o reverse(sorted()) em uma lista com list(), teremos a visualização de uma lista do maior para o menor
print(list(reversed((sorted((idades))))))
print("-----------------------------------")

# outra forma de ter a lista do maior para o menor, é usando sorted() com 'reverse=True'
print(sorted(idades, reverse=True))
print("-----------------------------------")

