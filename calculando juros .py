from datetime import datetime

valor_da_divida = float(input("Digite o valor da dívida: "))



data_vencimento = input("Digite a data de vencimento (dd/mm/aaaa): ")

data_vencimento = datetime.strptime(
    data_vencimento,
    "%d/%m/%Y"
)

data_hoje = datetime.today()

print("Vencimento:", data_vencimento)
print("Hoje:", data_hoje)

dias_atraso = data_hoje - data_vencimento

print("Dias de atraso:", dias_atraso.days)

juros = dias_atraso.days * 0.025
valor_total = valor_da_divida + (valor_da_divida * juros)

print(f"R$juros {juros:.3f}")
print("Valor total:", valor_total)