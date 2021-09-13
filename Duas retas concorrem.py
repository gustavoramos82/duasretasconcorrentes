from termcolor import colored as cl
from matplotlib import pyplot as pl
import numpy as np

#Valor correspondente a primeira equação
ca1 = float(input(cl('Digite o valor do primeiro coeficiente angular:','cyan')))
cl1 = float(input(cl('Digite o valor do primeiro coeficiente linear:','yellow')))

#Valor correspondente a segunda equação
ca2 = float(input(cl('Digite o valor do segundo coeficiente angular:','cyan')))
cl2 = float(input(cl('Digite o valor do segundo coeficiente linear:','yellow')))

#Valor das coordenadas
coorx = (cl2-cl1)/(ca1-ca2)
coory = (ca1*cl2-cl1*ca2)/(ca1-ca2)

if ca1 == ca2:
    print(cl('As retas não se intersectam','red'))
elif ca1 != ca2:
    print(cl('As retas se intersectam no ponto ({:.2f},{:.2f})'.format(coorx,coory),'green'))

print(cl('Agora vou mostrar o grafico para ficar melhor a visualização','cyan'))

#Mostrando o gráfico
valorx = np.arange(-1000,1000,1)

pl.plot(valorx,ca1*valorx+cl1)
pl.plot(valorx,ca2*valorx+cl2)
pl.show()