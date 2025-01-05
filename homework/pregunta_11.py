"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """

    dicc = {}  
    with open("files/input/data.csv", "r") as archivo:
        for linea in archivo:
            columnas = linea.strip().split("\t") 
            valor_columna_2 = int(columnas[1])  
            letras_columna_4 = columnas[3].split(",") 

            for letra in letras_columna_4:
                if letra in dicc:
                    dicc[letra] += valor_columna_2
                else:
                    dicc[letra] = valor_columna_2

    resultado_ordenado = dict(sorted(dicc.items()))
    return resultado_ordenado

print("La solución es:")
print(pregunta_11())
