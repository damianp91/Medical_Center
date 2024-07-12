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

from mc_library_utn import(
    clear_console, UTN_messenger, mc_menu_principal, mc_alta_paciente,
    mc_alta_turno, mc_mostrar_tabla_ordenada, mc_pacientes_espera,
    atender_pacientes, mc_cobrar_atencion, mc_informe
)
from mc_validaciones import(
    validar_salida
)
from mc_manejo_archivos import(
    copia_json_original, pasar_lista_archivo
)
from mc_clinica import Clinica
from mc_paciente import Paciente
from mc_turno import Turno


def main_app():
    """
    Aplicacion principal del Segundo Parcial de Laboratorio 1
    """
    
    while True:
        
        opcion = mc_menu_principal()
        copia_pacientes = copia_json_original('lista_pacientes.json')
        copia_turnos = copia_json_original('lista_turnos.json')
        
        match opcion:
            case 1: # Alta paciente
                nueva_lista_pacientes = mc_alta_paciente(copia_pacientes)
                pasar_lista_archivo(nueva_lista_pacientes, 'lista_pacientes.json')
            case 2: # Alta turno
                nueva_lista_turnos = mc_alta_turno(copia_turnos, copia_pacientes)
                pasar_lista_archivo(nueva_lista_turnos, 'lista_turnos.json')
            case 3: # Ordenar turnos
                mc_mostrar_tabla_ordenada(copia_turnos)
            case 4: # Mostrar pacientes en espera
                mc_pacientes_espera(copia_turnos, copia_pacientes)
            case 5: # Atender pacientes
                nueva_lista_atendidos =atender_pacientes(copia_turnos)
                pasar_lista_archivo(nueva_lista_atendidos, 'lista_turnos.json')
            case 6: # Cobrar atenciones
                lista_cobro = mc_cobrar_atencion(copia_turnos)
                pasar_lista_archivo(lista_cobro, 'lista_turnos.json')
            case 7: # Cerrar caja
                pass
            case 8: # Mostrar informe
                mc_informe(copia_pacientes, copia_turnos)
            case 9: # Salir
                validar_salida()
                print("¡¡¡Gracias por usar nuestra app!!!")
                break
            case _:
                UTN_messenger('Opción inválida. Por favor, seleccione una opción válida.', 'Error')
        clear_console()
            