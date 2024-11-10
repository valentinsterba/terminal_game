"""import random
from variables import jugadores, puntuaciones,preguntas, respuestas, puntos, puntuacion
with open('datos_usuarios.json', mode='w+') as archivo:
    datos = archivo.readlines()

preguntas_y_respuestas = [
    ["¿Qué significa 'bancar'?", ["Apoyar", "Financiar", "Sostener", "Perdonar"]],
    ["¿Qué postre tiene dulce de leche?", ["Chocotorta", "Flan", "Pastelito", "Helado"]],
    ["¿Qué es un 'cheto'?", ["Pijo", "Rico", "Snob", "Fashion"]],
    ["¿Qué se lleva a una merienda?", ["Facturas", "Tortas", "Dulce de leche", "Galletitas"]],
    ["¿Qué es 'la 12'?", ["La hinchada de Boca", "Un barrio", "Un club", "Un equipo"]],
    ["¿Qué postre es un clásico argentino?", ["Flan", "Helado", "Chocotorta", "Budin"]],
    ["¿Qué se lleva a un asado?", ["Carne", "Pan", "Ensalada", "Vino"]],
    ["¿Cuál es el barrio más famoso por su tango?", ["La Boca", "San Telmo", "Palermo", "Recoleta"]],
    ["¿Qué palabra se usa para referirse a un amigo?", ["Che", "Amigo", "Flaco", "Pibe"]],
    ["¿Qué comida se come en un 'domingo' familiar?", ["Asado", "Pizza", "Pastas", "Sushi"]],
    ["¿Qué famoso artista es un ícono del rock argentino?", ["Charly Garcia", "Fito Paez", "Gustavo Cerati", "Andres Ciro"]],
    ["¿Cuál es un programa de televisión popular en Argentina?", ["Gran Hermano", "Showmatch", "MasterChef", "CQC"]],
    ["¿Qué bebida es típica para brindar?", ["Champagne", "Fernet", "Vino", "Cerveza"]],
    ["¿Qué instrumento se asocia al tango?", ["Bandoneon", "Piano", "Guitarra", "Violin"]]
]
def puntaje_respuesta(respuestas,eleccion):
    puntuacion = 0
    for i in range(len(respuestas)):
        for j in range(len(respuestas[i])):
            if eleccion == respuestas[i][j]:
                puntuacion += puntos[j]
            
    return puntuacion

def buscar_respuesta(respuestas: list[list], respuesta_ingresada: str) -> bool:
    #Busca la respuesta ingresada por el usuario y verifica si existe o no en las respuestas posibles.\n
    #Parámetros: respuestas (list[list]), respuesta_ingresada (str).\n
    #Retorno: respuesta_encontrada (bool).

    if (respuesta_ingresada in respuestas):
        respuesta_encontrada = True
    else:
        respuesta_encontrada = False
    
    return respuesta_encontrada

def selecion_pyr(preguntas_y_respuestas):
    pyr_seleccionadas = []
    pyr_seleccionadas = random.sample(preguntas_y_respuestas,5)
    return pyr_seleccionadas


def jugar():
    pyr = selecion_pyr(preguntas_y_respuestas)
    nombre_jugador = input("Cual es tu nombre? ").strip()
    while nombre_jugador in jugadores:
        print("El nombre está ocupado, por favor elija otro.")
        nombre_jugador = input("¿Cuál es tu nombre? ").strip()
    
    jugadores.add(nombre_jugador)
    puntuaciones[nombre_jugador] = 0
    print(f"¡Preparate {nombre_jugador} que la partida comenzará en breve..!")

    for i in range(len(pyr)):
        intentos = 1
        respuestas_correctas = 0
        respuestas_ingresadas = []
        print(f"\nPregunta {i+1}: {pyr[i][0]}")
        
        while (intentos > 0):
            eleccion = input("Ingrese su respuesta: ")

            while (eleccion in respuestas_ingresadas):
                eleccion = input("Respuesta Ya Ingresada. Ingrese otra: ")

            if buscar_respuesta(pyr[i][1], eleccion):
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
                if (respuestas_correctas == len(pyr[i][1])):
                    break
            else:
                print("¡Respuesta Incorrecta!")
                intentos -= 1
        
        print(f"Respuestas: {pyr[i][1]}")


jugar()
"""
text = input("enter; ")
