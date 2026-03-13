# 33. Receba um número. Calcule e mostre a série 1 + 1/2 + 1/3 + ... + 1/N.

# DECLARAÇÃO DE VARIÁVEIS
num: int = 0

# INICIO
while (num <= 0):
    num = int(input(">>>"))
for x in range(1, num):
    if (x != 1):
        print(f"1/{x}")
    else:
        print("1")
    if (x < num - 1):
        print(" + ")
# FIM
