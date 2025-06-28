# Diccionario para almacenar los datos de los estudiantes.
# La clave será el número de identificación del estudiante (string),
# y el valor será otro diccionario con 'nombre', 'edad' y 'notas'.
estudiantes = {}

def registrar_estudiante():
    # Permite al usuario registrar un nuevo estudiante solicitando su nombre,
    # número de identificación, edad y una lista de al menos 3 notas.
    # Valida la entrada para el ID, la edad y las notas.
    print("\n--- Registrar Estudiante ---")
    while True:
        try:
            identificacion = input("Ingrese el número de identificación del estudiante: ")
            if not identificacion.strip(): # Verifica que el ID no esté vacío o solo contenga espacios
                raise ValueError("La identificación no puede estar vacía.")
            if identificacion in estudiantes:
                print("¡Error! Ya existe un estudiante con esta identificación. Intente de nuevo.")
                continue # Continúa el ciclo para pedir un ID diferente
            break # Sale del ciclo si el ID es válido y único
        except ValueError as e:
            print(f"Error: {e}")

    nombre = input("Ingrese el nombre del estudiante: ")
    while not nombre.strip(): # Valida que el nombre no esté vacío
        print("El nombre no puede estar vacío. Por favor, ingrese un nombre.")
        nombre = input("Ingrese el nombre del estudiante: ")

    while True:
        try:
            edad = int(input("Ingrese la edad del estudiante: "))
            if edad <= 0:
                raise ValueError("La edad debe ser un número positivo.")
            break # Sale del ciclo si la edad es válida
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero para la edad.")

    notas = [] # Inicializa una lista para almacenar las notas
    while True:
        try:
            num_notas = int(input("¿Cuántas notas desea ingresar (mínimo 3)? "))
            if num_notas < 3:
                print("Debe ingresar al menos 3 notas.")
                continue # Pide de nuevo la cantidad de notas si es menor a 3
            break # Sale del ciclo si el número de notas es válido
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")

    # Bucle 'for' para pedir cada una de las notas
    for i in range(num_notas):
        while True:
            try:
                nota = float(input(f"Ingrese la nota {i + 1}: "))
                if not (0 <= nota <= 5):  # Asumiendo que las notas están entre 0 y 5
                    raise ValueError("La nota debe estar entre 0 y 5.")
                notas.append(nota) # Agrega la nota a la lista
                break # Sale del ciclo interno si la nota es válida
            except ValueError as e:
                print(f"Entrada inválida: {e} Por favor, ingrese un número válido para la nota.")

    # Almacena toda la información del estudiante en el diccionario 'estudiantes'
    estudiantes[identificacion] = {
        "nombre": nombre,
        "edad": edad,
        "notas": notas
    }
    print(f"Estudiante '{nombre}' registrado exitosamente.")

def calcular_promedio(notas):
    #Calcula el promedio de una lista de notas.
    if not notas: # Evita la división por cero si la lista de notas está vacía
        return 0
    return sum(notas) / len(notas)

def consultar_estudiante():
    # Permite al usuario consultar la información de un estudiante por su ID,
    # mostrando su edad, lista de notas y el promedio.
    # Notifica si el estudiante no existe.
    print("\n--- Consultar Estudiante ---")
    identificacion = input("Ingrese el número de identificación del estudiante a consultar: ")

    if identificacion in estudiantes:
        estudiante = estudiantes[identificacion] # Obtiene los datos del estudiante
        print(f"\n--- Información del Estudiante ---")
        print(f"Nombre: {estudiante['nombre']}")
        print(f"Identificación: {identificacion}")
        print(f"Edad: {estudiante['edad']}")
        print("Notas:")
        # Bucle 'for' para mostrar cada nota
        for i, nota in enumerate(estudiante['notas']):
            print(f"  - Nota {i + 1}: {nota}")
        promedio = calcular_promedio(estudiante['notas'])
        print(f"Promedio: {promedio:.2f}") # Formatea el promedio a dos decimales
    else:
        print(f"¡Error! No se encontró ningún estudiante con la identificación '{identificacion}'.")

