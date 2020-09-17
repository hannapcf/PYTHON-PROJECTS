v1 = int(input('Insira o 1º valor: '))
v2 = int(input('Insira o 2º valor: '))
opcao = 0

while opcao != 5:
    print(""" -=-=- M E N U -=-=- 
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa""")
    opcao = int(input('Qual é sua opção? '))
    if opcao < 1 or opcao > 5:
        print('Opção inválida.')
    elif opcao == 1:
        print('A soma dos dois números é {}'.format(v1+v2))
    elif opcao == 2:
        print('A multiplicação dos dois números é {}'.format(v1*v2))
    if opcao == 3:
        if v1 > v2:
            print('O maior número é o {}'.format(v1))
        else:
            print('O maior número é o {}'.format(v2))
    if opcao == 4:
        v1 = int(input('Insira o 1º valor: '))
        v2 = int(input('Insira o 2º valor: '))

print('Programa finalizado.')
