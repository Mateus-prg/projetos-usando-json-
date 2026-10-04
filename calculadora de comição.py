import json

with open("vendas.json", "r") as arquivo:
    dados = json.load(arquivo)

def calcular_comissao(valor):
        if valor >= 500:
            return valor * 0.05
        elif valor > 100:
            return valor * 0.01
        else:
            return 0
totais = {}

  
for venda in dados["vendas"]:
    vendedor = venda["vendedor"]
    valor = venda["valor"]

    comissao = calcular_comissao(valor)
    totais[vendedor] = totais.get(vendedor, 0) + comissao

for vendedor, total in totais.items():
    print(f"Vendedor: {vendedor}")
    print(f"Total de Comissões: R$ {total:.2f}")
    print("-" * 30)