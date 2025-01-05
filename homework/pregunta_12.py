"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """

    dicc = {} 
    with open("files\\input\\data.csv", "r") as archivo:
        for linea in archivo:
            columnas = linea.strip().split("\t")
            clave = columnas[0] 
            valores_texto = columnas[4]  
            
            suma_valores = sum(int(valor.split(":")[1]) for valor in valores_texto.split(","))

            if clave in dicc:
                dicc[clave] += suma_valores
            else:
                dicc[clave] = suma_valores  
    
    return dicc

print("La solución es:")
print(pregunta_12())