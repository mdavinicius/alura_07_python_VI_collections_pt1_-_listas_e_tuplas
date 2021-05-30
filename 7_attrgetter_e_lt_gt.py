from functools import total_ordering
# Ao chamar o 'total_ordering' e construir 2 métodos entre (eq + lt, le, gt ou ge), a Classe terá terá possibilidade
# de realizar todas as outras operações sem precisar declara-las.

@total_ordering
class Conta:
    def __init__(self, codigo):  # para iniciar a classe Conta é necessário inserir um código de conta
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, saldo):  # função para depositar um valor na conta
        self._saldo += saldo

    def __str__(self):  # print formatado da conta e saldo com __str__
        return f'[>>Codigo {self._codigo} Saldo {self._saldo} <<]'

    def __eq__(self, other):  # permite comparar igualdade entre objetos com __eq__
        return self._codigo == other._codigo

    def __lt__(self, other):  # permite comparar se um objeto é menor que o outro com __lt__
        if self._saldo != other._saldo:
            return self._saldo < other._saldo

        return self._codigo < other._codigo


# criar 3 Contas (17 / 3 / 133), depositar (500 / 1000/ 510) e criar uma lista de contas
conta_guilherme = Conta(17)
conta_guilherme.deposita(500)

conta_daniela = Conta(3)
conta_daniela.deposita(1000)

conta_paulo = Conta(133)
conta_paulo.deposita(510)

contas = [conta_guilherme, conta_daniela, conta_paulo]
print(contas)  # sai a identificação do objeto na ordem que foram adicionados
print("-----------------------------------")

# print(sorted(contas)) # dará erro, pois não tem como saber qual conta é menor do que outra pois cada objeto armazena conta e saldo

def extrai_saldo(conta):  # criando uma função para tornar o saldo como um meio de ordenar as contas
    return conta._saldo

for conta in sorted(contas, key=extrai_saldo):  # ordenou, mas não é uma boa prática pois puxamos um atributo privado
    print(conta)
print("-----------------------------------")

from operator import attrgetter # O 'attrgetter' é uma forma de puxar um 'atributo' de uma Classe, sem precisar criar uma função para acessá-lo

for conta in sorted(contas, key=attrgetter("_saldo")):  # conseguimos puxar sem precisar criar uma função, mas continuamos usando um atributo privado
    print(conta)
print("-----------------------------------")

print(conta_guilherme < conta_daniela)  # agora com a função __lt__ é possível compará-los
print(conta_guilherme > conta_daniela)  # o inverso também é possível, sem precisar adicionar a função __gt__
print("-----------------------------------")

for conta in sorted(contas):  # agora também é possível ordernar a lista pelo saldo
    print(conta)
print("-----------------------------------")

for conta in sorted(contas, reverse=True):  # e também do maior para o menor
    print(conta)
print("-----------------------------------")

# E se as contas tivessem o mesmo saldo? Como ordernar por código então?
# Update no __lt__ adicionando um if, e no else, ao invés de olhar para _saldo, olhamos para _codigo

conta_guilherme = Conta(17)
conta_guilherme.deposita(500)

conta_daniela = Conta(3)
conta_daniela.deposita(500)

conta_paulo = Conta(13)
conta_paulo.deposita(500)

contas = [conta_guilherme, conta_daniela, conta_paulo]

print("Ordenando contas com saldos iguais pelo código da conta")
for conta in sorted(contas):
    print(conta)
print("-----------------------------------")

# from functools import total_ordering
# a partir de agora podemos fazer todas as operações > < <= >= == declarando apenas __eq__ + uma, graças ao total_ordering

print(conta_guilherme <= conta_daniela)
print(conta_guilherme == conta_daniela)
print(conta_guilherme >= conta_daniela)
# Como os saldos são iguais, a 'conta_guilherme' tem o código MAIOR do que a 'conta_daniela'
