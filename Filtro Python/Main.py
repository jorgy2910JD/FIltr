import json
import os

def limpiar_terminal():
    if os.name=="nt":
        os.system("cls")
    else:
        os.system("clear")

def registro_usuario():
  while True:
    print("""
            **********************
            *                    *
            * REGISTRO DE USUARIO *
            *                    *
            **********************
            """)
    print("Bienvenido Usuario!")
    print("Que deseas hacer el día de hoy?")
    print("Registrame------------------->(1) ")
    print("Iniciar sesión--------------->(2) ") 
    with open("JSON/Datos.json", "r") as outfile:
        Data = json.load(outfile)

    newU = {}
    newU["cédula"] = int(input("*Ingresa tu numero de documento por favor: "))
    newU["nombres"] = input("*Ingrese los nombres                                  : ")
    newU["apellido"] = input("*Ingresa los apellidos                               : ")
    newU["direccion"] = input("*Ingrese la Dirección del camper que deseas agregar : ")
    newU["N_celular"] = input("*Ingrese el numero de celular: ")
    newU["N_fijo"] = input("*Ingrese el numero de teléfono fijo: ")
 
    Data["Usuarios"].append(newU)

    with open("JSON/Campers.json", "w") as outfile:
        json.dump(Data, outfile, indent=4) 


def menu_principal():
    while True:
        print("""
                **********************
                *    MENÚ PRINCIPAL  *
                **********************
                """)
        print("Seleccione una opción:")
        print("Registro usuario------>(1)")
        print("Categorías de usuario--->(2)")
        print(" Info plan Hogar------>(3)")
        print("planes postpago--------->(4)")
        print("4. Salir")  

        opcionM= int(input("Ingresa la opcion que desees por favor"))

        if opcionM == 1:
           print(registro_usuario) 





def categorias_usuario():
   while True:
      print ("""
                **********************
                *Categorias de Usuario*
                **********************
                """)
      print("Seleccione una opción:")
      print("Nuevos clientes------>(1)")
      print("Clientes regulares--->(2)")
      print("Clientes leales------>(3)")
      print("Salir---------------->(4)")  



def plan_hogar(): 
   while True:
      print ("""
                **********************
                *    Planes hogar    *
                **********************
                """)
      print("Seleccione una opción:")
      print("Internet/television------>(1)")
      print("Internet/television/Telefonia Fija--->(2)")
      print("Salir---------------->(4)")  

      opcionP= int(input("Selecciona la opcion que desees: "))

      if opcionP == 1: 
         print("Los planes de Internet/Televisión son los siguientes: ") 
         print("Internet fibra Optica 200 mbps + 86 canales(40 HD) a 91.000$ ") 
         print("Internet fibra Optica 300 mbps + 110 canales(55 HD) a 124.000$ ") 
         print("Internet fibra Optica 500 mbps + 120 canales(65 HD) a 145.000$ ")
         print("Internet fibra Optica 900 mbps + 120 canales(70 HD) a 176.000$ ")


      elif opcionP == 2: 

        print ( )
