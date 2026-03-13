# 45. Calcule e mostre a série 1 – 2/4 + 3/9 – 4/16 + 5/25 - ... + 15/225

# DECLARAÇÃO DE VARIÁVEIS
sum_: float = 0

# INICIO
for x in range(1, 16):
    if (x != 1):
        print(f"{x}/{x ** 2}")
    else:
        print("1")

    if (x % 2 == 0 and (x < 16 - 1)):
        sum_ -= (x/x ** 2)
        print(" + ")
    elif (x % 2 != 0 and (x < 16 - 1)):
        sum_ += (x/x ** 2)
        print(" - ")
    else:
        sum_ += (x/x ** 2)
        print(" = ")
print(sum_)
# FIM
