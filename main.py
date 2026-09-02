import os

from models.produto import Produto, Base
from services.estoque_service import Estoque
from database.connection import engine


# Cria as tabelas do banco caso ainda não existam
Base.metadata.create_all(engine)


def limpar_tela():
    os.system("clear")


def mostrar_cabecalho():
    print("╔══════════════════════════════════════════════════════╗")
    print("║                  SISTEMA DE ESTOQUE                  ║")
    print("║                     v1.0.0                           ║")
    print("╠══════════════════════════════════════════════════════╣")
    print("║                                                      ║")


def mostrar_menu():
    print("║  [1]  Adicionar produto                              ║")
    print("║  [2]  Listar produtos                                ║")
    print("║  [3]  Buscar produto                                 ║")
    print("║  [4]  Atualizar produto                              ║")
    print("║  [5]  Remover produto                                ║")
    print("║  [6]  Sair                                           ║")
    print("║                                                      ║")
    print("╚══════════════════════════════════════════════════════╝")


estoque = Estoque()


while True:

    limpar_tela()

    mostrar_cabecalho()
    mostrar_menu()

    opcao = input("\n  ➜ Escolha uma opção: ")

    if opcao == "1":

        limpar_tela()

        print("╔══════════════════════════════════════════════════════╗")
        print("║                  ADICIONAR PRODUTO                   ║")
        print("╚══════════════════════════════════════════════════════╝")

        nome = input("\nNome do produto: ")
        sku = input("SKU do produto: ")
        preco = float(input("Preço do produto: "))
        quantidade = int(input("Quantidade do produto: "))

        produto = Produto(nome, sku, preco, quantidade)

        estoque.adicionar_produto(produto)

        print("\n✓ Produto adicionado com sucesso!")

        input("\nPressione ENTER para continuar...")


    elif opcao == "2":

        limpar_tela()

        print("╔══════════════════════════════════════════════════════╗")
        print("║                  PRODUTOS CADASTRADOS                ║")
        print("╚══════════════════════════════════════════════════════╝")

        produtos = estoque.listar_produtos()

        if produtos:

            print()

            for produto in produtos:
                print(f"  ID: {produto.id}")
                print(f"  Produto: {produto.nome}")
                print(f"  SKU: {produto.sku}")
                print(f"  Preço: R$ {produto.preco:.2f}")
                print(f"  Estoque: {produto.quantidade} unidades")
                print()
                print("  ────────────────────────────────────────────────────")
                print()

        else:
            print("\n  Nenhum produto cadastrado.")

        input("\nPressione ENTER para continuar...")


    elif opcao == "3":

        limpar_tela()

        print("╔══════════════════════════════════════════════════════╗")
        print("║                    BUSCAR PRODUTO                    ║")
        print("╚══════════════════════════════════════════════════════╝")

        sku = input("\nDigite o SKU do produto: ")

        produto = estoque.buscar_produto(sku)

        if produto:

            print("\n  Produto encontrado!")
            print()
            print(f"  ID: {produto.id}")
            print(f"  Produto: {produto.nome}")
            print(f"  SKU: {produto.sku}")
            print(f"  Preço: R$ {produto.preco:.2f}")
            print(f"  Estoque: {produto.quantidade} unidades")

        else:
            print("\n  ✗ Produto não encontrado.")

        input("\nPressione ENTER para continuar...")


    elif opcao == "4":

        limpar_tela()

        print("╔══════════════════════════════════════════════════════╗")
        print("║                  ATUALIZAR PRODUTO                   ║")
        print("╚══════════════════════════════════════════════════════╝")

        sku = input("\nDigite o SKU do produto: ")

        produto = estoque.buscar_produto(sku)

        if produto:

            print("\n  Produto encontrado!")
            print("  Pressione ENTER para manter o valor atual.\n")

            nome = input(
                f"Novo nome (atual: {produto.nome}): "
            ) or produto.nome

            preco = input(
                f"Novo preço (atual: {produto.preco:.2f}): "
            ) or produto.preco

            quantidade = input(
                f"Nova quantidade (atual: {produto.quantidade}): "
            ) or produto.quantidade

            produto_atualizado = estoque.atualizar_produto(
                sku,
                nome,
                float(preco),
                int(quantidade)
            )

            if produto_atualizado:
                print("\n✓ Produto atualizado com sucesso!")
            else:
                print("\n✗ Não foi possível atualizar o produto.")

        else:
            print("\n  ✗ Produto não encontrado.")

        input("\nPressione ENTER para continuar...")


    elif opcao == "5":

        limpar_tela()

        print("╔══════════════════════════════════════════════════════╗")
        print("║                   REMOVER PRODUTO                    ║")
        print("╚══════════════════════════════════════════════════════╝")

        sku = input("\nDigite o SKU do produto: ")

        produto = estoque.buscar_produto(sku)

        if produto:

            print("\n  Produto encontrado:")
            print(f"  Produto: {produto.nome}")
            print(f"  SKU: {produto.sku}")
            print(f"  Preço: R$ {produto.preco:.2f}")
            print(f"  Estoque: {produto.quantidade} unidades")

            confirmacao = input(
                "\n  Deseja realmente remover este produto? (s/n): "
            ).lower()

            if confirmacao == "s":

                removido = estoque.remover_produto(sku)

                if removido:
                    print("\n✓ Produto removido com sucesso!")
                else:
                    print("\n✗ Não foi possível remover o produto.")

            else:
                print("\n  Operação cancelada.")

        else:
            print("\n  ✗ Produto não encontrado.")

        input("\nPressione ENTER para continuar...")


    elif opcao == "6":

        limpar_tela()

        print("╔══════════════════════════════════════════════════════╗")
        print("║                                                      ║")
        print("║              Encerrando o sistema...                 ║")
        print("║                                                      ║")
        print("╚══════════════════════════════════════════════════════╝")

        break


    else:

        print("\n  ✗ Opção inválida. Tente novamente.")

        input("\nPressione ENTER para continuar...")