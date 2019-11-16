import os
#Input
nota1=float(os.sys.argv[1])
nota2=float(os.sys.argv[2])
nota3=float(os.sys.argv[3])
nota4=float(os.sys.argv[4])

#Processing
promedio=(nota1+nota2+nota3+nota4)/4

#Ouput
print("############################################")
print("# Algoritmo para saber la suma de 4 notas  #")
print("############################################")
print("# nota1    :",nota1,"                            #")
print("# nota2    :",nota2,"                            #")
print("# nota3    :",nota3,"                            #")
print("# nota4    :",nota4,"                            #")
print("# promedio :",promedio,"                            #")
print("############################################")

#condicional doble
if promedio>=11:
    print("alumno aprobado")
else:
    print("alumno desaprobado")
#fin_if
