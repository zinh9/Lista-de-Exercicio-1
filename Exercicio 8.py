print("Este programa calcula a distância percorrida com o Movimento Uniformemente Variado, \nsabendo que a posição inicial é 2 metros, velocidade inicial é de 3 m/s, e a aceleração é de 10 m/s²")

tempo = float(input("Digite o tempo percorrido (segundos): "))
posicao_inicial = 2
velocidade_inicial = 3
aceleracao = 10

posicaoFinal = posicao_inicial + (velocidade_inicial * tempo) + (0.5 * aceleracao * tempo ** 2)

print("A distância percorrida foi de " + str(posicaoFinal) + " metros")