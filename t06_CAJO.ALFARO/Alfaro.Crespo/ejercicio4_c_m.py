import os
#Input
numero1=float(os.sys.argv[1])
numero2=float(os.sys.argv[2])

#Processing
división=numero1/numero2

#Ouput
print("########################################################")
print("# Algoritmo para hallar la division entre dos números  #")
print("########################################################")
print("# numero1  :",numero1,"                                #")
print("# numero2  :",numero2,"                                #")
print("# division :",división,"                               #")
print("########################################################")

#condicional multiple
if división==int(división):
    print("la division es entera")
if división!=int(división):
    print("la division no es entera")
if numero2==0:
    print("ingrese otro numero")
if numero1>0 and numero2<0:
    print("la division es negativa")
if numero2>0 and numero1<0:
    print("la division es negativa")
#fin_if
