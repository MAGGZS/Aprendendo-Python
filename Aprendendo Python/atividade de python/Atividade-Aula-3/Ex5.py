cotacao = float(input("Digite a cotação do dólar (R$): "))
valor_dolar = float(input("Digite o valor em dólares: "))
valor_real = valor_dolar * cotacao
print(f"Valor em Reais: R$ {valor_real:.2f}")