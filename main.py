from models.produto import Produto
from services.estoque import Estoque

print("=" * 50)
print(" " * 15, "Sistema de Estoque")
print("=" * 50)
menu = """
1. Adicionar Produto
2. Listar Produtos
3. Buscar Produto
4. Remover Produto
5. Atualizar Produto
6. Sair 
"""

estoque = Estoque()

while True:
    print(menu)
    opcao = input("Escolha uma opção:")

    if opcao == "1":
        nome = input("Nome do produto: ")
        sku = input("SKU do produto: ")
        preco = float(input("Preço do produto: "))
        quantidade = int(input("Quantidade do produto: "))
        produto = Produto(nome, sku, preco, quantidade)
        estoque.adicionar_produto(produto)
        print("Produto adicionado com sucesso!")

    elif opcao == "2":
        produtos = estoque.listar_produtos()
        for produto in produtos:
            print(produto)
        if not produtos:
            print("Nenhum produto cadastrado.")

    elif opcao == "3":
        sku = input("Digite o SKU do produto que deseja buscar: ")
        produto = estoque.buscar_produto(sku)
        if produto:
            print(produto)
        else:
            print("Produto não encontrado.")

    elif opcao == "4":
        sku = input("Digite o SKU do produto que deseja remover: ")
        estoque.remover_produto(sku)
        print("Produto removido com sucesso!")

    elif opcao == "5":
        sku = input("Digite o SKU do produto que deseja atualizar: ")
        produto = estoque.buscar_produto(sku)
        if produto:
            nome = input(f"Novo nome (atual: {produto.nome}): ") or produto.nome
            preco = input(f"Novo preço (atual: {produto.preco}): ") or produto.preco
            quantidade = input(f"Nova quantidade (atual: {produto.quantidade}): ") or produto.quantidade
            produto.nome = nome
            produto.preco = float(preco)
            produto.quantidade = int(quantidade)
            print("Produto atualizado com sucesso!")
        else:
            print("Produto não encontrado.")

    elif opcao == "6":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida. Tente novamente.")