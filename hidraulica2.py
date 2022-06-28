#Carlos Rovello Gando
#Prueba de calculos hidraulicos
#prueba continuidad calculo caudal

#llamado a libreria
from cmath import pi

print("Calculo caudal por tuberia")
print("__________")
print("")

#Inicalizacion de variables

continuar=True

#ingreso datos

while continuar:

	D=float(input("ingrese Diametro mm:"))
	V=float(input("ingrese Velocidad m/s:"))
	a=D/1000
	b=(pi*a**2)/4
	c=b*V
	d=c*3600



	print("el caudal de paso es", d,"m3/h")
	print("")

#opcion de seleccion ciclica

	opcion= input("Conitnuar (s/n)")
	if (opcion.upper()=="N"):
		continuar=False

print("listo")
print("____________________")