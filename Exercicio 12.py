print("Este programa calcula o seu salario final com o número de carros vendidos, o valor total de vendas, \no salário fixo e o valor de comissão que ele recebe por carro vendido")

qnt_carros_vendidos = int(input("Digite a quantidade de carros vendidos: "))
val_total_vendas = float(input("Digite o valor total de vendas: "))
val_sal_fixo = float(input("Digite o valor do seu salario: "))
val_comissao = float(input("Digite o valor da comissão: "))

val_sal_final = val_sal_fixo + (val_comissao * qnt_carros_vendidos) + (5 * val_total_vendas / 100)

print("O seu salario final é de: R$" +str(val_sal_final))