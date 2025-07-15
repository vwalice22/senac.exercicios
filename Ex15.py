valor_hora = float(input('Quanto você ganha por hora?\n'))
total_hora = int(input('Quantas horas você trabalha por mês?\n'))

salario_bruto = valor_hora*total_hora
irrf = salario_bruto*0.11
inss = salario_bruto*0.08
sindicato = salario_bruto*0.05

print(f'O valor do salário bruto é: {salario_bruto} reais')
print(f'Desconto do INSS: R${inss}')
print(f'Desconto do sindicato: R${sindicato}')
print(f'Salário líquido: R${salario_bruto - (inss + sindicato + irrf)}')