def actualizar_notas():
    # Permite al programa modificar las notas de un estudiante existente.
    
    print("\n--- Actualizar Notas ---")
    identificacion = input("Ingrese el número de identificación del estudiante cuyas notas desea actualizar: ")

    if identificacion in estudiantes:
        estudiante = estudiantes[identificacion]
        print(f"Notas actuales de {estudiante['nombre']}:")
        # Bucle 'for' para mostrar las notas actuales
        for i, nota in enumerate(estudiante['notas']):
            print(f"  - Nota {i + 1}: {nota}")

        nuevas_notas = []
        num_notas_actuales = len(estudiante['notas']) # Mantiene la cantidad de notas existentes
        print(f"Ingrese las {num_notas_actuales} nuevas notas para {estudiante['nombre']}:")
        # Bucle 'for' para pedir las nuevas notas
        for i in range(num_notas_actuales):
            while True:
                try:
                    nota = float(input(f"Ingrese la nueva nota {i + 1}: "))
                    if not (0 <= nota <= 5):
                        raise ValueError("La nota debe estar entre 0 y 5.")
                    nuevas_notas.append(nota)
                    break
                except ValueError as e:
                    print(f"Entrada inválida: {e} Por favor, ingrese un número para la nota.")
        estudiante['notas'] = nuevas_notas # Actualiza la lista de notas del estudiante
        print(f"Notas del estudiante '{estudiante['nombre']}' actualizadas exitosamente.")
    else:
        print(f"¡Error! No se encontró ningún estudiante con la identificación '{identificacion}'.")

def eliminar_estudiante():
    # Permite al usuario eliminar un registro de estudiante utilizando su número de identificación.
    print("\n--- Eliminar Estudiante ---")
    identificacion = input("Ingrese el número de identificación del estudiante a eliminar: ")

    if identificacion in estudiantes:
        nombre_eliminado = estudiantes[identificacion]['nombre']
        del estudiantes[identificacion] # Elimina el estudiante del diccionario
        print(f"Estudiante '{nombre_eliminado}' con identificación '{identificacion}' eliminado exitosamente.")
    else:
        print(f"¡Error! No se encontró ningún estudiante con la identificación '{identificacion}'.")

def ver_todos_los_estudiantes():
    # Muestra una lista con todos los estudiantes registrados y su promedio general.
    # Presenta esta información de forma clara.
    print("\n--- Listado General de Estudiantes ---")
    if not estudiantes: # Verifica si el diccionario de estudiantes está vacío
        print("No hay estudiantes registrados en el sistema.")
        return

    # Bucle 'for' para recorrer los elementos del diccionario (ID y datos del estudiante)
    for identificacion, datos_estudiante in estudiantes.items():
        nombre = datos_estudiante['nombre']
        promedio = calcular_promedio(datos_estudiante['notas'])
        print(f"---")
        print(f"Identificación: {identificacion}")
        print(f"Nombre: {nombre}")
        print(f"Promedio: {promedio:.2f}")
    print("---\n") # Separador visual

def mostrar_menu():
    #Muestra el menú interactivo al usuario.
    print("\n----- Sistema de Gestión Académica -----")
    print("1. Registrar estudiante")
    print("2. Consultar estudiante")
    print("3. Actualizar notas")
    print("4. Eliminar estudiante")
    print("5. Ver todos los estudiantes")
    print("6. Salir")
    print("---------------------------------------")

def main():
    # Función principal que ejecuta el programa de gestión académica de estudiantes.
    # Mantiene el programa en ejecución hasta que el usuario decida salir.
    while True: # Bucle 'while' principal para mantener el programa en ejecución
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            registrar_estudiante()
        elif opcion == '2':
            consultar_estudiante()
        elif opcion == '3':
            actualizar_notas()
        elif opcion == '4':
            eliminar_estudiante()
        elif opcion == '5':
            ver_todos_los_estudiantes()
        elif opcion == '6':
            print("Saliendo del programa. ¡Hasta pronto!")
            break # Sale del bucle 'while' y finaliza el programa
        else:
            print("Opción inválida. Por favor, seleccione una opción del 1 al 6.")

if __name__ == "__main__":
    main()