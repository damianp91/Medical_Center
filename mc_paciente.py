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
    validar_entero, validar_caracteres, validar_obra_social
)
from mc_library_utn import(
    verificador_formato_fecha, normalizar_frase
)
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
    #-----------------------------------------------------------------------
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
    #-----------------------------------------------------------------------
    def set_id(self, valor: int) -> (None):
        """
        Establece el ID del paciente.
        Args:
            valor (int): El ID a establecer.
        """
        
        if int(valor):
            self.__id = str(valor)
    
    
    def set_nombre(self, valor: str) -> (bool):
        """
        Establece el nombre del paciente, validando que no supere los 30 caracteres.
        Args:
            valor (str): El nombre a establecer.
        Returns:
            bool: True si el nombre es válido y se establece, False en caso contrario.
        """
        
        nombre_ok = False
        if validar_caracteres(valor, 30, False):
            self.__nombre = normalizar_frase(valor)
            nombre_ok = True
        return nombre_ok
    
    
    def set_apellido(self, valor: str) -> (bool):
        """
        Establece el apellido del paciente, validando que no supere los 30 caracteres.
        Args:
            valor (str): El apellido a establecer.
        Returns:
            bool: True si el apellido es válido y se establece, False en caso contrario.
        """
        
        apellido_ok = False
        if validar_caracteres(valor, 30, False):
            self.__apellido = normalizar_frase(valor)
            apellido_ok = True
        return apellido_ok
    
    
    def set_dni(self, valor: str) -> (bool):
        """
        Establece el DNI del paciente, validando que sea un número entero y esté en el rango correcto.
        Args:
            valor (str): El DNI a establecer.
        Returns:
            bool: True si el DNI es válido y se establece, False en caso contrario.
        """
        
        dni_ok = False
        if validar_entero(valor, 1 ,100000000):
            dni_ok = True
            self.__dni = valor
        
        return dni_ok
    
    
    def set_edad(self, valor: int) -> (bool):
        """
        Establece la edad del paciente, validando que esté en el rango de 18 a 90.
        Args:
            valor (int): La edad a establecer.
        Returns:
            bool: True si la edad es válida y se establece, False en caso contrario.
        """
        
        edad_ok = False
        if validar_entero(valor, 18, 90):
            self.__edad = valor
            edad_ok = True
        return edad_ok
    
    
    def set_fecha_ingreso(self, valor: datetime) -> (bool):
        """
        Establece la fecha de ingreso del paciente.
        Args:
            valor (datetime): La fecha de ingreso a establecer.
        Returns:
            bool: True si la fecha es válida y se establece, False en caso contrario.
        """
        
        fecah_ok = False
        if type(valor) == datetime:
            self.__fecha_ingreso = valor
            fecah_ok = False
        return fecah_ok
    
    
    def set_obra_social(self, valor: str) -> (bool):
        """
        Establece la obra social del paciente, validando que sea un número entero entre 1 y 4.
        Args:
            valor (str): La obra social a establecer.
        Returns:
            bool: True si la obra social es válida y se establece, False en caso contrario.
        """
        
        obra_social = False
        if validar_entero(valor, 1, 4):
            obra = validar_obra_social(valor, self.get_edad())
            self.__obra_social = obra
            obra_social = True
        return obra_social
    
    #-----------------------------------------------------------------------
    
    def mostrar_paciente(self):
        """
        Muestra la información del paciente.
        """
        
        fecha = verificador_formato_fecha(self.__fecha_ingreso)
        mensaje = f'|id: {self.__id} nombre: {self.__nombre} apellido: {self.__apellido} dni: {self.__dni:10}\
        edad: {self.__edad} fecha: {fecha} obra social: {self.__obra_social}|'
        
        print(mensaje)




