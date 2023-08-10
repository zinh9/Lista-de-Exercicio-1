print("Este programa calcula a sua idade em dias")

idade = int(input("Digite a sua idade: "))
meses = int(input("Digite os meses: "))
dias = int(input("Digite os dias: "))

dias_ano = idade * 365
dias_meses = meses * 30

dias_totais = dias_ano + dias_meses + dias

print("Sua idade em dias é de: " +str(dias_totais) +" dias")