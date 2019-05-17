#raizes de uma equação quadrática
#dados de entrada
import math
a=float(input("Entre com o valor de a:"))
b=float(input("Entre com o valor de b:"))
c=float(input("Entre com o valor de c:"))


#calculo delta
delta= (b**2)-(4*a*c)


#calculo bhaskara
def bhaskara(x):
    x1=(-b+math.sqrt(delta))/(2*a)
    x2=(-b-math.sqrt(delta))/(2*a)
    return x1,x2

#verificacao das raizes
if delta<0:
    print("Esta equação não possui raízes reais")
else:
    if delta==0:
        bhaskara(delta)
        print("Esta equação possui duas raízes reais iguais", bhaskara(delta)) 
    else:
        bhaskara(delta)
        print("Esta equação possui duas raízes reais diferentes", bhaskara(delta))
        
        
