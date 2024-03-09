"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
import os
import glob

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    suma = 0

    dataset = glob.glob(os.path.join(os.getcwd(), "*.csv"))
    for archivo in dataset:
        with open(archivo, "r") as f:
            for linea in f:
                # print(linea.split('\t')[1])
                suma += int(linea.split('\t')[1])
                
    return suma


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    conteo_letras = {}

    dataset = glob.glob(os.path.join(os.getcwd(), "*.csv"))
    for archivo in dataset:
        with open(archivo, "r") as f:
            for linea in f:
                # Extrae la primera letra de la primera columna de cada línea
                letra = linea.strip()[0]
                # Incrementa el contador correspondiente en el diccionario
                conteo_letras[letra] = conteo_letras.get(letra, 0) + 1

    # Ordena el diccionario por las claves (letras) alfabéticamente y conviértelo en una lista de tuplas
    lista_conteo = sorted(conteo_letras.items())

    # Retorna la lista de tuplas
    return lista_conteo


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    letter_sum = {}

    # Abrir el archivo en modo lectura
    dataset = glob.glob(os.path.join(os.getcwd(), "*.csv"))
    for archivo in dataset:
        with open(archivo, "r") as f:
        # Iterar sobre cada línea del archivo
            for linea in f:
                elementos = linea.strip().split(',')
                # Extraer la letra de la primera columna y el valor de la segunda columna
                letra = elementos[0][0]  # Se asume que la letra está en el primer carácter de la primera columna
                column_value = int(linea.split('\t')[1])  # Se convierte a entero el valor de la segunda columna

                # Sumar el valor de la segunda columna correspondiente a cada letra
                letter_sum[letra] = letter_sum.get(letra, 0) + column_value

    # Ordenar las claves (letras) alfabéticamente y convertirlo en una lista de tuplas
    list_letter_sum = sorted(letter_sum.items())

    # Retornar la lista de tuplas
    return list_letter_sum


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    # Inicializar un diccionario para almacenar la cantidad de registros por cada mes
    month_count = {}

    # Abrir el archivo en modo lectura
    dataset = glob.glob(os.path.join(os.getcwd(), "*.csv"))
    for archivo in dataset:
        with open(archivo, "r") as f:
        # Iterar sobre cada línea del archivo
            for linea in f:
            # Dividir la línea en sus elementos utilizando el delimitador adecuado
                elementos = linea.split()
                # Extraer el mes de la columna 3
                date = elementos[2]
                month = date.split('-')[1].zfill(2)
                # Incrementar el contador del mes correspondiente en el diccionario
                if month in month_count:
                    month_count[month] += 1
                else:
                    month_count[month] = 1
    
    # Ordenar los result por mes y convertirlos en una lista de tuplas
    month_count = sorted(month_count.items())

    return month_count


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    # from collections import defaultdict
    
    # # Crear un diccionario para almacenar los valores máximos y mínimos por letra
    # max_min_por_letra = defaultdict(lambda: (float('-inf'), float('inf')))

    # # Abrir el archivo CSV
    # with open(dataframe, 'r') as f:
    #     for linea in f:
    #         # Dividir la línea en sus elementos utilizando el delimitador adecuado
    #         elementos = linea.split()
    #         letra, valor = elementos[0], int(elementos[1])
    #         # Actualizar los valores máximo y mínimo para la letra actual
    #         max_valor, min_valor = max_min_por_letra[letra]
    #         max_min_por_letra[letra] = (max(max_valor, valor), min(min_valor, valor))

    # # Convertir el diccionario en una lista de tuplas, convirtiendo los valores a enteros
    # result = [(letra, int(max_valor), int(min_valor)) for letra, (max_valor, min_valor) in max_min_por_letra.items()]
    
    # result.sort()
    
    # Crear un diccionario para almacenar los valores máximos y mínimos por letra
    max_min_por_letra = {}

    # Abrir el archivo en modo lectura
    dataset = glob.glob(os.path.join(os.getcwd(), "*.csv"))
    for archivo in dataset:
        with open(archivo, "r") as f:
        # Iterar sobre cada línea del archivo
            for linea in f:
                # Dividir la línea en sus elementos utilizando el delimitador adecuado
                elementos = linea.split()
                letra, valor = elementos[0], int(elementos[1])
                # Actualizar los valores máximo y mínimo para la letra actual
                if letra not in max_min_por_letra:
                    max_min_por_letra[letra] = (float('-inf'), float('inf'))
                max_valor, min_valor = max_min_por_letra[letra]
                max_min_por_letra[letra] = (max(max_valor, valor), min(min_valor, valor))

    # Convertir el diccionario en una lista de tuplas, convirtiendo los valores a enteros
    result = [(letra, int(max_valor), int(min_valor)) for letra, (max_valor, min_valor) in max_min_por_letra.items()]

    # Ordenar la lista de tuplas por la letra
    result.sort()

    # Retornar la lista de tuplas
    return result



