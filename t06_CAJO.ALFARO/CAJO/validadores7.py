import os
#promedio de ventas de los 3 ultimos meses

#Input
vendedor=os.sys.argv[1]
mes1=float(os.sys.argv[2])
mes2=float(os.sys.argv[3])
mes3=float(os.sys.argv[4])

#Processing
promedio_de_ventas=(mes1+mes2+mes3)/3

#validadores
excelente_vendedor=(promedio_de_ventas>1000)

#Ouput
print("############################################")
print("#          calcular el promedio            #")
print("############################################")
print("# vendedor   :",vendedor,"                          #")
print("# mes1    :",mes1,"                          #")
print("# mes2    :",mes2,"                          #")
print("# mes3    :",mes3,"                          #")
print("# promedio de ventas :",promedio_de_ventas,"                          #")
print("############################################")

#
#condision simple
if (promedio_de_ventas == True):
    print("excelente vendedor")
#fin_if
