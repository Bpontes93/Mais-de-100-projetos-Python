# Desenvolva uma lógica que leia o peso e altura de uma pessoa. Calcule o IMC e apresente:
# Abaixo de 18.5: Abaixo do peso | Entre 18.5 e 25: Peso ideal | 25 até 30: Sobrepeso
# 30 até 40: Obesidade | Acima de 40: Obesidade mórbida.

peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é sua altura? (m) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:0.1f}'.format(imc))

if imc < 18.5:
	print('ABAIXO DO PESO')

elif 18.5 <= imc < 25:
	print('PESO IDEAL')

elif 25 <= imc > 30:
	print('SOBREPESO')

elif 30 <= imc > 40:
	print('OBESIDADE')

elif imc >= 40:
	print('OBESIDADE MÓRBIDA')