menu = "1. Registrar Alumno\n 2. Registrar Notas\n 3. Buscar Estudiante\n 4. Salida  "
subMenuNotas = "1. Parciales\n 2. Quices\n 3. Trabajos\n 4. Regresar al menu principal"
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