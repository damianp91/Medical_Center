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

from mc_menus import(
    menu_obra_social, menu_especialidad
)




def validar_caracteres(texto: str, longitud: int, alfanumerico= False) -> (bool):
    """
    Valida cadena de caracteres si son alfabeticos o alfanumericos segun
    eleccion por parametro
    Args:
        texto (srt): cadena de caracteresa evaluar
        longitud (int): La cantidad de caracteres que se permitira validar
        alfanumerico (bool): por defecto es False, pero si se desea validar
        cadena de caracteres alfanumeroricos puede agregarse True
    Returns:
        bool: True si la cadena representa caracteres alfanumericos dentro 
        del rango especificado, False en caso que sean solo alfabeticos.
    """
    validador_ok = False
    tex_aux = texto.replace(' ', '')
    
    if alfanumerico:
        if len(texto) <= longitud:
            validador_ok = tex_aux.isalnum()
    else:
        if len(texto) <= longitud:
            validador_ok = tex_aux.isalpha()
    
    return validador_ok


def validar_entero(numero_str: str, minimo: int, maximo: int) -> (bool):
    """
    Valida si una cadena representa un número entero dentro de un rango específico.
    Args:
        numero_str (str): Cadena que se desea validar.
        minimo (int): Valor mínimo aceptado.
        maximo (int): Valor máximo aceptado.
    Returns:
        bool: True si la cadena representa un número entero dentro del 
        rango especificado, False en caso contrario.
    """
    validador_ok = False
    
    if numero_str.isdigit():
        numero = int(numero_str)
        validador_ok = minimo <= numero <= maximo
    
    return validador_ok
# ● Obra social: Debe ser un valor entre: Swiss Médical, Apres, PAMI, Particular.
# ○ Si el paciente tiene 60 años o más, la única opción disponible a seleccionar
# será PAMI. Si tiene menos de 60, puede seleccionar las restantes EXCEPTO
# PAMI.
def validar_obre_social(anios_paciente: int) -> (str):
    """
    Valida y selecciona una obra social para el paciente basado en su edad
    Args:
        anios_paciente (int): anios de paciente a validar
    Returns:
        str: Devuelve una obra social entre Swiss Médical, Apres, PAMI,
            Particular
    """
    obras = {
        '1': 'Swiss Médical',
        '2': 'Apres',
        '3': 'PAMI',
        '4': 'Particular'
    }
    
    menu_obra_social()
    seleccion = input("Ingrese opcion: ")
    if validar_entero(seleccion, 1, 4) and anios_paciente < 60:
        obra = obras[seleccion]
        print(f"Se selecciono especialidad: {obra}.")
    else:
        obra = obras['4']
        print(f"Se selecciono especialidad: {obra}.")
    
    return obra
# ● Especialidad: El valor debe estar entre las opciones: Médico Clínico, Odontología,
# Psicología y Traumatología.
def validar_especialidad() -> (str):
    """
    Valida y selecciona una especialidad
    Returns:
        str: Devuelve una obra social entre Swiss Médical, Apres, PAMI,
            Particular
    """
    especialidades = {
        '1': 'Medico Clínico.',
        '2': 'Odontologia.',
        '3': 'Psicologia.',
        '4': 'Traumatologia.'
    }
    
    menu_especialidad()
    seleccion = input("Ingrese opcion: ")
    if validar_entero(seleccion, 1, 4):
        especialidad = especialidades[seleccion]
        print(f"Se selecciono especialidad: {especialidad}.")
    else:
        print("No se selecciono especialidad.")
    return especialidad
# ● Estado del turno: al momento de cargarlo, el estado por defecto será: “Activo”.
def estado_turno() -> (str):
    """
    Devuelve por defecto 'Activo'
    Returns:
        str: cadena de caracteres
    """
    return 'Activo'
# ● Monto a pagar (del turno): el monto se calculará teniendo en cuenta el precio base
# de la atención ($4000) y luego aplicarle el descuento o recargo según la obra social
# del paciente. Además, a ese monto resultante, tener en cuenta lo siguiente:
# ○ Si el paciente tiene Swiss Medical (Aplicar -40% y además...):
# ■ Si la edad está entre 18 y 60, se aplica un -10% extra
# ○ Si el paciente tiene Apres (Aplicar -25% y además...):
# ■ Si la edad está entre 26 y 59, se aplica un -3% extra
# ○ Si el paciente tiene PAMI (Aplicar -60% y además...):
# ■ Si la edad es 80 o superior, se aplica un -3% extra
# ○ Si el paciente es Particular (Aplicar +5% y además...):
# ■ Si la edad está entre 40 y 60, se aplica un +15% extra
def calcular_monto_a_pagar(obra_social: str, edad: int) -> (float):
    """
    Calcula el monto a pagar para una atención médica basado en la obra social y la 
    edad del paciente.
    Args:
        obra_social (str): La obra social del paciente.
        edad (int): La edad del paciente.
        Returns: float: El monto a pagar por la atención médica.
    """
    precio_base = 4000
    descuentos = {
        'Swiss Medical': lambda edad: precio_base * 0.6 * (0.9 if 18 <= edad <= 60 else 1),
        'Apres': lambda edad: precio_base * 0.75 * (0.97 if 26 <= edad <= 59 else 1),
        'PAMI': lambda edad: precio_base * 0.4 * (0.97 if edad >= 80 else 1),
        'Particular': lambda edad: precio_base * 1.05 * (1.15 if 40 <= edad <= 60 else 1)
    }
    
    monto_a_pagar = descuentos.get(obra_social, lambda edad: precio_base)(edad)
    
    return round(monto_a_pagar, 2)


def validar_salida() -> (None):
    """
    Valida que el usuario quiera salir y guardar o no cambios en lista de proyectos
    Args:
        proyectos (list[dict]): Lista de proyectos a guardar
    """
    guardar = True
    while guardar:
        eleccion = input("\n¿Desea guardar los cambios? (s/n): ").lower()
        if validar_caracteres(eleccion, 1):
            if eleccion == 's':
                guardar = False
            elif eleccion == 'n':
                print("\nNo se hace cambios en lista de proyectos")
                guardar = False
            else:
                print("\n¡Debe elegir entre 's' y 'n' para poder salir del parcial!")
        else:
            print("\n¡Debe elegir entre 's' y 'n' para poder salir del parcial!")


