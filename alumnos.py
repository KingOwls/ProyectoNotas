import os
def regAlumno(diccAlumnos :  dict) :
    codigo = input("ingrese el codigo del estudiante:   ")
    nombre = input("ingrese el nombre del estudiante:   ")
    edad = int(input("ingrese la edad del estudiante:   "))
    
    alumno ={
        "codigo":codigo,
        "nombre":nombre,
        "edad":edad,
        "notas": {
            "parciales":[],
            "quipes":[],
            "trabajos":[]
        }
    }
    return{codigo:alumno}

def buscarAlumno(codAlumno : str,Alumno : dict):
    data = Alumno.get(codAlumno,-1)
    if (type(data) == dict):
        for llave,valor in data.items():
            print(f"{llave} : {valor}")
        os.system("pause")
    else:
        print(f"no se encontro el estudiante con el codigo {codAlumno}")
        os.system("pause")