import os
#Input
lado1=float(os.sys.argv[1])
lado2=float(os.sys.argv[2])
lado3=float(os.sys.argv[3])

#Processing
perimetro=lado2+lado1+lado3

#Ouput
print("##################################################################")
print("#      Algoritmo para hallar el perimetro  de un triangulo       #")
print("##################################################################")
print("# lado1     :",lado1,"                                           #")
print("# lado2     :",lado2,"                                           #")
print("# lado3     :",lado3,"                                           #")
print("# perimetro :",perimetro,"                                       #")
print("##################################################################")

#condicional multiple
if perimetro<=0:
    print("el triangulo no existe")
if perimetro>100:
    print("el perimetro es extenso")
if perimetro>0 and perimetro<=100:
    print("el perimetro es pequeño")
#fin_if

