# Año bisiesto

Año = int(input("Escribe el año :"))

if Año < 1582:
    print ("No se considera Año Gregoriano")
else:
    if Año % 4 != 0:
        print ("Es un año comun")
    elif Año % 100 != 0:
        print ("Es un año bisiesto")
    elif Año % 400 != 0:
        print ("Es un año comun")
    else:
        print ("Es un año bisiesto")

    
 