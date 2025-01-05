"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """

    dicc = {}
    with open("files/input/data.csv", "r") as archivo:
        for linea in archivo:
            columnas = linea.strip().split("\t")
            diccionario_texto = columnas[4]

            # Dividir los pares de clave-valor por la coma
            pares = diccionario_texto.split(",")  
            for par in pares:
                try:
                    clave, valor = par.split(":")
                    valor = int(valor)  # Convertir el valor a entero

                    if clave not in dicc:
                        dicc[clave] = []

                    dicc[clave].append(valor)
                except ValueError:
                    # Manejar posibles errores de formato
                    print(f"Error procesando el par: {par}")

    # Generar la lista de resultados
    resultado = [(clave, min(valores), max(valores)) for clave, valores in dicc.items()]
    resultado.sort()

    return resultado

print("La solución es:")
print(pregunta_06())