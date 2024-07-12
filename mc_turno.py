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

from mc_validaciones import(
    validar_entero, validar_especialidad, validar_caracteres
)

class Turno:
    """
    Clase que representa un turno en una clínica.
    Atributos:
    ----------
    id_turno : int
        Identificador único del turno.
    id_paciente : int
        Identificador único del paciente.
    especialidad : str
        Especialidad médica para la que se ha asignado el turno.
    monto_pagar : float
        Monto a pagar por el turno.
    estado : str
        Estado del turno (por ejemplo: "pendiente", "confirmado", "cancelado").
    """
    def __init__(self, id_turno: int, id_paciente: int, especialidad: str, monto_pagar: float, estado: str):
        self.__id_turno = id_turno
        self.__id_paciente = id_paciente
        self.__especialidad = especialidad
        self.__monto_pagar = monto_pagar
        self.__estado = estado
    
    # Getters
    #-----------------------------------------------------------------------
    def get_id(self) -> (int):
        return self.__id_turno
    
    
    def get_id_paciente(self) -> (int):
        return self.__id_paciente
    
    
    def get_especialidad(self) -> (str):
        return self.__especialidad
    
    
    def get_monto_pagar(self) -> (float):
        return self.__monto_pagar
    
    
    def get_estado_turno(self) -> (str):
        return self.__estado
    # Setters
    #-----------------------------------------------------------------------
    def set_id_turno(self, valor: int) -> (None):
        """
        Establece el ID del turno.
        Args:
            valor (int): El ID a establecer.
        """
        self.__id_turno = str(valor)
    
    def set_id_paciente(self, valor: str) -> (bool):
        """
        Establece el id del paciente.
        Args:
            valor (str): El id a establecer.
        Returns:
            bool: True si el nombre es válido y se establece, False en caso contrario.
        """
        
        id_paciente_ok = False
        if validar_entero(valor, 1, 500):
            self.__id_paciente = str(valor)
            id_paciente_ok = True
        return id_paciente_ok
    
    
    def set_especialidad(self, valor: str) -> (None):
        """
        Establece el apellido del paciente, validando que no supere los 30 caracteres.
        Args:
            valor (str): El apellido a establecer.
        Returns:
            bool: True si el apellido es válido y se establece, False en caso contrario.
        """
        
        especialidad_ok = False
        if validar_entero(valor, 1, 4):
            especialidad = validar_especialidad()
            self.__especialidad = especialidad
            especialidad_ok = True
        return especialidad_ok
    
    
    def set_monto_pagar(self, valor: str):
        """
        Establece el DNI del paciente, validando que sea un número entero y esté en el rango correcto.
        Args:
            valor (str): El DNI a establecer.
        """
        self.__monto_pagar = valor
    
    
    def set_estado_turno(self, valor: str) -> (None):
        """
        Establece la edad del paciente, validando que esté en el rango de 18 a 90.
        Args:
            valor (int): La edad a establecer.
        Returns:
            bool: True si la edad es válida y se establece, False en caso contrario.
        """
        
        tuno_ok = False
        if validar_caracteres(valor, 20):
            self.__estado = valor
            tuno_ok = True
        return tuno_ok
    #-----------------------------------------------------------------------
    def mostrar_paciente(self):
        """
        Muestra la información del paciente.
        """
        
        mensaje = f'|id turno: {self.__id_turno} id paciente: {self.__id_paciente} especialidad: {self.__especialidad}\
        monto: {self.__monto_pagar:10} estado turno: {self.__estado}|'
        
        print(mensaje)
