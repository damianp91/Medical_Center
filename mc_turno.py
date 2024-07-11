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
        self.id_turno = id_turno
        self.id_paciente = id_paciente
        self.especialidad = especialidad
        self.monto_pagar = monto_pagar
        self.estado = estado
