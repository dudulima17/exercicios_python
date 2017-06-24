#VARIÁVEIS DE ENTRADA
dia=int(input('Informe o dia em que nasceu: '))
mes=int(input('Informe o mes em que nasceu: '))
ano=int(input('Informe o ano em que nasceu: '))
dia_atual=int(input('Informe o dia atual: '))
mes_atual=int(input('Informe o mes atual: '))
ano_atual=int(input('Informe o ano atual: '))

#PROCESSAMENTO
x=(2017-ano)
if mes_atual < mes:
    print(x-1)
else:
    print(x)
if dia_atual < dia:
    print(x-1)
else:
    print(x)

mes_atual=(30*12)
dia_atual=(365*30)


print('Voce tem', dia_atual, 'dias')
print('Voce tem', mes_atual, 'meses')
print('Voce tem', x, 'anos')
