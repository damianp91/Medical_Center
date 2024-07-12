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

def menu_principal() -> (None):
    """
    Imprime por consola el menu del sistema principal
    Args:
        None.
    Returns:
        str: Devuelve uan cadena de caracteres
    """
    menu = \
    """
    =============================================
    \t\tGESTION DE CITAS
    =============================================
    01. Alta paciente.
    02. Alta turno.
    03. Ordenar turnos.
    04. Mostrar pacientes.
    05. Atender pacientes.
    06. Cobrar atenciones.
    07. Cerrar caja.
    08. Monto total obtenido de
        pacientes de Swiss Medical
        mayores de 21 años.
    09. Salir 
    =============================================
    """
    print(menu)


def menu_obra_social() -> (None):
    """
    Imprime en consola el submenu del sistema para
    seleccionar obra social
    Args:
        None.
    Returns:
        str: Devuelve una cadena de caracteres
    """
    sub_menu = \
    """
    ==================================
    \tOBRA SOCIAL
    ==================================
    1. Swiss Medical.
    2. Apres.
    3. PAMI.
    4. Particular.
    ==================================
    """
    print(sub_menu)


def menu_especialidad() -> (None):
    """
    Imprime en consola el submenu del sistema para
    seleccionar especialidad
    Args:
        None.
    Returns:
        str: Devuelve una cadena de caracteres
    """
    sub_menu = \
    """
    ==================================
    \tESPECIALIDAD
    ==================================
    1. 'Medico Clinico.
    2. 'Odontologia.
    3. 'Psicologia.
    4. 'Traumatologia.
    ==================================
    """
    print(sub_menu)


def menu_ordenamiento() -> (None):
    """
    Imprime en consola el submenu del sistema para
    seleccionar especialidad
    Args:
        None.
    Returns:
        str: Devuelve una cadena de caracteres
    """
    sub_menu = \
    """
    ==================================
        SENTIDO ORDEMANIENTO
    ==================================
    1. Obra Social ASC
    2. Monto DESC
    ==================================
    """
    print(sub_menu)


def consulta_elemento(palabra: str) -> (str):
    """
    Solicita al usuario que ingrese un valor asociado a la palabra proporcionada.  
    Args:
        palabra (str): La palabra que se utilizará para solicitar el valor al usuario. 
    Returns:
        str: El valor ingresado por el usuario.
    """
    return input(f"Ingrese {palabra}: ")