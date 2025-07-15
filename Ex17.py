area = float(input("Digite o tamanho da área a ser pintada (m²): "))

# Cálculo de litros necessários
litros_necessarios = area / 6

# Situação 1: Apenas latas de 18 litros
latas18 = litros_necessarios / 18
preco_latas18 = latas18 * 80

print(f"\nSituação 1 - Apenas latas de 18 litros:")
print(f"Quantidade de latas: {latas18}")
print(f"Preço total: R$ {preco_latas18:.2f}")

# Situação 2: Apenas galões de 3,6 litros
galoes36 = litros_necessarios / 3.6
preco_galoes36 = galoes36 * 25

print(f"\nSituação 2 - Apenas galões de 3,6 litros:")
print(f"Quantidade de galões: {galoes36}")
print(f"Preço total: R$ {preco_galoes36:.2f}")