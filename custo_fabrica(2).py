#O custo ao consumidor de um carro novo é a soma do custo de fábrica com a percentagem do distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que a percentagem do distribuidor seja de 28% e os impostos de 45%, escrever um algoritmo que leia o custo de fábrica de um carro e escreva o custo ao consumidor.
#VARIÁVEIS DE ENTRADA
val_carro=int(input('Digite o valor do carro:'))
distri=0.28
impos=0.45
custo=0.27
custo_consu=(val_carro*custo)
print("O custo da fábrica é: ",custo_consu) #SAÍDA
