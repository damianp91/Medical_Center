# MIT License
#
# Copyright (c) 2024 [UTN FRA](https://fra.utn.edu.ar/) All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import json
from unidecode import unidecode
from datetime import datetime

def convertir_valor(clave: str, valor: str, formato: str) -> (datetime | int):
    """
    Convierte el valor de un campo específico a un tipo apropiado.
    Args:
        clave (str): La clave del valor.
        valor (str): El valor a convertir.
        formato (str): Formato que se desea.
    Returns:
        datetime | float: El valor convertido.
    """
    conversion = valor
    
    if clave in ['fecha ingreso']:
        if isinstance(valor, datetime):
            conversion = valor.strftime(formato)
        else:
            conversion = datetime.strptime(valor, formato)
    
    if clave in ['Presupuesto']:
        conversion = int(valor)
    
    return conversion


def copia_json_original(nombre_archivo: str) -> (list[dict]):
    """
    Lee un archivo JSON y devuelve una lista de diccionarios con los datos del archivo.
    
    Args:
        nombre_archivo (str): Nombre del archivo JSON a leer.
        
    Returns:
        list: Lista de diccionarios con los datos del archivo JSON.
    """
    lista_aux = []
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            datos = json.load(archivo)
            for fila in datos:
                fila_ok = {unidecode(clave): convertir_valor(unidecode(clave), unidecode(str(valor)), '%d-%m-%Y')\
                for clave, valor in fila.items()}
                lista_aux.append(fila_ok)
    except FileNotFoundError:
        print(f"Error: El archivo {nombre_archivo} no se encontró.")
    except json.JSONDecodeError:
        print(f"Error: El archivo {nombre_archivo} no está en un formato JSON válido.")
    except Exception as e:
        print(f"Error inesperado: {e}")
    
    return lista_aux


def pasar_lista_archivo(lista: list[dict], archivo: str) -> (None):
    """
    Filtra proyectos con estado 'Finalizado' y los guarda en un archivo JSON con fechas en una lista.
    Args:
        proyectos (list[dict]): Lista de diccionarios.
    """
    try:
        lista_convertida = []
        for fila in lista:
            fila_ok = {clave: convertir_valor(clave, valor, '%d-%m-%Y') for clave, valor in fila.items()}
            lista_convertida.append(fila_ok)
        
        with open(archivo, 'w', encoding='utf-8') as archivo_original:
            json.dump(lista_convertida, archivo_original, ensure_ascii=False, indent=4)
        
        print(f"Datos guardados exitosamente en {archivo}.")
    except Exception as e:
        print(f"Error al guardar los datos en {archivo}: {e}")