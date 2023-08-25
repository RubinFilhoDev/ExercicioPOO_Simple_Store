from produto import Produto
from carrinho import Carrinho


def exibir_menu():
    print("Bem-vindo à Lojinha de Suplementos!")
    print("1. Botar no carrinho")
    print("2. Tirar do carrinho")
    print("3. Total do carrinho")
    print("4. Listar o Carrinho")

def main():
    carrinho = Carrinho()
    produtos_disponiveis = [
        Produto("Whey Protein", 100.0),
        Produto("Creatina", 30.0),
        Produto("BCAA", 25.0),
        Produto("Barra de Proteína", 10.0)
    ]

    def show_cart_iten():
        itens_do_carrinho = carrinho.get_carrinho()
        for i, produto in enumerate(itens_do_carrinho, start=1):
            print(i, produto.nome, produto.preco)


    while True:
        opcao = exibir_menu()
        opcao_escolhida = input("Selecione uma opção: ")


        if opcao_escolhida == str(1):
            for i, produto in enumerate(produtos_disponiveis):
                print(i + 1, produto.nome, produto.preco)
            produto_escolhido = input("Escolha um produto: ")
        
            produto_encontrado = produtos_disponiveis[int(produto_escolhido) - 1]
            print(produto_encontrado.nome, produto_encontrado.preco)

            carrinho.adicionar_item(produto_encontrado)

        if opcao_escolhida == str(2):
            show_cart_iten()
            produto_idx = input("Escolha um produto para remover: ")
            carrinho.remove_by_index(int(produto_idx) - 1)

        if opcao_escolhida == str(3):
            show_cart_iten()
            print("Total: " + str(carrinho.calcular_total()))

        
        if opcao_escolhida == str(4):
            show_cart_iten()


if __name__ == "__main__":
    main()
