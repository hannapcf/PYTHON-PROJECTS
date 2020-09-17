peso = float(input('Insira seu peso: '))
altura = float(input('Insira sua altura em metros: '))
imc = peso / (altura **2)

if imc < 18.5:
    print('Você está abaixo do peso.')
elif imc < 25:
    print('Você está no seu peso ideal.')
elif imc < 30:
    print('Você está com sobrepeso.')
elif imc < 40:
    print('Você está com obesidade.')
else:
    print('Você está com obesidade mórbida.')