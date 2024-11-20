import random
import csv
from variables import puntuaciones, puntos, preguntas_y_respuestas,jugadores, puntuacion

def selecion_pyr(preguntas_y_respuestas):
    pyr_seleccionadas = []
    pyr_seleccionadas = random.sample(preguntas_y_respuestas,10)
    return pyr_seleccionadas

def menu():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Jugar")
        print("2. Reglas")
        print("3. Ranking")
        print("4. Salir \n")
       
        opcion = input("Selecciona una opción: ")
        
        match opcion:
            case "1":
                jugar()
            case "2":
                reglas()
                input("\nEnter para salir: ")
            case "3":
                imprimir_ranking(archivo_csv="data.csv")
                input("\nEnter para salir: ")
                
            case "4":
                print("Saliendo del juego. ¡Hasta la próxima!")
                break
            case _:
                print("Opción no válida. Por favor, intenta de nuevo.")

def reglas():
    """Función para mostrar las reglas del juego."""
    print("¡100 Programadores Dicen!")
    print("----- REGLAS DEL JUEGO -----")
    print("1. El jugador deberá responder las preguntas correctamente.")
    print("2. Cada respuesta correcta sumará puntos.")
    print("3. El jugador tendrá un margén de error de 3 intentos hasta pasara a la siguiente pregunta.")
    print("4. El jugador puede revisar el ranking después de jugar.")
    print("5. Para salir, elija la opción 'Salir' en el menú.")
    print("------------------------------")

def agregar_puntuacion(nombre, puntuacion, archivo_csv="data.csv"):
    datos = []
    nombre_existente = False
    with open(archivo_csv, mode="r", newline="") as archivo:
            lector_csv = csv.reader(archivo)
            for fila in lector_csv:
                if fila and fila[0] == nombre:  #solo si existe una fila con data
                    puntuacion_arch = int(fila[1]) # convierto la puntuacion str a int para comparar
                    # comparar puntuaciones y actualizar solo si la nueva es mayor si el nombre ya está
                    if puntuacion > puntuacion_arch:
                        datos.append([nombre, puntuacion])  # actualizamos su puntuación

                    else:
                        datos.append(fila)  
                    nombre_existente = True
                else:
                    datos.append(fila)
    
    if not nombre_existente:
        datos.append([nombre, puntuacion])

    with open(archivo_csv, mode="w", newline="") as archivo:
        escritor_csv = csv.writer(archivo)
        escritor_csv.writerows(datos)
    
def jugar():
    reso = selecion_pyr(preguntas_y_respuestas)
    nombre_jugador = input("\nCual es tu nombre? ").strip()
    
    puntuaciones[nombre_jugador] = 0
    print(f"¡Preparate {nombre_jugador} que la partida comenzará en breve..!")
    
    for i in range(len(reso)):
        intentos = 1
        respuestas_correctas = 0
        respuestas_ingresadas = []
        print(f"\nPregunta {i+1}: {reso[i][0]}")

        while (intentos > 0):
            num = "R: "
            eleccion = input("Ingrese su respuesta: ")

            while (eleccion in respuestas_ingresadas):
                eleccion = input("Respuesta Ya Ingresada. Ingrese otra: ")

            if buscar_respuesta(reso[i][1], eleccion):
                puntos_obtenidos = puntaje_respuesta(reso[i][1],eleccion)
                puntuaciones[nombre_jugador] += puntos_obtenidos 
                print(f"¡Respuesta Correcta! Tu puntuación ahora es: {puntuaciones[nombre_jugador]}")

                match puntos_obtenidos:
                    case 80:
                        print("¡+80 puntos!")
                    case 60:
                        print("¡+60 puntos!")
                    case 40:
                        print("¡+40 puntos!")
                    case 20:
                        print("¡+20 puntos!")
                    case _:
                        print("")

                respuestas_correctas += 1
                respuestas_ingresadas.append(eleccion)
                if (respuestas_correctas == len(reso[i][1])):
                    break
            else:
                print("¡Respuesta Incorrecta!")
                print("""   """)
                intentos -= 1
        for k in range(4):
            print(num, end=" ")
            print(reso[i][1][k])
        
    agregar_puntuacion(nombre_jugador, puntuaciones[nombre_jugador])

    print(f"\nPuntuación Final: {puntuaciones[nombre_jugador]}\n")
    if puntuaciones[nombre_jugador] > 2000:
        print(f"Superaste los 2000 puntos, sos un groso")
    elif 1000 < puntuaciones[nombre_jugador] > 2000:
        print(f"Superaste los 1000 puntos... ni tan bien ni tan mal eh")
    else: 
        print(f"y... no llegar a los 1000 puntos es un poco triste\npero el intento es lo que cuenta no?...")
        
def imprimir_ranking(archivo_csv="puntuaciones.csv"):
    
    jugadores = []
    with open(archivo_csv, mode="r") as archivo:
        lector_csv = csv.reader(archivo)

        for fila in lector_csv:
            nombre = fila[0]
            puntuacion = fila[1]
            jugadores.append((nombre, puntuacion))
        #sorte ordena, le paso jugadores, (nombre,puntuacion, key=lambda x: x[1], funcion lambda x:toma un elemento x de la lista (una tupla) y devuelve x[1] / (ordena la puntuacion) de manera decreciente con reverse
    jugadores_ordenados = sorted(jugadores, key=lambda x: x[1], reverse=True)
    
    print("""--- Ranking ---""")
    for posicion, (nombre, puntuacion) in enumerate(jugadores_ordenados, start=1):
        print(f"{posicion}. {nombre}: {puntuacion} puntos")

def buscar_respuesta(respuestas: list[list], respuesta_ingresada: str) -> bool:
    """Busca la respuesta ingresada por el usuario y verifica si existe o no en las respuestas posibles.\n
    Parámetros: respuestas (list[list]), respuesta_ingresada (str).\n
    Retorno: respuesta_encontrada (bool)."""

    if (respuesta_ingresada in respuestas):
        respuesta_encontrada = True
    else:
        respuesta_encontrada = False
    
    return respuesta_encontrada

def puntaje_respuesta(respuestas,eleccion):
    puntuacion = 0
    
    for i in range(len(respuestas)):
        if eleccion == respuestas[i]:
            puntuacion = puntos[i]
            break
    return puntuacion


        