def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    # Crear un diccionario para almacenar los valores máximos y mínimos por letra
    min_max_values = {}

    dataset = glob.glob(os.path.join(os.getcwd(), "*.csv"))
    for archivo in dataset:
        with open(archivo, "r") as f:
        # Iterar sobre cada línea del archivo
            for linea in f:
                # Divide la línea en partes usando la coma como separador
                elementos = linea.split()[4]
                partes = elementos.strip().split(',')
                # Iterar sobre cada parte y extraer la clave y el valor
                # Iterar sobre cada parte y extraer la clave y el valor
                for parte in partes:
                    letra, valor = parte.split(':')
                    valor = int(valor)  # Convertir el valor a entero
                    
                    # Verificar si ya existe la clave en el diccionario
                    if letra in min_max_values:
                        # Actualizar el valor mínimo y máximo si es necesario
                        min_max_values[letra] = (min(min_max_values[letra][0], valor), 
                                                 max(min_max_values[letra][1], valor))
                    else:
                        # Si no existe la clave, crear una nueva entrada en el diccionario
                        min_max_values[letra] = (valor, valor)

    # Ordenar el diccionario por clave y devolver una lista de tuplas con las claves y sus valores mínimos y máximos
    result = sorted([(letra, min_max_values[letra][0], min_max_values[letra][1]) for letra in min_max_values])
    return result


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    letters_values = {}

    dataset = glob.glob(os.path.join(os.getcwd(), "*.csv"))
    for archivo in dataset:
        with open(archivo, "r") as f:
        # Iterar sobre cada línea del archivo
            for linea in f:
 # Dividir la línea en columnas utilizando tabulaciones como separador
                columnas = linea.strip().split('\t')

                # Extraer la columna 1 (letras) y la columna 2 (valores)
                letras = columnas[0]
                valores = columnas[1]

                # Convertir la columna 1 a un número entero
                numero = int(valores)

                # Verificar si el número ya está en el diccionario
                if numero in letters_values:
                    letters_values[numero].append(letras)
                else:
                    letters_values[numero] = [letras]
    
    # Ordenar alfabéticamente las letras en la lista asociada a cada valor
    # for valor, letras in letters_values.items():
    #     letters_values[valor] = sorted(letras)

    # Convertir el diccionario en una lista de tuplas
    result = [(numero, letras) for numero, letras in sorted(letters_values.items())]

    return result
# df = pregunta_07("data.csv")
# print(df)



