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

#condicional multiple
if nota1<0 or nota2<0 or nota3<0 or nota4<0:
    print("las notas son incorrectas")
if nota1>20 or nota2>20 or nota3>20 or nota4>20:
    print("la calificacion es de 0 a 20 revise las notas")
if nota1>0 and nota2>0 and nota3>0 and nota4>0 and promedio>=11:
    print("alumno aprobado")
if nota1>0 and nota2>0 and nota3>0 and nota4>0 and promedio<11:
    print("alumno desaprobado")
#fin_if
