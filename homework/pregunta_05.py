"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    dicc = {}
    with open("files\\input\\data.csv", "r") as archivo:
        for linea in archivo:
            #se dividen las columnas por las tabulaciones
            columnas = linea.strip().split("\t")
            val = int(columnas[1])
            letra = columnas[0]

            if letra in dicc:
                dicc[letra].append(val)
                dicc[letra].append(val)
            else:
                dicc[letra] = [val]

    solucion = []
    for letra, valores in sorted(dicc.items()):  
        maximo = max(valores)  
        minimo = min(valores)  
        solucion.append((letra, maximo, minimo))  
    return solucion

print("La solucion es")
print(pregunta_05())
