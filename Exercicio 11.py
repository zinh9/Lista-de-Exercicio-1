print("Este programa calcula o custo final do preço de um carro novo")

custo_carro = float(input("Digite o preço do carro: "))
porc_distribuidor = 28 / 100
porc_imposto = 45 / 100

custo_final = (porc_distribuidor * custo_carro) + (porc_imposto * custo_carro) + custo_carro

print("O valor final do carro sai por: R$" +str(custo_final))