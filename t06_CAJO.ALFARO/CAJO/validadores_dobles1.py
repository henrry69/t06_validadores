import os
#PROMEDIO DE ALUMNO

#Input
alumno=os.sys.argv[1]
nota1=float(os.sys.argv[2])
nota2=float(os.sys.argv[3])
nota3=float(os.sys.argv[4])

#Processing
promedio=(nota1+nota2+nota3)/3

#validadores
alumno_aprobado=(promedio>=10)

#Ouput
print("############################################")
print("#          calcular el promedio            #")
print("############################################")
print("# alumno   :",alumno,"                          #")
print("# nota1    :",nota1,"                          #")
print("# nota2    :",nota2,"                          #")
print("# nota3    :",nota3,"                          #")
print("# promedio :",promedio,"                          #")
print("############################################")

#
#condision doble
if (alumno_aprobado == True):
    print("aprobaste el curso")

else:
    print ("desaprobaste el curso")
#fin_if
