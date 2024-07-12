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

class Clinica:
    """
    Clase que representa una clínica.
    Atributos:
    ----------
    razon_social : str
        La razón social de la clínica.
    lista_pacientes : List[str]
        Lista de nombres de pacientes.
    lista_turnos : List[str]
        Lista de turnos asignados a los pacientes.
    especialidades : Dict{clave:valor}
        Diccionario de especialidades médicas disponibles en la clínica.
    obras_sociales : Dict{clave:valor}
        Diccionario de obras sociales que acepta la clínica.
    recaudacion : float
        La recaudación total de la clínica.
    pacientes_no_atencion : Bool
        Bandera para identificar pacientes que no han recibido atención.
    """
    def __init__(self, razon_social: str, lista_pacientes: list, lista_turnos: list,\
    especialidades: dict, obras_sociales: dict, recaudacion: float, pacientes_no_atencion: bool):
        self.__razon_social = razon_social
        self.__lista_pacientes = lista_pacientes
        self.__lista_turnos = lista_turnos
        self.__especialidades = especialidades
        self.__obras_sociales = obras_sociales
        self.__recaudacion = recaudacion
        self.__pacientes_no_atencion = pacientes_no_atencion
    
    # Getters
    #-----------------------------------------------------------------------
    def get_razon_social(self) -> (str):
        return self.__razon_social
    
    
    def get_lista_pacientes(self) -> (list):
        return self.__lista_pacientes
    
    
    def get_lista_turnos(self) -> (list):
        return self.__lista_turnos
    
    
    def get_especialidades(self) -> (dict):
        return self.__especialidades
    
    
    def get_obras_sociales(self) -> (dict):
        return self.__obras_sociales
    
    
    def get_recaudacion(self) -> (float):
        return self.__recaudacion
    
    
    def get_pacientes_no_atencion(self) -> (float):
        return self.__pacientes_no_atencion
        
    def agregar_monto(self, monto: float):
        """
        Agrega un monto a la recaudación total de la clínica.
        Args:
            monto (float): El monto a agregar.
        """
        self.__recaudacion += monto

