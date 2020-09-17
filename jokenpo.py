import random
import time

PAPEL = 'Papel'
PEDRA = 'Pedra'
TESOURA = 'Tesoura'

print('-=-'*15)
print('AGORA NÓS VAMOS JOGAR JOKENPÔ!')
print('-=-'*15)
print("""Você está preparado?
1- Papel
2- Pedra
3- Tesoura""")
print('-=-'*15)

while True:
    escolha = int(input('E ái!? Pedra, papel ou tesoura? '))
    print('-=-'*15)
    computador = random.randint(1,3)

    if computador == 1:
        computador = PAPEL
    elif computador == 2:
        computador = PEDRA
    elif computador == 3:
        computador = TESOURA

    if escolha == 1:
        escolha = PAPEL
    elif escolha == 2:
        escolha = PEDRA
    elif escolha == 3:
        escolha = TESOURA

    print('JO')
    time.sleep(0.5)
    print('KEN')
    time.sleep(0.5)
    print('PO!')
    time.sleep(0.5)
    print('-=-'*15)

    print('Você escolheu:', escolha)
    print('O bot escolheu:', computador)
    print('-=-'*15)

    if escolha == computador:
        print('Temos um empate!')
    elif escolha == PAPEL and computador == PEDRA:
        print('Papel ganha de pedra!')
        print('Parabéns, você ganhou!')
    elif escolha == PEDRA and computador == PAPEL:
        print('Papel ganha de pedra!')
        print('Você perdeu!')
    elif escolha == TESOURA and computador == PAPEL:
        print('Tesoura ganha de papel!')
        print('Parabéns, você ganhou!')
    elif escolha == PAPEL and computador == TESOURA:
        print('Tesoura ganha de papel!')
        print('Você perdeu!')
    elif escolha == TESOURA and computador == PEDRA:
        print('Pedra ganha de tesoura!')
        print('Você perdeu!')
    elif escolha == PEDRA and computador == TESOURA:
        print('Pedra ganha de tesoura!')
        print('Parabéns! Você ganhou!')
    else:
        (print('Insira um comando válido.'))
    print('-=-'*15)