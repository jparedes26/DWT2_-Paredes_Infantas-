from alumnos import Alumno, guardarAlumnos, cargarAlumnos

def main():
    print("Bienvenidos al registro de notas")

    alumnos = cargarAlumnos()

    while True:
        comando = input("Ingrese comando (R: Registrar, C: Calificar, P: Promedio, S: Suma, X: Salir): ").upper()

        if comando == 'R':
            nombre = input("Ingrese nombre del alumno: ")
            apellido = input("Ingrese apellido del alumno: ")
            edad = int(input("Ingrese edad del alumno: "))
            nacionalidad = input("Ingrese nacionalidad del alumno: ")

            nuevo_alumno = Alumno(nombre, apellido, edad, nacionalidad)
            alumnos.append(nuevo_alumno)

            print(f"Alumno {nombre} {apellido} registrado exitosamente.")

        elif comando == 'C':
            for alumno in alumnos:
                alumno.leerNota()

        elif comando == 'P':
            if len(alumnos) == 0:
                print("No hay alumnos registrados.")
            else:
                promedio = sum(alumno.nota for alumno in alumnos) / len(alumnos)
                print(f"El promedio de notas para {len(alumnos)} alumnos es: {promedio:.2f}")

        elif comando == 'S':
            if len(alumnos) == 0:
                print("No hay alumnos registrados.")
            else:
                suma_notas = sum(alumno.nota for alumno in alumnos)
                print(f"La suma de notas de {len(alumnos)} alumnos es: {suma_notas}")

        elif comando == 'X':
            guardarAlumnos(alumnos)
            print("Programa terminado.")
            break

        else:
            print("Comando no válido. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()


