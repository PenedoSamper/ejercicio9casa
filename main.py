import persistencia_json

lista_coche = []
while True:
    marcacoche = input("Marca coche: ")
    if marcacoche == "fin":
        break
    modelo = input("Modelo: ")
    combustible = input("Tipo combustible: ")
    cilindrada = input("Cilindrada: ")
    linea= {}
    linea["Marca coche: "] = marcacoche
    linea["Modelo: "] = modelo
    linea["Combustible: "] = combustible
    linea["Cilindrada: "] = cilindrada
    lista_coche.append(linea)
print("Lista coche:\n", lista_coche)

persistencia_json.dump(persistencia_json.dumps(lista_coche), open("coches.txt", "w"))

lista_coches = []