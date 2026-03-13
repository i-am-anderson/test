# 40. Receba 2 números inteiros. Verifique e mostre todos os números primos existentes entre eles.

# DECLARAÇÃO DE VARIÁVEIS
a: int = 0
b: int = 0
sqrt: int = 0
ehPrimo: bool = True

# INICIO
while ((a <= 0 and b <= 0) or a >= b):
    a = int(input(">>>"))
    b = int(input(">>>"))
for n in range(a, b, 1):
    if (n > 2):
        ehPrimo = True
        sqrt = round(n ** 0.5)
        for m in range(2, sqrt + 1, 1):
            if (n % m == 0):
                ehPrimo = False
                break
        if ehPrimo:
            print(n, ",")
# FIM
