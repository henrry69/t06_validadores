import os
#Input
lado1=float(os.sys.argv[1])
lado2=float(os.sys.argv[2])

#Processing
area=lado2*lado1

#Ouput
print("##################################################")
print("# Algoritmo para hallar el area de un rectangulo #")
print("##################################################")
print("# lado1 :",lado1,"                                     #")
print("# lado2 :",lado2,"                                     #")
print("# area  :",area,"                                  #")
print("##################################################")

#condicional doble
if area<25:
    print("el area es muy pequeña para construir una casa")
else:
    print("se puede contruir una casa")
#fin_if
