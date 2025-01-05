"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
    dicc = {}
    with open("files/input/data.csv", "r") as archivo:
        for linea in archivo:
            #se dividen las columnas por las tabulaciones
            columnas = linea.strip().split("\t")  
            letra = columnas[0]

            if letra in dicc:
                dicc[letra] += 1
            else:
                dicc[letra] = 1

        solucion = sorted(dicc.items())
    
    return solucion

print("La solucion es")
print(pregunta_02())

