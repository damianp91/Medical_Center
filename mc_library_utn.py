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

import os
from mc_paciente import Paciente
from mc_validaciones import (
    validar_entero
)
from mc_menus import (
    menu_principal
)
from datetime import datetime


def clear_console():
    """
    The function `clear_console` prompts the user to press Enter to continue and then clears the console
    screen based on the operating system.
    """
    _ = input('\nPresione Enter para continuar...')
    if os in ['nt', 'dos', 'ce']:
        os.system('clear')
    else: os.system('cls')    


def UTN_messenger(message: str, message_type: str = None, new_line: bool = False) -> (None):
    """
    This is a Python function that prints a message with a specific color and message type.
    
    :param message: The message that needs to be displayed in the console
    :param message_type: The type of message being passed, which can be 'Error', 'Success', 'Info',
    or None. If None, the message will be printed without any formatting
    """
    _b_red: str = '\033[41m'
    _b_green: str = '\033[42m'
    _b_blue: str = '\033[44m'
    _f_white: str = '\033[37m'
    _no_color: str = '\033[0m'
    message_type = message_type.strip().capitalize()
    new_line_char = '\n'
    final_message = f'{new_line_char if new_line else ""}'
    match message_type:
        case 'Error':
            final_message += f'{_b_red}{_f_white}> Error: {message}{_no_color}'
        case 'Success':
            final_message += f'{_b_green}{_f_white}> Success: {message}{_no_color}'
        case 'Info':
            final_message += f'{_b_blue}{_f_white}> Information: {message}{_no_color}'
        case _:
            final_message += message
    print(final_message)


def mc_menu_principal() -> (int):
    """
    Muestra en cosola menu principal y valida si la opcion ingresada sea correcta
    Returns:
        (int): devuelve -1 si no es un valor numerico o el valor ingresado
    """
    valor = -1
    menu_principal()
    opcion = input("\nIngrese la opcion (1-9): ")
    if validar_entero(opcion, 1, 9):
        valor = int(opcion)
    return valor


def ingreso_fecha() -> (datetime):
    """
    Pide por consola dia, mes, anio para ser validados y formateados como (dd/mm/aaaa)
    Returns:
        datetime: Devuelve objeto de tipo datetime o None en caso de no ingresar los datos
        correctamente.
    """
    dia = input("\nIngrese dia (dd): ")
    mes = input("Ingrese mes (mm): ")
    anio = input("Ingrese anio (aaaa): ")
    
    fecha = None
    if validar_entero(dia, 1, 31) and validar_entero(mes, 1, 12)\
        and validar_entero(anio, 1800, 3000):
            formato = f"{int(dia):02d}/{int(mes):02d}/{anio}"
            
            try:
                fecha = datetime.strptime(formato, '%d/%m/%Y')
                print("\nFecha correcta")
            except:
                print("\nLa fecha ingresada no es válida.")
    
    else:
        print("\nEl dato ingresado no es numerico o no respeta el formato pedido (dd)(mm)(aaaa)")
    
    return fecha


def fecha_hoy() -> (datetime):
    """
    Obtiene la fecha actual y la devuelve como un objeto datetime.
    
    Returns:
        datetime: La fecha actual como un objeto datetime.
    """
    hoy = datetime.now()
    
    return hoy


def bucar(lista: list[dict], clave: str, valor: str) -> (bool):
    """
    Busca por clave y valor si el elemnto esta en la lista de diccionarios
    retorna un True 
    Args:
        proyectos (list[dict]): Lista de diccionarios de proyectos
        calve (str): calve a buscar
        valor (str): valor a comparar
    Returns:
        (bool): Retorna un True si se encuantra el valor o por defecto retorna un False
    """
    buscar_ok = False
    if lista:
        for elemento in lista:
            if elemento.get(clave) == valor:
                buscar_ok = True
    
    return buscar_ok


def asignacion_id(proyectos: list[dict]) -> (int):
    """
    Asigna un nuevo ID autoincremental basado en los IDs existentes en la lista de proyectos.
    Args:
        proyectos (list[dict]): Lista de diccionarios con los proyectos existentes.
    Returns:
        int: El nuevo ID autoincremental.
    """
    id = 1
    if proyectos:
        ultimo_id = max(int(proyecto['id']) for proyecto in proyectos)
        id = ultimo_id + 1 
    
    return id


def normalizar_frase(frase: str) -> (str):
    """
    Capitaliza las palabras de más de tres caracteres en una frase.
    Args:
        frase (str): Cadena de caracteres a normalizar.
    Returns:
        str: Frase normalizada con palabras de más de tres caracteres
        capitalizadas.
    """
    frase = frase.split()
    list_aux = []
    
    for palabra in frase:
        if len(palabra) > 3:
            palabra = palabra.capitalize()
        list_aux.append(palabra)
    
    frase_hecha = ' '.join(list_aux)
    
    return frase_hecha


def mc_alta_paciente(lista_pacientes: list[dict]) -> (list[dict]):
    if lista_pacientes:
        pass