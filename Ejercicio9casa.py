class rueda:

    def __init__(self):
        self.ancho=input("Ancho de la rueda:")
        self.rodadura=input("Rodadura de la rueda:")
        self.diametro=input("Diametro de la rueda:")
        self.presion= 0
    def set_pressure(self):
        self.presion= input("Presión de la rueda:")

    def print_info(self):
        print(self.ancho,"/",self.rodadura,"R",self.diametro)
    def print_pressure(self):
        self.pressure= self.presion
        print(self.pressure, "bares")

# bloque principal

rueda1= rueda()
rueda1.set_pressure()
rueda1.print_info()
rueda1.print_pressure()
