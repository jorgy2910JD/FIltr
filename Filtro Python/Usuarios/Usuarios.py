import json
import os
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
      print("3. Menú Camper")
      print("4. Salir")  















registro_usuario() 
