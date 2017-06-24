quant_alu=int(input('Digite a quantidade de alunos presentes: '))
cont=1

while quant_alu >= cont:
    peso=float(input('Digite o peso do aluno: '))
    print(peso)
    alt=float(input('Digite a altura do aluno: '))
    print(alt)
    cont=cont+1
media_p=(peso/quant_alu)
print(media_p)
media_alt=(alt/quant_alu)
print(media_alt)
imc=(peso/alt**2)
print(imc)
