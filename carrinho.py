class Carrinho:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, produto):
        self.itens.append(produto)

    def remover_item(self, produto):
        self.itens.remove(produto)

    def remove_by_index(self, idx):
        self.itens.pop(idx)

    def calcular_total(self):
        total = sum(item.preco for item in self.itens)
        return total

    def get_carrinho(self):
        return self.itens