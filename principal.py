import os
import menus
import alumnos as st

alumnos={}
isActive = True
opMenu=0
while isActive:
    os.system("cls")
    try:
        opMenu= menus.menuPrincipal()
    except ValueError:
        print("Error al dato de ingreso")
        os.system("pause")
    else:
        if(opMenu==1):
            rta = "S"
            while(rta in ["S", "s"]):
                os.system("cls")
                alumnos.update(st.regAlumno())
                rta = input("Desea registrar otro alumno S(si) o N (no)").upper()
        elif(opMenu==3):
            codAlumno = input("ingrese el codigo del alumno")
            st.buscarAlumno(codAlumno,alumnos)
        if(opMenu==4):
            isActive=False