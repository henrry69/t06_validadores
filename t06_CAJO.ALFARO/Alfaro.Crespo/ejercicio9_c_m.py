import os
#Input
numero1=float(os.sys.argv[1])
numero2=float(os.sys.argv[2])

#Processing
potencia=(numero1*numero2)**5

#Ouput
print("##################################################")
print("# Algoritmo para elevar un producto a la quinta  #")
print("#################################################")
print("# numero1  :",numero1,"                            #")
print("# numero2  :",numero2,"                            #")
print("# potencia :",potencia,"                            #")
print("##################################################")

#condicional multiple
if potencia>=10000:
    print("nos tomo un par de segundos hacer tu calculo ")
if potencia<10000:
    print("el calculo fue rapido")
if potencia<0:
    print("el numero1 o el numero2 es negativo")
#fin_if
