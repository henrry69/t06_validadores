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

#condicional multiple
if area<25:
    print("el area es muy pequeña para construir una casa")
if area>=25 and area<200:
    print("se puede contruir una casa pequeña")
if area>=200 and area<400:
    print("se puede contruir una casa grande")
if area>=400:
    print("se puede construir una mansion")
#fin_if
