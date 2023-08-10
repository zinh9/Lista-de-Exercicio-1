print("Este programa calcula o seu IMC (Índice de Massa Corporal)")

massa = float(input("Digite a sua massa (kg): "))
altura = float(input("Digite a sua altura (metros): "))

imc = massa / (altura ** 2)

print("O seu IMC de é" +str(imc) +" kg")