soma = 0
maior_idade_h = 0
nome_velho = ''
total_mulher_20 = 0
media = 0

for cont in range(1, 5, 1):
    print('----- {}ª Pessoa -----'.format(cont))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [F/M]: ')).strip().upper()
    soma += idade
    if cont == 1 and sexo == 'M':
        nome_velho = nome
        maior_idade_h = idade
    if sexo == 'M' and idade > maior_idade_h:
        nome_velho = nome
        maior_idade_h = idade
    if sexo in 'F' and idade < 20:
        total_mulher_20 += 1

media = soma/4
print('----- Analisando -----')
print('A média de idade do grupo é de {} anos'.format(media))

if maior_idade_h == 0:
    print('Não há nenhum homem cadastrado.')
else:
    print('O homem mais velho tem {} anos e se chama {}.'.format(maior_idade_h, nome_velho))

if total_mulher_20 == 0:
    print('Não foi inserida nenhuma mulher com menos de 20 anos cadastrada.')
else:
    print('Ao todo são {} mulheres com menos de 20 anos.'.format(total_mulher_20))