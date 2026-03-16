import math
graus = float(input("Digite um ângulo em graus: "))
radianos = math.radians(graus)
print(f"Radianos: {radianos:.4f}")
print(f"Seno: {math.sin(radianos):.4f}")
print(f"Cosseno: {math.cos(radianos):.4f}")
print(f"Tangente: {math.tan(radianos):.4f}")