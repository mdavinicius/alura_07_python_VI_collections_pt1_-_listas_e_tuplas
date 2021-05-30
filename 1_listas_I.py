idades = [39, 30, 27, 18]

print(f"O tipo da variável é: {type(idades)}")  # vendo o tipo da variável com type()
print(f"A len da variável é: {len(idades)}")  # vendo o tamanho com len()
print("-----------------------------------")

print(idades[1])  # fatiamento, printando o valor da posição 1
idades.append(15)  # adicionando valor ao final da lista com append()
print(idades)
print(idades[4])  # fatiamento, printando o valor da posição 4
print("-----------------------------------")

for n in idades:
    print(f'Printando for nº{n}')  # loop for para printar todos os valores  da lista de maneira formatada
print("-----------------------------------")

idades.remove(30)  # removendo o valor 30 da lista com remove()
print(idades)
idades.extend([11, 5])  # agrega / concatena / extende a lista [11, 5] a lista ja existente
print(idades)
print("-----------------------------------")

idades_ano_que_vem = []
for idade in idades:
    idades_ano_que_vem.append(idade + 1)  # adicionou 1 ano em cada idade da lista 'idades' criando uma nova lista 'idades_ano_que_vem'
print(idades_ano_que_vem)

idades_ano_que_vem_2 = [(idade + 1) for idade in idades]  # mesma coisa, porém com List Comprehension
print(idades_ano_que_vem_2)
print("-----------------------------------")

idades_ano_que_vem_3 = [(idade) for idade in idades if idade > 21]  # adicionou em uma lista nova apenas as idades 'maiores que 21'
print(idades_ano_que_vem_3)