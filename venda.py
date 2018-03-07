

promos = []


def promocao(nome_funcao):
    promos.append(nome_funcao)
    return nome_funcao

@promocao
def fidelidade(pedido):
    return pedido.total() * 0.05 if pedido.cliente == 'Zenir' else 0

@promocao
def muitos_itens(pedido):
    desconto = 0
    for item in pedido.carrinho:
        if item.quantidade >= 20:
            desconto += item.total() * .1
    return desconto

def melhor_promocao(order):
    return max(promo(order) for promo in promos) or 0


class Item(object):

    def __init__(self, produto, quantidade, preco):
        self.produto = produto
        self.quantidade = quantidade
        self.preco = preco

    def total(self):
        return self.preco * self.quantidade

class Pedido(object):

    def __init__(self, cliente, carrinho, promocao=None):
        self.cliente = cliente
        self.carrinho = list(carrinho)
        self.promocao = promocao

    def total_pagar(self):
        discount = melhor_promocao(self)
        return self.total() - discount

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.carrinho)
        return self.__total
