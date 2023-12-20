import os
def addgrades(alumno : dict, categoria : str):
    dataNotas = alumno.get("notas")
    evaluacion = dataNotas.get(categoria)
    nota = float(input(f'ingrese la nota de {alumno.get("nombre").upper()}'))
    evaluacion.append(nota)