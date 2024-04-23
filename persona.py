class Persona:
    def __init__(self, nombre, apellidos):
        self.name = nombre
        self.surname = apellidos

    def saludar(self):
        print ("Hola, me llamo", self.name, self.surname)
    
mon = Persona("Mon", "Maldonado")
fatima = Persona("Fatima", "Garcia")

mon.saludar()
fatima.saludar()

print(fatima.name)