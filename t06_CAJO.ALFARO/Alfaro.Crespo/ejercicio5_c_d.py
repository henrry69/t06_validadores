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

#condicional doble
if raiz==int(raiz):
    print("la raiz es exacta")
else:
    print("la raiz es inexacta")
#fin_if
