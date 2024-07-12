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



def mostrar_paciente(diccionario: dict) -> (None):
    """
    Muestra por consola diccionario en formato tabla
    Args:
        proyecto (dict): Diccionario a formatear como tabla
    """
    
    mensaje = f"| {diccionario['id']:^4} | {diccionario['dni']:^10} | {diccionario['nombre']:30}\
 | {diccionario['apellido']:30} | {diccionario['edad']:4} | {diccionario['obra social']:^12} |"
    
    print(mensaje)


def mc_mostrar_pacientes(proyectos: list[dict]) -> (None):
    """
    Muestra por consola proyectos en formato tabla
    Args:
        proyectos (list[dict]): Lista de diccionarios
    """
    print("-" * 109)
    print("|\t\t\t\t\t\t  Medical Center UTN\t\t\t\t\t    |")
    print("-" * 109)
    print(f"| {'ID':^4} | {'DNI':^10} | {'NOMBRE':^30} | {'APELLIDO':^30}\
 | {'EDAD':^4} | {'OBRA SOCIAL':^12} |")
    print("-" * 109)
    for proyecto in proyectos:
        mostrar_paciente(proyecto)
    print("-" * 109)


def mostrar_turno(diccionario: dict) -> (None):
    """
    Muestra por consola diccionario en formato tabla
    Args:
        proyecto (dict): Diccionario a formatear como tabla
    """
    
    mensaje = f"| {diccionario['id']:^4} | {diccionario['id_paciente']:^4} | {diccionario['especialidad']:30}\
 | {diccionario['monto_pagar']:10} | {diccionario['estado_turno']:12} |"
    
    print(mensaje)


def mc_mostrar_turnos(proyectos: list[dict]) -> (None):
    """
    Muestra por consola proyectos en formato tabla
    Args:
        proyectos (list[dict]): Lista de diccionarios
    """
    print("-" * 90)
    print("|\t\t\t\t\t\t  Medical Center UTN\t\t\t\t\t    |")
    print("-" * 90)
    print(f"| {'ID':^4} | {'ID PACIENTE':^4} | {'ESPECIALIDAD':^30} | {'MONTO A PAGAR':^10}\
 | {'ESTADO TURNO':^12} |")
    print("-" * 90)
    for proyecto in proyectos:
        mostrar_turno(proyecto)
    print("-" * 90)


def mostrar_clave_valor(proyectos: list[dict], clave: str, valor: str) -> (list[dict]):
    """
    Agrega a una lista de retorno el o los diccionarios que cumplan con con el criterio
    de clave y valor
    Args:
        proyectos (list[dict]): Lista de diccionarios
        clave (str): calve de diccionario
        valor (str): valor de la clave
    Returns:
        list: lista de elementos, elemento o lista vacia 
    """
    retorno_lista = []
    if proyectos:
        for proyecto in proyectos:
            if proyecto.get(clave) == valor:
                retorno_lista.append(proyecto)
    
    return retorno_lista