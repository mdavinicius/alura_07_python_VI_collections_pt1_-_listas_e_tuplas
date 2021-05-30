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


conta1 = Conta(17)  # criando uma conta
print(conta1)
conta1.deposita(1000)  # depositando 1000
print(conta1)
print("-----------------------------------")

conta2 = Conta(17)  # criando outra conta
print(conta2)
print("-----------------------------------")

# Criar uma função que faça a verificação de igualdade entre as contas com __eq__
print(conta1 == conta2)
print("-----------------------------------")

print(isinstance(conta1, Conta))  # isinstance verifica se o objeto faz parte da hierarquia
print("-----------------------------------")