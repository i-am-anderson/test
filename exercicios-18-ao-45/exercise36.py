# 36. Receba um número N. Calcule e mostre a série 1 + 1/1! + 1/2! + ... + 1/N!

# DECLARAÇÃO DE VARIÁVEIS
n: int = 0
fact: int = 0
sum_: float = 0

# INICIO
while (n <= 0):
    n = int(input(">>>"))
for i in range(1, n+1, 1):
    fact = 1
    for f in range(1, i + 1, 1):
        fact *= f
    sum_ += (1 / fact)
    print(f"{1}/{i}!")
    if (i < n):
        print(" + ")
    else:
        print(" = ")
print(f"{sum_:,.2f}")
# FIM
