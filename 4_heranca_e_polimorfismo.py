from abc import ABCMeta, abstractmethod
# com uma classe contendo 'metaclass=ABCMeta' e uma função @abstractmethod, nós fazemos com que essa função
# seja obrigatória de existir em qualquer classe filha que puxar essa herança

class Conta(metaclass=ABCMeta):
    def __init__(self, codigo):  # para iniciar a classe Conta é necessário inserir um código de conta
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):  # função para depositar um valor na conta
        self._saldo += valor

    @abstractmethod
    def passa_o_mes(self):  # método obrigatório na herança com @abstractmethod
        pass

    def __str__(self):
        return "[>> Codigo {}, Saldo {} <<]".format(self._codigo, self._saldo)  # print formatado da conta e saldo com __str__

class ContaCorrente(Conta):
    def passa_o_mes(self):  # ao passar o mês na ContaCorrente, o saldo da conta é diminuido em 2
        self._saldo -= 2

class ContaPoupanca(Conta):
    def passa_o_mes(self):  # ao passar o mês na ContaPoupança, o saldo da conta aumenta 1% e diminui em 3
        self._saldo *= 1.01
        self._saldo -= 3

class ContaInvestimento(Conta):
    pass  # conta em branco apenas para testar a necessidade da funão passa_o_mes() por conta do abstractmethod

# Testes com conta 16 e 17, deposita 1000 em e cada e em uma chama ContaCorrente em outra ContaPoupanca e passa_o_mes em ambas
conta16 = ContaCorrente(16)
conta16.deposita(1000)
print(conta16)
conta16.passa_o_mes()
print(conta16)

conta17 = ContaPoupanca(17)
conta17.deposita(1000)
print(conta17)
conta17.passa_o_mes()
print(conta17)
print("-----------------------------------")

# Lista com as 2 conta e faz um passa_o_mes para ambas de uma vez
conta16 = ContaCorrente(16)
conta17 = ContaPoupanca(17)
conta16.deposita(1000), conta17.deposita(1000)
contas = [conta16, conta17]

for conta in contas:
    conta.passa_o_mes()
    print(conta)
print("-----------------------------------")

# Utilizar o ABCMethos e abstractmethod para impedir a criação de uma classe sem um método específico da classe mãe
conta1 = ContaInvestimento(1)