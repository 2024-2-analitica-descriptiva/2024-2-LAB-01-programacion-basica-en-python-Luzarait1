"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene  el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera  columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]

    """

    dicc = {}  
    with open("files\\input\\data.csv", "r") as archivo:
        for linea in archivo:
            columnas = linea.strip().split("\t")
            
            try:
                valor_columna2 = int(columnas[1])  
                letra_columna0 = columnas[0]  

                if valor_columna2 in dicc:
                    if letra_columna0 not in dicc[valor_columna2]:
                        dicc[valor_columna2].append(letra_columna0)
                else:
                    dicc[valor_columna2] = [letra_columna0]  
                
            except (ValueError, IndexError) as e:
                print(f"Advertencia: línea no válida -> {linea.strip()}")

    resultado = sorted((clave, sorted(set(valor))) for clave, valor in dicc.items())
    return resultado

print("La solución es:")
print(pregunta_08())