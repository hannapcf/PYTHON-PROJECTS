MOEDA100 = 100
MOEDA50 = 50
MOEDA25 = 25
MOEDA10 = 10
MOEDA5 = 5

quantidade_moeda_100 = int(input('Insira a quantidade de moedas de 1 real: '))
quantidade_moeda_50 = int(input('Insira a quantidade de moedas de 50 centavos: '))
quantidade_moeda_25 = int(input('Insira a quantidade de moedas de 25 centavos: '))
quantidade_moeda_10 = int(input('Insira a quantidade de moedas de 10 centavos: '))
quantidade_moeda_5 = int(input('Insira a quantidade de moedas de 5 centavos: '))

while True:
    troco100 = 0
    troco50 = 0
    troco25 = 0
    troco10 = 0
    troco5 = 0

    valor_gasto = float(input('Insira o valor gasto pelo cliente: '))
    valor_pago = float(input('Insira o valor pago pelo cliente: '))
    troco = valor_pago - valor_gasto
    troco_centavos = int(troco * 100)

    if troco_centavos % 5 > 0:
        print('!ATENÇÃO! Erro. Esta maquina nao possui moedas de 1 centavo.')
        exit()

    while troco_centavos > 0:
        if troco_centavos >= 100 and quantidade_moeda_100 > 0:
            quantidade_moeda_100 = quantidade_moeda_100 - 1
            troco100 = troco100 + 1
            troco_centavos = troco_centavos - 100
        elif troco_centavos >= 50 and quantidade_moeda_50 > 0:
            quantidade_moeda_50 = quantidade_moeda_50 - 1
            troco50 = troco50 + 1
            troco_centavos = troco_centavos - 50
        elif troco_centavos >= 25 and quantidade_moeda_25 > 0:
            quantidade_moeda_25 = quantidade_moeda_25 - 1
            troco25 = troco25 + 1
            troco_centavos = troco_centavos - 25
        elif troco_centavos >= 10 and quantidade_moeda_10 > 0:
            quantidade_moeda_10 = quantidade_moeda_10 - 1
            troco10 = troco10 + 1
            troco_centavos = troco_centavos - 10
        elif troco_centavos >= 5 and quantidade_moeda_5 > 0:
            quantidade_moeda_5 = quantidade_moeda_5 - 1
            troco5 = troco5 + 1
            troco_centavos = troco_centavos - 5
        elif troco_centavos > 0:
            print('!ATENÇAO! Erro. Nao ha mais moedas na maquina')
            exit()

    print('Seu troco é de R$', troco, 'reais. Ele sera pago em:')
    print(troco100, 'moedas de 1 real')
    print(troco50, 'moedas de 50 centavos')
    print(troco25, 'moedas de 25 centavos')
    print(troco10, 'moedas de 10 centavos')
    print(troco5, 'moedas de 5 centavos')