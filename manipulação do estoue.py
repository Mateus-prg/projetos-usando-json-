import json

with open("estoque.json", "r") as arquivo:
    dados = json.load(arquivo)

id_movimentacao = 1

while True:
    print("\n==== controle de estoque ====")
    print("1- listar produtos")
    print("2-fazer movimentação")
    print("3- sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("\n==== produtos ====")
        for produto in dados["estoque"]:
            print(
                f"código:{produto['codigoproduto']}|"
                f"produto:{produto['descricaoproduto']}|"
                f"estoque:{produto['estoque']}|"
            )

    elif opcao == "2":
        print("\n==== movimentação ====")
        codigo = input("Digite o código do produto: ")
        produto_encontrado = None

        for produto in dados["estoque"]:
            if produto["codigoproduto"] == codigo:
                produto_encontrado = produto
                break

        if produto_encontrado is None:
            print("Produto não encontrado.")
            continue

        print(f"\nproduto:{produto_encontrado['descricaoproduto']}|")
        print(f"estoque atual:{produto_encontrado['estoque']}|")

        print("\n1 - entrada")
        print("2 - saída")

        tipo = input("digite o tipo de movimentação: ")
        quantidade = int(input("Digite a quantidade: "))

        if tipo == "1":
            produto_encontrado["estoque"] += quantidade
            descricao = "entrada de mercadoria"
            print("\n movimentação realizada com sucesso!")
        elif tipo == "2":
            if quantidade <= produto_encontrado["estoque"]:
                produto_encontrado["estoque"] -= quantidade
                descricao = "saída de mercadoria"
                print("\n movimentação realizada com sucesso!")
            else:
                print("\n quantidade insuficiente em estoque!")
                continue
        else:
            print("\nTipo de movimentação inválido.")
            continue

        print("\n=== movimentação ===")
        print(f"ID: {id_movimentacao}")
        print(f"Descrição: {descricao}")
        print(f"Produto: {produto_encontrado['descricaoproduto']}")
        print(f"Estoque final: {produto_encontrado['estoque']}")

        id_movimentacao += 1

    elif opcao == "3":
        print("\nPrograma encerrado.")
        break

    else:
        print("\nOpção inválida.")

