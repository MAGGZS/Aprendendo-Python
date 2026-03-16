anos = int(input("Digite sua idade em anos: "))
meses = int(input("Digite os meses restantes: "))
dias = int(input("Digite os dias restantes: "))
total_dias = (anos * 365) + (meses * 30) + dias
print(f"Sua idade em dias é: {total_dias} dias")