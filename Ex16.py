area = float(input("Digite o tamanho da área a ser pintada (m²): "))
litros_necessarios = area / 3
latas = litros_necessarios / 18
preco_total = latas * 80

print(f"Quantidade de latas de tinta: {latas}")
print(f"Preço total: R$ {preco_total:.2f}")