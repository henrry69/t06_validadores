import os
#boleta de venta

#Input
cliente=os.sys.argv[1]
producto=os.sys.argv[2]
precio=float(os.sys.argv[3])
cantidad=float(os.sys.argv[4])

#Processing

monto_total=precio*cantidad
#validadores
comprador_recurrente=(monto_total>500)

#Ouput
print("############################################")
print("#            boleta de ventas              #")
print("############################################")
print("# cliente   :",cliente,"                          #")
print("# producto    :",producto,"                          #")
print("# precio    :",precio,"                          #")
print("# cantidad   :",cantidad,"                          #")
print("# monto total :",monto_total,"                          #")
print("############################################")

#
#condision multiple
if (comprador_recurrente == True):
    print(" opcion a llevar un producto gratis ")
if (monto_total<0):
    print("error en el sistema")
else:
    print ("compras mas  para llegar a la opcion de llevarse un producto gratis")

#fin_if
