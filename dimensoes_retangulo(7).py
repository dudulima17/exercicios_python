#Escreva um algoritmo para ler as dimensões de um retângulo (base e altura), calcular e escrever a área do retângulo, e caso seja um quadrado, exibir a frase: área de um quadrado
base=float(input('Digite o valor da altura: '))
alt=float(input('Digite o valor da altura: '))
area_retan=(base*alt)
if base == alt:
    area_quad=(alt*alt)
    print('Esta figura é um quadrado\n', area_quad)
else:
   if base > alt or base < alt:
    print('Esta figura é um retangulo\n', area_retan)
