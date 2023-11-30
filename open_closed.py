# OPP Open Closed Principle

class CalculaImposto:

    def __init__(self, valor) -> None:
        self.valor = valor

    def calcular(self):
        return self.valor * 1.2


class CalculaImpostoDeValoresMaioresQueCem(CalculaImposto):

    def calcular(self):
        if self.valor > 100:
            return self.valor * 1.3
        return super().calcular()


class CalculaImpostoDeValoresMaioresQueCem2:

    def __init__(self, valor, calcula_imposto: CalculaImposto) -> None:
        self.valor = valor
        self.calcula_imposto = calcula_imposto

    def calcular(self):
        if self.valor > 100:
            return self.valor * 1.3
        return self.calcula_imposto.calcular()


calcular_imposto = CalculaImposto(100)
assert calcular_imposto.calcular() == 120
print(calcular_imposto.calcular())

calcular_imposto = CalculaImpostoDeValoresMaioresQueCem(100)
assert calcular_imposto.calcular() == 120
print(calcular_imposto.calcular())

calcular_imposto = CalculaImpostoDeValoresMaioresQueCem(101)
assert calcular_imposto.calcular() == 131.30
print(calcular_imposto.calcular())


valor = 101
calcular_imposto = CalculaImposto(valor)
calcular_imposto_2 = CalculaImpostoDeValoresMaioresQueCem2(valor, calcular_imposto)

print("-------")
print(calcular_imposto_2.calcular())