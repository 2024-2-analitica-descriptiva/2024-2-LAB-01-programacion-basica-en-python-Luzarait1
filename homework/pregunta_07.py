"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla
    contiene un valor posible de la columna 2 y una lista con todas las letras
    asociadas (columna 1) a dicho valor de la columna 2.

    Rta/
    [(0, ['C']),
     (1, ['E', 'B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E', 'E', 'D']),
     (4, ['E', 'B']),
     (5, ['B', 'C', 'D', 'D', 'E', 'E', 'E']),
     (6, ['C', 'E', 'A', 'B']),
     (7, ['A', 'C', 'E', 'D']),
     (8, ['E', 'D', 'E', 'A', 'B']),
     (9, ['A', 'B', 'E', 'A', 'A', 'C'])]

    """

    asociaciones = {} 
    with open("files\\input\\data.csv", "r") as archivo:
        for linea in archivo:
            columnas = linea.strip().split("\t")
            
            if len(columnas) >= 3:
                try:
                    valor_columna2 = int(columnas[2]) 
                    letra_columna1 = columnas[0]   

                    if valor_columna2 in asociaciones:
                        asociaciones[valor_columna2].append(letra_columna1)
                    else:
                        asociaciones[valor_columna2] = [letra_columna1]
                except ValueError:
                    print(f"Advertencia: no se pudo procesar la línea -> {linea.strip()}")
            else:
                print(f"Advertencia: línea incompleta o no válida -> {linea.strip()}")

    resultado = sorted(asociaciones.items())
    return resultado

print("La solución es:")
print(pregunta_07())