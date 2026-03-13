# 32. Receba um número inteiro. Calcule e mostre o seu fatorial.

# DECLARAÇÃO DE VARIÁVEIS
num: int = 0
fact: int = 1

# INICIO
num = int(input(">>>"))
for n in range(num, 0, -1):
    fact *= n
print(fact)
# FIM
