import pickle

class Alumno:
    def __init__(self, nombre, apellido, edad, nacionalidad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.nota = None  # Inicialmente la nota es None, ya que se asignará más tarde
        self.nacionalidad = nacionalidad

    def leerNota(self):
        try:
            nota = float(input(f"Ingrese nota para {self.nombre} {self.apellido}: "))
            if 0 <= nota <= 20:
                self.nota = nota
                print(f"Nota registrada correctamente: {self.nota}")
            else:
                print("La nota debe estar en el rango de 0 a 20. Inténtelo de nuevo.")
                self.leerNota()
        except ValueError:
            print("Error: Ingrese un número válido para la nota. Inténtelo de nuevo.")
            self.leerNota()

    def registrarNota(self, notaAlumno):
        if 0 <= notaAlumno <= 20:
            self.nota = notaAlumno
            print(f"Nota registrada correctamente: {self.nota}")
        else:
            print("La nota debe estar en el rango de 0 a 20. Inténtelo de nuevo.")
            self.registrarNota()

    def __str__(self):
        return f"{self.nombre} {self.apellido}, Edad: {self.edad}, Nacionalidad: {self.nacionalidad}, Nota: {self.nota}"

def guardarAlumnos(alumnos):
    with open('alumnos_data.pkl', 'wb') as file:
        pickle.dump(alumnos, file)

def cargarAlumnos():
    try:
        with open('alumnos_data.pkl', 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return []



