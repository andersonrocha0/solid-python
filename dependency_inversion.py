from abc import ABC, abstractmethod


class EstoqueContrato(ABC):

    @abstractmethod
    def baixar_estoque(self, id_produto, quantidade):
        pass


class Estoque(EstoqueContrato):

    def baixar_estoque(self, id_produto, quantidade):
        print(f"Baixando o estoque do produto {id_produto} com a quantidade {quantidade}...")


class EstoqueComNovasRegras(EstoqueContrato):

    def baixar_estoque(self, id_produto, quantidade):
        print(
            f"Baixando o estoque com a nova regra de negócio para o produto {id_produto} com a quantidade {quantidade}...")


class Vendedora:
    estoque_contrato: EstoqueContrato

    def __init__(self, estoque_contrato: EstoqueContrato) -> None:
        super().__init__()
        self.estoque_contrato = estoque_contrato

    def vender(self):
        print("Vendendo...")

        self.estoque_contrato.baixar_estoque(123, 10)


estoque_contrato: EstoqueContrato = EstoqueComNovasRegras()

vendedora = Vendedora(estoque_contrato)
vendedora.vender()

estoque_contrato2: EstoqueContrato = Estoque()

vendedora2 = Vendedora(estoque_contrato2)
vendedora2.vender()
