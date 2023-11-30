# SRP com classes

class Estoquista:

    def baixar_estoque(self):
        pass


class Faturista:

    def faturar(self):
        pass

    def calcular_icms(self):
        pass

    def calcular_ipi(self):
        pass


class Vendedora:  # VendaService

    def __init__(self, estoquista: Estoquista, faturista: Faturista):
        self.estoquista = estoquista
        self.faturista = faturista

    def vender(self):
        # A lógica da venda
        # Comunicar com o estoquista
        # Comunicar com o faturista
        self.estoquista.baixar_estoque()
        self.faturista.faturar()


# SSR com funções

def calcula_impostos():
    pass
    # ruim


def calcula_ipi():
    pass
    # melhor


def calcula_icms():
    pass
    # melhor
