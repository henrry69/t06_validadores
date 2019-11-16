import os
#calcular la hipotenusa

#IMPUT
cateto_uno=float(os.sys.argv[1])
cateto_dos=float(os.sys.argv[2])

#PROCESSING
hipotenusa=(cateto_uno**2+cateto_dos**2)**(1/2)

#validadores
triangulo_grande=(hipotenusa>100)

#OUTPUT
print("##########################################")
print("####    calcular la hipotenusa        ####")
print("##########################################")
print("#### cateto uno:",cateto_uno,"               ######")
print("#### cateto dos:",cateto_dos,"                #####")
print("#### hipotenusa:",hipotenusa ,"   #####")
print("##########################################")

#
#condision simple
if (triangulo_grande == True):
    print("triangulo grande")
#fin_if
