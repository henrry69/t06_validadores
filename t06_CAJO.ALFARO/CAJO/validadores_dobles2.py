import os
#pago de trabajador
#INPUT
trabajador=os.sys.argv[1]
pago_por_horas=float(os.sys.argv[2])
horas_trabajadas=float(os.sys.argv[3])

#PROCESSING
pago_de_trabajador=pago_por_horas*horas_trabajadas

#validadores
trabjador_con_buen_sueldo=(pago_de_trabajador>8000)

#OUPUT
print("##########################################")
print("####   calcular pago de trabajador    ####")
print("##########################################")
print("####trabajador:",trabajador,"                  ###" )
print("#### pago por horas :",pago_por_horas,"           #####")
print("#### horas trabajadas:",horas_trabajadas,"          #####")
print("#### pago de trabajdor:",pago_de_trabajador,"         #####")
print("##########################################")

#
#condision simple
if (trabjador_con_buen_sueldo == True):
    print("buena paga a trabajador")
else:
    print("mala paga a trabajador")
#fin_if
