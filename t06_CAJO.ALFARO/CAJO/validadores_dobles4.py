import os
#INPUT
estudiante=os.sys.argv[1]
horas_estudiadas_por_dia=float(os.sys.argv[2])
dias_de_estudio=float(os.sys.argv[3])

#PROCESSING
horas_estudiadas_en_la_semana=horas_estudiadas_por_dia*dias_de_estudio

#Validadores
varias_hora_estudiadas=(horas_estudiadas_en_la_semana>150)

#OUTPUT

print("##############################################")
print("##calcular horas estudiadas a la semana ######")
print("##############################################")
print("####estudiante:",estudiante,"                  ###" )
print("#### horas de estudiadas por dia:",horas_estudiadas_por_dia,"    ####")
print("#### dias de estudio:",dias_de_estudio,"                 ###")
print("#### horas estudiadas a la semana:",horas_estudiadas_en_la_semana  ,"  ####")
print("#############################################")

#
#condision doble
if (varias_hora_estudiadas == True):
    print("alumnno estudioso")
else:
    print ("alumno no estudioso")
#fin_if
