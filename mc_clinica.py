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
        self.razon_social = razon_social
        self.lista_pacientes = lista_pacientes
        self.lista_turnos = lista_turnos
        self.especialidades = especialidades
        self.obras_sociales = obras_sociales
        self.recaudacion = recaudacion
        self.pacientes_no_atencion = pacientes_no_atencion

