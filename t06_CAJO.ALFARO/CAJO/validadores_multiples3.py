import os
#bonificacion de trabajador
#INPUT
trabajador=os.sys.argv[1]
numero_de_articulos_vendidos=float(os.sys.argv[2])
monto_promedio_de_ventas=float(os.sys.argv[3])

#PROCESSING
bonificacion=numero_de_articulos_vendidos*monto_promedio_de_ventas

#Validadores
bonificacion_alta=(bonificacion>100)

#OUTPUT

print("##########################################")
print("####   calcular la bonificacion       ####")
print("##########################################")
print("####trbajador:",trabajador,"                  ###" )
print("#### numero de articulos vendidos:",numero_de_articulos_vendidos,"###")
print("#### monto promedio de ventas:",monto_promedio_de_ventas,"   ####")
print("#### bonificacion:",bonificacion  ,"               ####")
print("##########################################")

#
#condision multiple
if (bonificacion_alta == True):
    print("trabajador con bonificacion ata")
if (bonificacion==0):
    print ("no trabajo hors extras")
else:
    print("trabajador con bonificacion baja")
#fin_if
