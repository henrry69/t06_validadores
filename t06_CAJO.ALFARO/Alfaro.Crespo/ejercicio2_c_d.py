import os
#Input
numero1=int(os.sys.argv[1])
numero2=int(os.sys.argv[2])

#Processing
modulo=numero1%numero2

#Ouput
print("###########################################################")
print("# Algoritmo para hallar el modulo de dos números enteros  #")
print("###########################################################")
print("# numero1 :",numero1,"                                           #")
print("# numero2 :",numero2,"                                           #")
print("# modulo  :",modulo,"                                            #")
print("###########################################################")

#condicional doble
if modulo==0:
    print("el numero1 es multiplo del numero2 ")
else:
    print("el numero1 no es multiplo del numero2 ")
#fin_if
