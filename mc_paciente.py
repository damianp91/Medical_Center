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

from datetime import datetime
from mc_validaciones import(
    validar_caracteres, validar_entero
)
from mc_menus import(
    consulta_elemento, menu_obra_social
)


from datetime import datetime

class Paciente:
    """
    Clase que representa un paciente en una clínica.
    
    Atributos:
    ----------
    id : int
        Identificador único del paciente.
    nombre : str
        Nombre del paciente.
    apellido : str
        Apellido del paciente.
    dni : int
        Documento Nacional de Identidad del paciente.
    edad : int
        Edad del paciente.
    fecha_ingreso : datetime
        Fecha de ingreso del paciente a la clínica.
    obra_social : str
        Obra social del paciente.
    """
    
    def __init__(self, id: int, nombre: str, apellido: str, dni: int, edad: int, fecha_ingreso: datetime, obra_social: str):
        self.__id = id
        self.__nombre = nombre
        self.__apellido = apellido
        self.__dni = dni
        self.__edad = edad
        self.__fecha_ingreso = fecha_ingreso
        self.__obra_social = obra_social

    # Getters
    def get_id(self) -> (int):
        return self.__id

    def get_nombre(self) -> (str):
        return self.__nombre

    def get_apellido(self) -> (str):
        return self.__apellido

    def get_dni(self) -> (int):
        return self.__dni

    def get_edad(self) -> (int):
        return self.__edad

    def get_fecha_ingreso(self) -> (datetime):
        return self.__fecha_ingreso

    def get_obra_social(self) -> (str):
        return self.__obra_social

    # Setters
    def set_id(self, id: int):
        self.__id = id

    def set_nombre(self, valor: str):
        valor = consulta_elemento('nombre')
        if validar_caracteres(valor, 15):
            self.__nombre = valor.strip().capitalize()
        else:
            print("\nIngreso de elemento erróneo.")

    def set_apellido(self, valor: str):
        valor = consulta_elemento('apellido')
        if validar_caracteres(valor, 15):
            self.__apellido = valor.strip().capitalize()
        else:
            print("\nIngreso de elemento erróneo.")

    def set_dni(self, valor: int):
        valor = consulta_elemento('DNI')
        if validar_entero(valor, 10, 10):
            self.__dni = int(valor)
        else:
            print("\nIngreso de elemento erróneo.")

    def set_edad(self, valor: int):
        valor = consulta_elemento('edad')
        if validar_entero(valor, 18, 90):
            self.__edad = int(valor)
        else:
            print("\nIngreso de elemento erróneo.")

    def set_fecha_ingreso(self, fecha_ingreso: datetime):
        try:
            fecha = datetime.strptime(fecha_ingreso, '%d/%m/%Y')
            self.__fecha_ingreso = fecha
        except ValueError:
            print("\nFormato de fecha incorrecto. Debe ser DD/MM/AAAA.")

    def set_obra_social(self, obra_social: str):
        menu_obra_social()
        opcion = consulta_elemento('obra social')
        if validar_entero(opcion, 1, 4):
            self.__obra_social = obra_social
        else:
            print("\nIngreso de elemento erróneo.")




