import os
#Input
precio1=float(os.sys.argv[1])
precio2=float(os.sys.argv[2])
precio3=float(os.sys.argv[3])
precio4=float(os.sys.argv[4])
precio5=float(os.sys.argv[5])
precio6=float(os.sys.argv[6])
precio7=float(os.sys.argv[7])

#Processing
suma=precio1+precio2+precio3+precio4+precio5+precio6+precio7

#Ouput
print("################################################################")
print("# Algoritmo para hallar la suma de precios de útiles escolares #")
print("################################################################")
print("# precio1 :",precio1,"                                                    #")
print("# precio2 :",precio2,"                                                    #")
print("# precio3 :",precio3,"                                                    #")
print("# precio4 :",precio4,"                                                    #")
print("# precio5 :",precio5,"                                                    #")
print("# precio6 :",precio6,"                                                    #")
print("# precio7 :",precio7,"                                                    #")
print("# suma    :",suma,"                                             #")
print("################################################################")

#condicional doble
if  suma>100:
    print("Felicitaciones gano una tarjeta")
else:
    print("Gracias por su compra,vuelva pronto y compre mas para ganar una tarjeta")
#fin_if
