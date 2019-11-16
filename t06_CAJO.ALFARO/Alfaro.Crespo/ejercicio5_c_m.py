import os
#Input
numero1=float(os.sys.argv[1])
numero2=float(os.sys.argv[2])

#Processing
raiz=(numero1*numero2)**(1/2)

#Ouput
print("###########################################################")
print("# Algoritmo para hallar la raiz cuadrada de un producto   #")
print("###########################################################")
print("# numero1 :",numero1,"                                        #")
print("# numero2 :",numero2,"                                        #")
print("# raiz  :",raiz,"                                 #")
print("###########################################################")

#condicional multiple
if raiz==int(raiz):
    print("la raiz es exacta")
if raiz!=int(raiz):
    print("la raiz es inexacta")
if numero2>0 and numero1<0:
    print("cambie el numero1")
if numero1>0 and numero2<0:
    print("cambie el numero2")
#fin_if
