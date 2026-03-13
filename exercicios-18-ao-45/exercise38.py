# 38. Receba 100 números inteiros reais. Verifique e mostre o maior e o menor valor. Obs.: somente valores positivos.

# DECLARAÇÃO DE VARIÁVEIS
count: int = 0
num: int = 0
bigger: int = 0
smaller: int = 0

# INICIO
while (count < 5):
    num = int(input(">>>"))
    if (num > 0):
        if (count == 0):
            bigger = smaller = num
        else:
            if (num > bigger):
                bigger = num
            elif (num < smaller):
                smaller = num
        count += 1

print(f"Smaller: {smaller} - Bigger: {bigger}")
# FIM
