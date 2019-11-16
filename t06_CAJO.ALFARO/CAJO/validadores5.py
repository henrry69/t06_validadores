import os
#INPUT
trabajador=os.sys.argv[1]
pago_por_horas_extras=float(os.sys.argv[2])
horas_extras_trabajadas=float(os.sys.argv[3])

#PROCESSING
pago_total_de_horas_extras_trabajadas=pago_por_horas_extras*horas_extras_trabajadas

#Validadores
pago_total_por_horas_extras_alta=(pago_total_de_horas_extras_trabajadas>120)

#OUTPUT

print("###################################################")
print("####   calcular el pago tota por horas extras   ###")
print("###################################################")
print("####trbajador:",trabajador,"                               ###" )
print("#### pago por horas extras:",pago_por_horas_extras,"           #######")
print("#### horas extras trabajadas:",horas_extras_trabajadas,"             #####")
print("#### pago total de horas extras trabajadas:",pago_total_de_horas_extras_trabajadas ,"###")
print("##########################################")

#
#condision simple
if (pago_total_por_horas_extras_alta == True):
    print("pago total por horas extra salta")
#fin_if