def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    letters_values = {}

    dataset = glob.glob(os.path.join(os.getcwd(), "*.csv"))
    for archivo in dataset:
        with open(archivo, "r") as f:
        # Iterar sobre cada línea del archivo
            for linea in f:
 # Dividir la línea en columnas utilizando tabulaciones como separador
                columnas = linea.strip().split('\t')

                # Extraer la columna 1 (letras) y la columna 2 (valores)
                letras = columnas[0]
                valores = columnas[1]

                # Convertir la columna 1 a un número entero
                numero = int(valores)

                # Verificar si el número ya está en el diccionario
                if numero in letters_values:
                    # Verificar si la letra ya está en la lista de letras asociadas
                    if letras not in letters_values[numero]:
                        letters_values[numero].append(letras)
                else:
                    letters_values[numero] = [letras]
    
    # Ordenar alfabéticamente las letras en la lista asociada a cada valor
    for valor, letras in letters_values.items():
        letters_values[valor] = sorted(letras)

    # Convertir el diccionario en una lista de tuplas
    result = [(numero, letras) for numero, letras in sorted(letters_values.items())]

    return result


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    registros_por_clave = {}

    # Iterar sobre cada archivo CSV en el directorio actual
    for archivo in glob.glob(os.path.join(os.getcwd(), "*.csv")):
        with open(archivo, "r") as f:
            # Iterar sobre cada línea del archivo
            for linea in f:
                # Dividir la línea en columnas utilizando tabulaciones como separador
                columnas = linea.strip().split('\t')

                # Extraer la columna 5 (claves y valores)
                col_5 = columnas[4]

                # Dividir las claves y los valores separados por comas
                keys_values = col_5.split(',')

                # Iterar sobre los pares clave-valor y extraer las claves
                for par in keys_values:
                    clave, _ = par.split(':')

                    # Incrementar la cantidad de registros para esta clave
                    if clave in registros_por_clave:
                        registros_por_clave[clave] += 1
                    else:
                        registros_por_clave[clave] = 1
                        
    # Ordenar alfabéticamente las claves del diccionario
    registros_por_clave_ordenados = {k: registros_por_clave[k] for k in sorted(registros_por_clave)}

    return registros_por_clave_ordenados


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    result = []

    # Iterar sobre cada archivo CSV en el directorio actual
    for archivo in glob.glob(os.path.join(os.getcwd(), "*.csv")):
        with open(archivo, "r") as f:
            # Iterar sobre cada línea del archivo
            for linea in f:
                # Dividir la línea en columnas utilizando tabulaciones como separador
                columnas = linea.strip().split('\t')
                # Extraer la letra de la columna 1
                letra_columna1 = columnas[0]

                # Contar la cantidad de elementos en las columnas 4 y 5
                cantidad_elementos = letra_columna1, len(columnas[3].split(',')) , len(columnas[4].split(','))

                # Agregar la tupla a la lista de result
                result.append(cantidad_elementos)

    return result


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    suma_por_letra = {}

    # Iterar sobre cada archivo CSV en el directorio actual
    for archivo in glob.glob(os.path.join(os.getcwd(), "*.csv")):
        with open(archivo, "r") as f:
            # Iterar sobre cada línea del archivo
            for linea in f:
                columnas = linea.strip().split('\t')
                letras_columna4 = columnas[3].split(',')

                # Iterar sobre cada letra en la columna 4
                for letra_columna4 in letras_columna4:
                    # Verificar si la letra de la columna 4 ya está en el diccionario
                    if letra_columna4 in suma_por_letra:
                        # Si la letra ya existe, sumar la columna 2 al valor existente
                        suma_por_letra[letra_columna4.lower()] += int(columnas[1])
                    else:
                        # Si la letra no existe, inicializar el valor con la suma de la columna 2
                        suma_por_letra[letra_columna4.lower()] = int(columnas[1])

    # Ordenar el diccionario alfabéticamente por las claves (letras)
    suma_por_letra_ordenada = {letra: suma_por_letra[letra] for letra in sorted(suma_por_letra)}

    return suma_por_letra_ordenada

# df = pregunta_11("data.csv")
# print(df)

def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    suma_por_letra = {}

    # Iterar sobre cada archivo CSV en el directorio actual
    for archivo in glob.glob(os.path.join(os.getcwd(), "*.csv")):
        with open(archivo, "r") as f:
            # Iterar sobre cada línea del archivo
            for linea in f:
                columnas = linea.strip().split('\t')
                letra_columna1 = columnas[0]
                valores_columna5 = columnas[4].split(',')
                suma_columna5 = sum(int(valor.split(':')[1]) for valor in valores_columna5)

                # Agregar la suma al diccionario
                if letra_columna1 in suma_por_letra:
                    suma_por_letra[letra_columna1] += suma_columna5
                else:
                    suma_por_letra[letra_columna1] = suma_columna5

    # Ordenar el diccionario alfabéticamente por las claves (letras)
    suma_por_letra_ordenada = {letra: suma_por_letra[letra] for letra in sorted(suma_por_letra)}

    return suma_por_letra_ordenada

# df = pregunta_12("data.csv")
# print(df)
