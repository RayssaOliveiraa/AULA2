import random


class Conta():
    def __init__(self, numConta):
        self.numero = numConta
        self.saldo = 0

    def deposite(self, valor):
        # devem descontar 0,001% do que foi depositado.
        self.saldo = self.saldo + (valor - (valor*0.001))

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo = self.saldo - valor
            return True
        else:
            return False


class Poupanca(Conta):

    def render(self):
        self.saldo = self.saldo + self.saldo*0.01


class ContaBonificada(Conta):
    
    def renderBonus(self, valor):
        # acumula um bônus equivalente a 0,01% do valor depositado
        self.saldo = self.saldo + ((valor - (valor*0.001)) * 0.0001)


class Banco():
    def __init__(self, nome):
        self.nome = nome
        self.contas = []

    def getNome(self):
        return self.nome

    def criarConta(self):
        num = random.randint(0, 1000)
        c = Conta(num)
        self.contas.append(c)
        return num

    def criarPoupanca(self):
        num = random.randint(0, 1000)
        p = Poupanca(num)
        self.contas.append(p)
        return num

    def criarContaBonificada(self):
        num = random.randint(0, 1000)
        cb = ContaBonificada(num)
        self.contas.append(cb)
        return num

    def consultaSaldo(self, numConta):
        for conta in self.contas:
            if conta.numero == numConta:
                return conta.saldo
        return -1

    def depositar(self, numConta, valor):
        for conta in self.contas:
            if conta.numero == numConta and isinstance(conta, ContaBonificada):
                conta.deposite(valor)
                conta.renderBonus(valor)
            elif conta.numero == numConta:
                conta.deposite(valor)
            

    def sacar(self, numConta, valor):
        for conta in self.contas:
            if conta.numero == numConta:
                return conta.sacar(valor)

    def renderPoupanca(self, numConta):
        for i in self.contas:
            if i.numero == numConta and isinstance(i, Poupanca):
                i.render()
                return True
        return False
