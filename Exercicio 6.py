print("Este programa calcula o volume e a area de uma esfera")

raio_esfera = float(input("Digite o raio da esfera: "))

volume_esfera = (4 / 3) * 3.1415 * (raio_esfera ** 3)
area_esfera = 4 * 3.1415 * (raio_esfera ** 2)

print("O volume da esfera é de " +str(volume_esfera) +" cm")
print("E a area da esfera é de " +str(area_esfera) +" cm")