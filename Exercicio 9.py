print("Este programa calcula o preço total de compra de maçãs e bananas, sendo cada maçã R$1.30 e bananas R$5.00 o kg")

preco_maca = 1.30
preco_banana = 5
quantidade_macas = float(input("Digite a quantidade de maçãs que vai comprar: "))
quilo_bananas = float(input("Digite a quantidade de kg de bananas que vai comprar: "))

preco_macas = quantidade_macas * preco_maca
preco_bananas = quilo_bananas * preco_banana
preco_total = preco_macas + preco_bananas

print("O preço total a pagar é de: R$" +str(preco_total))