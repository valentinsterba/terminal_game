import random

class Entidad :
    envenenado = False
    curando = False

    def __init__(self, nombre: str, fuerza: float, salud: int, tipo: str):
        self.nombre = nombre
        self.fuerza = fuerza
        self.salud = salud
        self.salud_maxima = salud
        self.tipo = tipo
        self.turnos_envenenado = 0
        self.turnos_curando = 0
    
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}\nFuerza: {self.fuerza}\nSalud: {self.salud}\nTipo: {self.tipo}")

    def ataque_basico(self):
        dano = self.fuerza
        return dano
    
    def aplicar_veneno(self):
        if self.envenenado:
            self.salud -= 4
            print(f"{self.nombre} ha recibido veneno y ha perdido 4 de salud. Salud restante: {self.salud}")
            self.turnos_envenenado -= 1
        if self.turnos_envenenado == 0:
            self.envenenado = False
            

    def aplicar_curacion(self):
        if self.curando:
            self.salud += 4
            if self.salud >= self.salud_maxima:
                self.salud = self.salud_maxima
            print(f"{self.nombre} se ha curado y ahora tiene {self.salud} de salud.")
        
        

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
                print(f"{self.nombre} intentó un ataque letal, pero no fue exitoso. La salud de {enemigo.nombre} es demasiado alta.")
    
    def envenenar(self, enemigo):
        enemigo.envenenado = True
        if isinstance(enemigo, Pleurotus_Ostreatus):
            enemigo.turnos_envenenado = 4
            print(f"{self.nombre} ha envenenado a {enemigo.nombre} por {enemigo.turnos_envenenado} rondas.")
        else: 
            enemigo.turnos_envenenado = 2
            print(f"{self.nombre} ha envenenado a {enemigo.nombre} por {enemigo.turnos_envenenado} rondas.")
            

        

class Pleurotus_Ostreatus(Entidad):
    pass

personaje = Entidad("InserteNombre",5.0,20,"InserteTipo")
amanita = Amanita_Muscaria("Amanita Muscaria", 6.0, 100, "Tóxico")
pleurotus = Pleurotus_Ostreatus("Pleurotus_Ostreatus", 5.5, 130, "Curación")
amanita.ataque_esporas(personaje)
amanita.mostrar_info()
personaje.mostrar_info()
amanita.envenenar(personaje)