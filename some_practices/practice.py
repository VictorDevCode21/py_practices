n = [7, 1, 5, 3, 6, 4]

num_mayor = 0
num_menor = 0

min = float("inf")
max = 0

for i in range(0, len(n)):
    print(f"Bucle nro: {i}")
    if n[i] < min:
        min = n[i]
    elif n[i] > max:
        max = n[i]

dia_de_compra = n.index(min)
dia_de_venta = n.index(max)

print(f"\nel max es: {max} y el min es: {min}\n")
print(
    f"El dia de compra es dia: {dia_de_compra + 1} y el dia de venta es dia {dia_de_venta + 1}"
)
