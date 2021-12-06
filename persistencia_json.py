import persistencia_json

def store(variable, nombrearchivo):
    variable = input(print("Introduce una variable: "))
    nombrearchivo = input(print("Nombre del archivo: "))
    persistencia_json.dump(persistencia_json.dumps(nombrearchivo), open(nombrearchivo, "w"))
def retrieve(nombrearchivo):
    return persistencia_json.load