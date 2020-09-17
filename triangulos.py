r1 = float(input('Insira a primeira reta: '))
r2 = float(input('Insira a segunda reta: '))
r3 = float(input('Insira a terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas acima podem formar um triângulo ', end='')
    if r1 == r2 == r3:
        print('Equilatero!')
    elif r1 != r2 != r3 != r1:
        print('Escaleno!')
    else:
        print('Isóceles!')
else:
    print('Essas retas não formam um triângulo.')