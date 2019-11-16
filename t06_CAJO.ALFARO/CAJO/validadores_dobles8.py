import os
#calcular celular
#INPUT
masa=float(os.sys.argv[1])
longitud=float(os.sys.argv[2])
tiempo=float(os.sys.argv[3])

#PROCESSING
energia=(masa*longitud**2)/tiempo**2

#Validador
mucha_energia_utilizada=(energia>10)

#OUTPUT
print("##########################################")
print("####       calcular la energia        ####")
print("##########################################")
print("#### base_mayor:",masa,"              #######")
print("####tiempo:", tiempo,"                    ######")
print("#### altura:",longitud,"                    #####")
print("#### area:",energia ,"       #####")
print("##########################################")

#
#condision doble
if (mucha_energia_utilizada == True):
    print("mucha energia utilizada")
else:
    print ("poca energia utilizada")
#fin_if
