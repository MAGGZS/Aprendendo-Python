a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))

print("==================================")
print("A 1° equação em questão é a ", a," + ",b, " x ", c, " = ??")
confirm = str(input("Quer ver resolução?? "))

if confirm == "sim" or "yes" or "s" or "y":
    print("o resultado desse calculo é de ", a+b*c)
    print("=======================================")

else:
    print("Fim dos calculos")

print("A 2° equação em questão é a ", a," / ",b, " = ??")
confirm = str(input("Quer ver resolução?? "))

if confirm == "sim" or "yes" or "s" or "y":
    print("o resultado desse calculo é de ", a/b)
    print("=======================================")

else:
    print("Fim dos calculos")


    
