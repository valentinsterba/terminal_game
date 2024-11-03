from variables import jugadores, puntuaciones,preguntas, respuestas, puntos, puntuacion

def menu():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Jugar")
        print("2. Reglas")
        print("3. Ranking (NO DISPONIBLE)")
        print("4. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        match opcion:
            case "1":
                jugar()
            case "2":
                reglas()
            case "3":
                mostrar_ranking()
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

def jugar():
    
    nombre_jugador = input("Cual es tu nombre? ").strip()
    while nombre_jugador in jugadores:
        print("El nombre está ocupado, por favor elija otro.")
        nombre_jugador = input("¿Cuál es tu nombre? ").strip()
    
    jugadores.add(nombre_jugador)
    puntuaciones[nombre_jugador] = 0
    print(f"¡Preparate {nombre_jugador} que la partida comenzará en breve..!")
    
    for i in range(len(preguntas)):
        intentos = 3
        respuestas_correctas = 0
        respuestas_ingresadas = []
        print(f"\nPregunta {i+1}: {preguntas[i]}")

        while (intentos > 0):
            eleccion = input("Ingrese su respuesta: ")

            while (eleccion in respuestas_ingresadas):
                eleccion = input("Respuesta Ya Ingresada. Ingrese otra: ")

            if buscar_respuesta(respuestas[i], eleccion):
                puntos_obtenidos = puntaje_respuesta(respuestas,eleccion)
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
                if (respuestas_correctas == len(respuestas[i])):
                    break
            else:
                print("¡Respuesta Incorrecta!")
                intentos -= 1
        
        print(f"Respuestas: {respuestas[i]}")
    
    print(f"Puntuación Final: {puntuaciones[nombre_jugador]}")
    if puntuaciones[nombre_jugador] > 2000:
        print(f"Superaste los 2000 puntos, sos un groso")
    elif 1000 < puntuaciones[nombre_jugador] > 2000:
        print(f"Superaste los 1000 puntos... ni tan bien ni tan mal eh")
    else: 
        print(f"y... no llegar a los 1000 puntos es un poco triste\npero el intento es lo que cuenta no?...")
        
    

    

def mostrar_ranking():
    if puntuaciones:
        print("\nRanking de puntajes: ")
        ranking_ordenado = sorted(puntuaciones, reverse=True)
        for puntaje in ranking_ordenado:
            print(f"{puntaje} puntos")
    else:
        print("\nNo hay puntajes registrados aun. Participa para ser el primero en el ranking!")
        #PROXIMAMENTE ...
        #EN LA BUILD 2.0


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
        for j in range(len(respuestas[i])):
            if eleccion == respuestas[i][j]:
                puntuacion += puntos[j]
            
    return puntuacion


        