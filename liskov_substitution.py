# LSP

class CalculaDesconto:

    def __init__(self, valor) -> None:
        self.valor = valor

    def aplicar_desconto(self, desconto):
        if desconto <= 0 or desconto > 100:
            return self.valor

        return self.valor * (100 - desconto) / 100


class CalculaDescontoEspecial(CalculaDesconto):

    def aplicar_desconto(self, desconto):
        if 0 < desconto <= 100:
            percentual = 100 - desconto
            return self.valor * percentual / 100
        return self.valor


calcula_desconto = CalculaDescontoEspecial(50)
print(calcula_desconto.aplicar_desconto(10))
