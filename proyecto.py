import sys
import math
import time
import os
listaCarros = ["Renault Duster", "Renault Kwid", "Kia Picanto", "Chevrolet Onix", "Mazda 3", "Toyota Corolla Cross", "Nissan Qashgqai"]
listaLocalidades = ["Chapinero", "Fontibon", "La Candelaria", "Santa Fe", "Teusaquillo", "Usaquen"]
listaGasolineras = ["Terpel Javeriana", "Eds Terpel Villa Alsacia", "Texaco Av 68 con Calle 13", "Texaco el Chico", "Primax Olaya", "Primax Calle 100"] 


def limpiarTerminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        
def Menu_1():
    while True: 
        print("---SELECCION DE VEHICULO---")
        print("")
        print("Seleccione su modelo de vehículo")
        print("1.Renault Duster")
        print("2.Renault Kwid")
        print("3.Kia Picanto")
        print("4.Chevrolet Onix")
        print("5.Mazda 3")
        print("6.Toyota Corolla Cross")
        print("7.Nissan Qashqai")
        print("0.Volver al menu")
        print("")
        modeloCarro = int(input("Ingrese una opcion: "))
        
        if modeloCarro == 0:
            modeloCarro = 1
            return None
        elif modeloCarro < 0 or modeloCarro > 7:
            print("")
            print("Opcion invalida, intente nuevamente")
        else:
            limpiarTerminal()
            print("Has elegido el carro: ", listaCarros[modeloCarro-1])
            time.sleep(2)
            limpiarTerminal()
            return modeloCarro    
    
def Menu_2():
    while True: 
        print("---SELECCION DE INICIO DE RUTA---")
        print("")
        print("Seleccione el punto de partida")
        print("1.Chapinero")
        print("2.Fontibon")
        print("3.La Candelaria")
        print("4.Santa Fe")
        print("5.Teusaquillo")
        print("6.Usaquen")
        print("0.Volver al menu")
        print("")
        inicioRuta = int(input("Ingrese una opcion: "))
        
        if inicioRuta == 0:
            Menu_Principal()
        elif inicioRuta < 0 or inicioRuta > 6:
            print("")
            print("Opcion invalida, intente nuevamente")
        else:
            limpiarTerminal()
            print("Has elegido el punto de partida: ", listaLocalidades[inicioRuta-1])
            time.sleep(2)
            limpiarTerminal()
            break
        
    while True: 
        print("---SELECCION DE DESTINO DE RUTA---")
        print("")
        print("Seleccione el destino de su viaje")
        print("1.Chapinero")
        print("2.Fontibon")
        print("3.La Candelaria")
        print("4.Santa Fe")
        print("5.Teusaquillo")
        print("6.Usaquen")
        print("0.Volver al menu")
        print("")
        finalRuta = int(input("Ingrese una opcion: "))
        
        if finalRuta == 0:
            finalRuta = 1
            Menu_Principal()
        elif finalRuta < 0 or finalRuta > 6:
            print("")
            print("Opcion invalida, intente nuevamente")
        else:
            limpiarTerminal()
            print("Has elegido el destino: ", listaLocalidades[finalRuta-1])
            time.sleep(2)
            limpiarTerminal()
            break
    
    return inicioRuta, finalRuta   
    

def Menu_3(): 
    while True: 
        print("---SELECCION DE GASOLINERA---")
        print("")
        print("Seleccione la gasolinera que planea usar")
        print("1.Terpel Javeriana ($16.330)")
        print("2.EDS Terpel Villa Alsacia ($15.550)")
        print("3.Texaco Av 68 con Calle 13 ($15.500)" )
        print("4.Texaco El Chico ($16.380)")
        print("5.Primax Olaya ($15.580)")
        print("6.Primax Calle 100 ($16.330)")
        print("0.Volver al menu")
        print("")
        gasolinera = int(input("Ingrese una opcion: "))
        
        if gasolinera == 0:
            gasolinera = 1
            Menu_Principal()
        elif gasolinera < 0 or gasolinera > 7:
            print("")
            print("Opcion invalida, intente nuevamente")
        else:
            limpiarTerminal()
            print("Has elegido la gasolinera: ", listaGasolineras[gasolinera-1])
            time.sleep(2)
            limpiarTerminal()
            break
    return gasolinera


def Menu_4(modeloCarro, inicioRuta, finalRuta, gasolinera, listaCarros, listaLocalidades, listaGasolineras):
    listaCoordX = [28, 12, 27, 27, 22, 29]
    listaCoordY = [22, 18, 16, 17, 19, 29]
    listaKmXgal = [40, 54, 52, 44, 37, 36, 28] 
    listaPrecios = [16330, 15550, 15500, 16380, 15580, 16330]
    distanciaX = abs(listaCoordX[inicioRuta - 1]- listaCoordX[finalRuta - 1])
    distanciaY = abs(listaCoordY[inicioRuta - 1]- listaCoordY[finalRuta - 1]) 
    distancia = math.hypot(distanciaX, distanciaY)
    galonesUsados = (distancia/listaKmXgal[modeloCarro - 1])
    while True: 
        print("---GASTO DE GASOLINA ESTIMADO---")
        print("")
        print("Modelo de carro: ", listaCarros[modeloCarro - 1])
        print("Punto de partida: ", listaLocalidades[inicioRuta - 1])
        print("Destino: ", listaLocalidades[finalRuta - 1])
        print("Distancia estimada: ", round(distancia, 1), "Km")
        print("Gasolinera seleccionada: ", listaGasolineras[gasolinera - 1])
        print("")
        print("USO DE GASOLINA: ", round(galonesUsados, 2), "gal")
        print("COSTO: $", round(galonesUsados*listaPrecios[gasolinera - 1]))
        print("")
        print("0.Volver al menu")
        opcion = int(input("Ingrese una opcion: "))
        
        if opcion == 0:
            opcion = 1
            Menu_Principal()
        elif opcion != 0:
            print("")
            print("Opcion invalida, intente nuevamente")
        else:
            break
    
    return 
    

def Menu_Principal():
    modeloCarro = 1
    inicioRuta = 1
    finalRuta = 1
    gasolinera = 1
    while True:
        print("-------MENU-------")
        print("")
        print("1.Elegir modelo de automovil")
        print("2.Seleccionar ruta")
        print("3.Seleccionar precio segun gasolinera")
        print("4.Calcular gasto de gasolina")
        print("0.Salir del programa")
        print("")
        opcion = int(input("Ingrese una opción: "))
        if opcion == 0:
            sys.exit()
        elif opcion < 0 or opcion > 4:
            limpiarTerminal()
            print("Opcion invalida, intente nuevamente")
            time.sleep(2)
            limpiarTerminal()
            
        elif opcion == 1:
            limpiarTerminal()
            modeloCarro = Menu_1()
            if modeloCarro == None:
                modeloCarro = 1
        elif opcion == 2:
            limpiarTerminal()
            inicioRuta, finalRuta = Menu_2()
        elif opcion == 3:
            limpiarTerminal()
            gasolinera = Menu_3()
        else:
            limpiarTerminal()
            Menu_4(modeloCarro, inicioRuta, finalRuta, gasolinera, listaCarros, listaLocalidades, listaGasolineras)
    

   
Menu_Principal()
