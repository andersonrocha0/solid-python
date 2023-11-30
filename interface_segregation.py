from abc import ABC, abstractmethod


class CobradoraContrato(ABC):

    @abstractmethod
    def cobrar(self):
        pass


class FaturistaContrato(ABC):

    @abstractmethod
    def faturar(self):
        pass


class VendedoraContrato(ABC):

    @abstractmethod
    def aplicar_desconto_na_venda(self):
        pass

    @abstractmethod
    def vender(self):
        pass


class Vendora(VendedoraContrato):

    def vender(self):
        print("Estou vendendo alguma coisa.")


    def aplicar_desconto_na_venda(self):
        print("Aplicando o desconto.")



class Cobradora(CobradoraContrato):

    def cobrar(self):
        print("Estou cobrando alguma coisa.")


vendedora = Vendora()
vendedora.vender()


cobradora = Cobradora()
cobradora.cobrar()
