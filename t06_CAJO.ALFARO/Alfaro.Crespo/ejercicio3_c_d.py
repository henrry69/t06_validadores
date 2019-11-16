import os
#Input
numero1=float(os.sys.argv[1])
numero2=float(os.sys.argv[2])
numero3=float(os.sys.argv[3])

#Processing
resta=numero1-numero2-numero3

#Ouput
print("################################################")
print("# Algoritmo para hallar la resta de 3 numeros  #")
print("################################################")
print("# numero1 :",numero1,"                              #")
print("# numero2 :",numero2,"                              #")
print("# numero3 :",numero3,"                              #")
print("# resta   :",resta,"                             #")
print("################################################")

#condicional doble
if resta>=0:
    print("la resta es positiva")
else:
    print("la resta es negativa")
#fin_if
