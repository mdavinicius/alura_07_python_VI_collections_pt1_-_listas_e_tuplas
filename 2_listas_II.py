class ContaCorrente:
    def __init__(self, codigo):  # para iniciar a classe ContaCorrente é necessário inserir um código de conta
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):  # função para depositar um valor na conta
        self.saldo += valor

    def __str__(self):
        return "[>> Código {} | Saldo {} <<]".format(self.codigo, self.saldo)  # print formatado da conta e saldo com __str__

    def deposita_para_todas(contas):  # deposita 100 em cada uma das contas em uma lista de contas
        for conta in contas:
            conta.deposita(100)


conta_do_vini = ContaCorrente(15)  # cria conta nº 15
print(conta_do_vini)
conta_do_vini.deposita(500)  # deposita 500 na conta
print(conta_do_vini)
print("-----------------------------------")

conta_da_dani = ContaCorrente(4875)  # cria conta 4875
conta_da_dani.deposita(1000)  # deposita 1000 na conta
print(conta_da_dani)
print("-----------------------------------")

contas = [conta_do_vini, conta_da_dani]  # uma lista de contas
print(contas)
for conta in contas:  # printando cada uma das contas da listas
    print(conta)
print("-----------------------------------")

contas2 = [conta_do_vini, conta_da_dani, conta_do_vini]  # agora temos uma conta repetida na lista
print(contas2[0])
conta_do_vini.deposita(1000)  # se depositamos no objeto, vai replicar o saldo em ambas as contas da lista
for conta in contas2:
    print(conta)
print("-----------------------------------")

contas2[2].deposita(1000)  # idem aqui, apesar de acessar a conta '3', o valor é replicado na conta '1' da lista
print(conta_do_vini)
for conta in contas2:
    print(conta)
print("-----------------------------------")

conta_do_vini = ContaCorrente(15)
conta_do_vini.deposita(900)
conta_da_dani = ContaCorrente(4875)
conta_da_dani.deposita(1000)
contas = [conta_do_vini, conta_da_dani]
print(contas[0], contas[1])
ContaCorrente.deposita_para_todas(contas)  # usando a função que faz um depósito para todas as contas da lista
print(contas[0], contas[1])