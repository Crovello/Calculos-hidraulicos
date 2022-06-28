#Carlos Rovello Gando
#Prueba de calculos hidraulicos
#prueba continuidad calculo velocidad

#llamado a libreria
from cmath import pi

print("Calculo velocidad por tuberia")
print("__________")
print("")

#Inicalizacion de variables

continuar=True

#ingreso datos

while continuar:


    D=float(input("ingrese Diametro mm:"))
    Q=float(input("ingrese Caudal m3/h:"))
    V=((Q/3600)/((pi*(D/1000)**2)/4))

    print("la velocidad es", V,"m/s")
    print("")

#opcion de seleccion ciclica
    opcion= input("Conitnuar (s/n)")
    if (opcion.upper()=="N"):
        continuar=False

print("listo")
print("____________________")

