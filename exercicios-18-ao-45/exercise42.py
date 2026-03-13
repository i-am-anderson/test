# 42. Calcule e mostre a série 1 + 2/3 + 3/5 + ... + 50/99

# DECLARAÇÃO DE VARIÁVEIS
rng: int = 51
y: int = 1


# INICIO
for x in range(1, rng):
    if (x != y):
        print(f"{x}/{y}")
    else:
        print(f"{x}")
    y += 2
    if (x < rng - 1):
        print(" + ")
# FIM
