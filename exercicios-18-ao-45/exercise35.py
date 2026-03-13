# 35. Receba 2 números inteiros, verifique qual o maior entre eles. Calcule e mostre o resultado da somatória dos números ímpares entre esses valores.

# DECLARAÇÃO DE VARIÁVEIS
x: int = 0
y: int = 0
greater: int = 0
lower: int = 0
sum_: int = 0

# INICIO
while (x == y):
    x = int(input(">>>"))
    y = int(input(">>>"))
if (x > y):
    greater = x
    lower = y
else:
    greater = y
    lower = x
for i in range(lower + 1, greater, 1):
    if (i % 2 != 0):
        sum_ += i

print(f"Greater: {greater}")
print(f"Sum: {sum_}")
# FIM
