#sistema deve perguntar quantos cigarros a pessoa fuma por dia  e por quantos anos ela já fuma. Sabendo que cada cigarro se perde 10min de vida sistema deve calcular quantos dias de vida o fumente perderá
cig=int(input('Indique a quantidade de cigarros por dia'))
anos=int(input('Indique quantos anos foram perdidos'))
min_per=cig*10
min_per_dia=min_per/1440
dias_per=min_per_dia*365*anos
print("voce perdeu", dias_per)

