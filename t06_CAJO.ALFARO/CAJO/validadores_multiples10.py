import os
#INPUT
radio=float(os.sys.argv[1])
pi=float(os.sys.argv[2])

#PROCESSING
area=pi*(radio**2)

#Validadores
radio_pequeno=(area<20)

#OUTPUT
print("##########################################")
print("####   calcular area del circulo      ####")
print("##########################################")
print("#### radio:",radio,"                   #######")
print("#### pi:",pi,"                       #####")
print("#### area:",area  ,"                     #####")
print("##########################################")

#
#condision multiple
if (radio_pequeno == True):
    print("radio pequño")
if (area<0):
    pritn("ingrese bien los valores")
else:
    print ("radio grande")
#fin_if
