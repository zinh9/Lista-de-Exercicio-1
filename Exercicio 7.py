print("Este programa calcula a média da avaliação semestral da escola")

primeira_avaliacao = float(input("Digite a nota da primeira avaliação: "))
segunda_avaliacao = float(input("Digite a nota da segunda avaliação: "))
atividades = float(input("Digite a nota total das atividades: "))

media = (4 * primeira_avaliacao) + (3 * segunda_avaliacao) + (2 * atividades) / 9

print("A sua média semestral é de: " +str(media) +" pontos")