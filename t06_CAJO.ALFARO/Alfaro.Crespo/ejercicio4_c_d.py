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

#condicional doble
if división==int(división):
    print("la division es entera")
else:
    print("la division no es entera")
#fin_if
