import random

class Entidad :
    
    def __init__(self, nombre: str, fuerza: float, salud : int, tipo: str):
        self.nombre = nombre
        self.fuerza = fuerza
        self.salud = salud
        self.tipo = tipo
    
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}\nFuerza: {self.fuerza}\nSalud: {self.salud}\nTipo: {self.tipo}")

    def ataque_basico(self):
        dano = self.fuerza
        return dano

class Amanita_Muscaria(Entidad):
    def ataque_esporas(self, enemigo):

        probabilidad_fallo = random.randint(0, 100)
        
        if probabilidad_fallo < 7:
            print(f"{self.nombre} falló el ataque!")
            return 0
               
        else:
            if isinstance(enemigo, Pleurotus_Ostreatus):
                dano = self.fuerza * 1.6
                print(f"{self.nombre} usa Ataque de Esporas a un oponente tipo curación ¡Inflinge {dano} de daño!")
            else:
                dano = self.fuerza
                print(f"¡{self.nombre} ataca al objetivo infligiendo {dano} de daño!")
            
            enemigo.salud -= dano
    
    
    def ataque_letal(self, enemigo):

        if isinstance(enemigo, Pleurotus_Ostreatus):
            if enemigo.salud <= 55:
                dano = enemigo.salud
                enemigo.salud -= dano
                print(f"{self.nombre} usó un ataque letal ¡{enemigo.nombre} fue derrotado!")

        else:
            if enemigo.salud < 30: 
                dano = enemigo.salud 
                enemigo.salud -= dano
                print(f"{self.nombre} usó un ataque letal ¡{enemigo.nombre} fue derrotado!")
            else:
                print(f"{self.nombre} intentó un ataque letal, pero no fue exitoso. La salud de  {enemigo.nombre} es demasiado alta.")
        
class Pleurotus_Ostreatus(Entidad):
    pass

personaje = Entidad("InserteNombre",5.0,20,"InserteTipo")
amanita = Amanita_Muscaria("Amanita Muscaria", 6.0, 100, "Tóxico")
pleurotus = Pleurotus_Ostreatus("Pleurotus_Ostreatus", 5.5, 130, "Curación")
amanita.ataque_esporas(personaje)
amanita.mostrar_info()
personaje.mostrar_info()