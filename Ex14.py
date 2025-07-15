peso = float(input("Digite o peso dos peixes (kg): "))
limite = 50
excesso = (peso - limite)
multa = excesso * 4.00

print(f"Peso informado: {peso} kg")
print(f"Excesso: {excesso} kg")
print(f"Multa a pagar: R$ {multa:.2f}")