lado1=input('Informe a medida do primeiro lado(base): ')
lado2=input('Informe a medida do segundo lado: ')
lado3=input('Informe a medida do terceiro lado: ')
if lado1 == lado2 == lado3:
    print('Este triangulo é equilátero!')
if lado2 == lado3:
    print('Este triangulo é isósceles!')
else:
    if lado1 > lado2 or lado1 < lado2 or lado2 > lado3 or lado2 < lado3 or lado3 > lado1 or lado3 < lado1 :
        print('Este triangulo é escaleno!')

