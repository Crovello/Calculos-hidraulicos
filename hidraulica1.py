#Carlos Rovello Gando
#Prueba de calculos hidraulicos
#prueba continuidad calculo caudal

#llamado a libreria
from cmath import pi

print("Calculo diametro tuberia")
print("__________")
print("")

#Inicalizacion de variables

continuar=True

#ingreso datos

while continuar:

	Q=float(input("ingrese Caudal m^3/h:"))
	V=float(input("ingrese Velocidad m/s:"))
	D=(((Q*4)/(3600*pi*V))**0.5)*1000 #falta redondear el resultado asi como dar el diametro comercial
	print("el diametro es", D,"mm")
	print("")

#opcion de seleccion ciclica

	opcion= input("Conitnuar (s/n)")
	if (opcion.upper()=="N"):
		continuar=False

print("listo")
print("____________________")
