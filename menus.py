import os
import notas
import alumnos
menu = "1. Registrar Alumno\n 2. Registrar Notas\n 3. Buscar Estudiante\n 4. Salida  "
subMenuDeNotas = "1. Parciales\n 2. Quices\n 3. Trabajos\n 4. Regresar al menu principal"
hasError = True
def menuPrincipal() -> int:
    global hasError
    hasError = True
    print(menu)
    while (hasError==True):
        try:
            hasError = False
            return int(input(":)"))
        except ValueError:
            hasError=True


def subMenuNotas() -> int:
    global hasError
    hasError = True
    print(subMenuDeNotas)
    os.system("pause")
    while (hasError==True):
        try:
            hasError = False
            return int(input(":)"))
            
        except ValueError:
            hasError=True

def menuNotas(alumnos : dict):
    os.system("cls")
    print(alumnos)
    os.system("pause")
    header ="""
    **********************************
    *** Menu de registro de notas  *** 
    **********************************
    """
    isActiveMenu = True
    while (isActiveMenu):
        try:
            opMenu = int(input(":)"))
        except ValueError:
            print("Opcion invalida... recuerde que son enteros")
        else:
            if(opMenu==1):
                print("Parciales")
                notas.addgrades(alumnos, "parciales")
            elif(opMenu==2):
                print("Quices")
                notas.addgrades(alumnos, "quices")
            elif(opMenu==3):
                print("Trabajos")
                notas.addgrades(alumnos, "trabajos")
            elif(opMenu==4):
                print("Regresar al menu principal")
                isActiveMenu = False
            else:
                print("Opción no valida")
                os.system("pause")