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

import os
from datetime import datetime
from mc_validaciones import(
    validar_entero, calcular_monto_a_pagar, estado_turno
)

from mc_menus import(
    menu_principal, consulta_elemento, menu_obra_social, menu_especialidad,
    menu_ordenamiento
)

from mc_mostrar_listas import(
    mc_mostrar_pacientes, mc_mostrar_turnos
)

def clear_console():
    """
    The function `clear_console` prompts the user to press Enter to continue and then clears the console
    screen based on the operating system.
    """
    _ = input('\nPresione Enter para continuar...')
    if os in ['nt', 'dos', 'ce']:
        os.system('clear')
    else: os.system('cls')    


def UTN_messenger(message: str, message_type: str = None, new_line: bool = False) -> (None):
    """
    This is a Python function that prints a message with a specific color and message type.
    
    :param message: The message that needs to be displayed in the console
    :param message_type: The type of message being passed, which can be 'Error', 'Success', 'Info',
    or None. If None, the message will be printed without any formatting
    """
    _b_red: str = '\033[41m'
    _b_green: str = '\033[42m'
    _b_blue: str = '\033[44m'
    _f_white: str = '\033[37m'
    _no_color: str = '\033[0m'
    message_type = message_type.strip().capitalize()
    new_line_char = '\n'
    final_message = f'{new_line_char if new_line else ""}'
    match message_type:
        case 'Error':
            final_message += f'{_b_red}{_f_white}> Error: {message}{_no_color}'
        case 'Success':
            final_message += f'{_b_green}{_f_white}> Success: {message}{_no_color}'
        case 'Info':
            final_message += f'{_b_blue}{_f_white}> Information: {message}{_no_color}'
        case _:
            final_message += message
    print(final_message)


def mc_menu_principal() -> (int):
    """
    Muestra en cosola menu principal y valida si la opcion ingresada sea correcta
    Returns:
        (int): devuelve -1 si no es un valor numerico o el valor ingresado
    """
    valor = -1
    menu_principal()
    opcion = input("\nIngrese la opcion (1-9): ")
    if validar_entero(opcion, 1, 9):
        valor = int(opcion)
    return valor


def ingreso_fecha() -> (datetime):
    """
    Pide por consola dia, mes, anio para ser validados y formateados como (dd/mm/aaaa)
    Returns:
        datetime: Devuelve objeto de tipo datetime o None en caso de no ingresar los datos
        correctamente.
    """
    dia = input("\nIngrese dia (dd): ")
    mes = input("Ingrese mes (mm): ")
    anio = input("Ingrese anio (aaaa): ")
    
    fecha = None
    if validar_entero(dia, 1, 31) and validar_entero(mes, 1, 12)\
        and validar_entero(anio, 1800, 3000):
            formato = f"{int(dia):02d}/{int(mes):02d}/{anio}"
            
            try:
                fecha = datetime.strptime(formato, '%d/%m/%Y')
                print("\nFecha correcta")
            except:
                print("\nLa fecha ingresada no es válida.")
    
    else:
        print("\nEl dato ingresado no es numerico o no respeta el formato pedido (dd)(mm)(aaaa)")
    
    return fecha


def fecha_hoy() -> (str):
    """
    Obtiene la fecha actual y la devuelve como un objeto datetime.
    
    Returns:
        datetime: La fecha actual como un objeto datetime.
    """
    hoy = datetime.now()
    
    fecha = hoy.date().strftime('%Y-%m-%d')
    
    return fecha


def verificador_formato_fecha(valor: str, formato: str= '%d/%m/%Y') -> (str):
    """
    Verifica si una fecha esta en el formato requerido. Si no, la formatea al formato
    especificado.
    Args:
        valor (str): La fecha a verificar.
        formato (str): El formato deseado. Por defecto es '%d/%m/%Y'.
    Returns:
        str | datetime: La fecha en el formato especificado.
    """
    formato_ok = ""
    try:
        # En caso que sea un objeto datetime
        if isinstance(valor, datetime):
            formato_ok = valor.strftime(formato)
        # En caso que sea un strin y tenga formato d/m/a
        else:
            fecha = datetime.strptime(valor, '%d-%m-%Y')
            formato_ok = fecha.strftime(formato)
    
    except ValueError:
        try:
            # En caso que sean un valor distinto a los anteriores
            datetime.strptime(valor, formato)
            formato_ok = valor
        
        except ValueError:
            # No es ninguno de los tres.
            raise ValueError(f"La fecha '{valor}' no está en un formato válido.")
    
    return formato_ok


def bucar_elemento(lista: list[dict], clave: str, valor: str) -> (bool):
    """
    Busca por clave y valor si el elemnto esta en la lista de diccionarios
    retorna un True 
    Args:
        proyectos (list[dict]): Lista de diccionarios de proyectos
        calve (str): calve a buscar
        valor (str): valor a comparar
    Returns:
        (bool): Retorna un True si se encuantra el valor o por defecto retorna un False
    """
    buscar_ok = False
    if lista:
        for elemento in lista:
            if elemento.get(clave) == valor:
                buscar_ok = True
    
    return buscar_ok


def asignacion_id(proyectos: list[dict]) -> (int):
    """
    Asigna un nuevo ID autoincremental basado en los IDs existentes en la lista de proyectos.
    Args:
        proyectos (list[dict]): Lista de diccionarios con los proyectos existentes.
    Returns:
        int: El nuevo ID autoincremental.
    """
    id = 1
    if proyectos:
        ultimo_id = max(int(proyecto['id']) for proyecto in proyectos)
        id = ultimo_id + 1 
    
    return id


def normalizar_frase(frase: str) -> (str):
    """
    Capitaliza las palabras de más de tres caracteres en una frase.
    Args:
        frase (str): Cadena de caracteres a normalizar.
    Returns:
        str: Frase normalizada con palabras de más de tres caracteres
        capitalizadas.
    """
    frase = frase.split()
    list_aux = []
    
    for palabra in frase:
        if len(palabra) > 3:
            palabra = palabra.capitalize()
        list_aux.append(palabra)
    
    frase_hecha = ' '.join(list_aux)
    
    return frase_hecha


def mc_alta_paciente(lista_pacientes: list[dict]) -> (list[dict]):
    from mc_paciente import Paciente
    """_summary_
    Raises:
        ValueError: _description_
        ValueError: _description_
        ValueError: _description_
        ValueError: _description_
        ValueError: _description_
    Returns:
        _type_: _description_
    """
    try:
        # Inicializar clase paciente
        nuevo = Paciente("", "", "", 0, 0, datetime.now(), "")
        
        # DNI
        alta_dni = consulta_elemento('DNI (Debe tener 10 digitos.)')
        if not nuevo.set_dni(alta_dni):
            raise ValueError(f"DNI: {alta_dni} no es numérico o es menor o mayor a los 10 caracteres.")
        
        print(f"\nDNI: {alta_dni} ingresado con éxito.")
        
        if bucar_elemento(lista_pacientes, 'dni', alta_dni):
            print(f"\nDNI: {alta_dni} ya fue dado de alta anteriormente.")
            return lista_pacientes  # Salir de la función si el DNI ya está registrado
        
        # ID
        alta_id = asignacion_id(lista_pacientes)
        nuevo.set_id(alta_id)
        print(f"\nId asignado con éxito.")
        
        # Nombre
        alta_nombre = consulta_elemento('nombre (No puede superar los 30 caracteres)').strip()
        if not nuevo.set_nombre(alta_nombre):
            raise ValueError(f"Nombre: {alta_nombre} no puede superar los 30 caracteres.")
        
        print(f"\nNombre: {alta_nombre} ingresado con éxito.")
        
        # Apellido
        alta_apellido = consulta_elemento('apellido (No puede superar los 30 caracteres)').strip()
        if not nuevo.set_apellido(alta_apellido):
            raise ValueError(f"Apellido: {alta_apellido} no puede superar los 30 caracteres.")
        
        print(f"\nApellido: {alta_apellido} ingresado con éxito.")
        
        # Edad
        alta_edad = consulta_elemento('edad (Debe estar en el rango de 18 a 90)')
        if not nuevo.set_edad(alta_edad):
            raise ValueError(f"Error edad: {alta_edad} debe ser un número y debe estar en el rango de '18' a '90'.")
        
        print(f"\nEdad: {alta_edad} ingresada con éxito.")
        
        # Fecha ingreso
        str(nuevo.set_fecha_ingreso(fecha_hoy()))
        
        # Obra social
        menu_obra_social()
        opcion = consulta_elemento('obra social (Debe elegir una opción de la lista)')
        if not nuevo.set_obra_social(opcion):
            raise ValueError("Error debe elegir una opción entre 1 a 4.")
        
        print(f"\nObra social: {nuevo.get_obra_social()} ingresada con éxito.")
        
        paciente_ok = {
            'id': nuevo.get_id(), 'dni': nuevo.get_dni(), 'nombre': nuevo.get_nombre(), 'apellido': nuevo.get_apellido(),
            'edad': nuevo.get_edad(), 'fecha ingreso': nuevo.get_fecha_ingreso(), 'obra social': nuevo.get_obra_social(),
        }
        
        lista_pacientes.append(paciente_ok)
    
    except ValueError as e:
        print(e)
        print("Regresando al menú principal...")
    
    return lista_pacientes


def bucar_indice(proyectos: list[dict], clave: str, valor: str) -> (int):
    """
    Busca un índice dentro de una lista de diccionarios según una clave y un valor específicos.
    Args:
        proyectos (list[dict]): Lista de diccionarios donde buscar.
        clave (str): Clave del diccionario que se utilizará para la búsqueda.
        valor (str): Valor que se está buscando dentro de la clave especificada.
        
    Returns:
        int: Índice del diccionario en la lista donde se encuentra el valor buscado. Si no se encuentra,
            retorna -1.
    """
    indice =  -1
    for i, diccionario in enumerate(proyectos):
        if diccionario.get(clave) == valor:
            indice = i
    
    return indice

#Alta turno: se dará de alta un turno para una especialidad, teniendo en cuenta el id de un paciente ya existente en el sistema.
def mc_alta_turno(lista_turnos: list[dict], lista_pacientes: list[dict]) -> (list[dict]):
    """_summary_
    Args:
        lista_turnos (_type_): _description_
    Raises:
        ValueError: _description_
        ValueError: _description_
        ValueError: _description_
    """
    from mc_turno import Turno
    
    try:
        
        nuevo_turno = Turno("", "", "", "", "")
        
        # ID_turno
        alta_id_turno = asignacion_id(lista_turnos)
        nuevo_turno.set_id_turno(alta_id_turno)
        print(f"\nId turno asignado con éxito.")
        
        # ID paciente
        mc_mostrar_pacientes(lista_pacientes)
        alta_id_paciente = consulta_elemento('ID paciente: ')
        if not bucar_elemento(lista_pacientes, 'id', alta_id_paciente):
            raise ValueError("\nError no se encuentra id paciente.")
        if not nuevo_turno.set_id_paciente(alta_id_paciente):
            raise ValueError("\nError debe elegir una opcion numerica valida.")
        print("\nId paciente agregado con exito")
        
        # especialidad
        menu_especialidad()
        alta_id_especialidad = consulta_elemento('especialidad: ')
        if not nuevo_turno.set_especialidad(alta_id_especialidad):
            raise ValueError("Error debe elegir una opción entre 1 a 4.")
        
        # monto a pagar
        indice = bucar_indice(lista_pacientes, 'id', alta_id_paciente)
        paciente = lista_pacientes[indice]
        monto = str(calcular_monto_a_pagar(paciente.get('obra social'), paciente.get('edad')))
        nuevo_turno.set_monto_pagar(monto)
        
        # estado turno
        turno = estado_turno()
        nuevo_turno.set_estado_turno(turno)
        
        turno_ok = {
            'id': nuevo_turno.get_id(), 'id_paciente': nuevo_turno.get_id_paciente(), 'especialidad': nuevo_turno.get_especialidad(),
            'monto_pagar': nuevo_turno.get_monto_pagar(),'estado_turno': nuevo_turno.get_estado_turno(),
        }
        
        lista_turnos.append(turno_ok)
        
        print("Turno registrado con exito.")
        
    except ValueError as e:
        print(e)
        print("Regresando al menú principal...")
    
    return lista_turnos


def ordenar_tabla_valor(lista_ordenar: list[dict], key: str, men_may= True) -> (list[dict]):
    """
    Ordena una lista de diccionarios segun criterio
    Args:
        personajes (list[dict]): Lista de diccionarios a ordenar
        key (str): Clave a evaluar
        may_men (bool): Opcion de sentido por defecto es True si se desea que 
                        el sentido sea de menor a mayor o False en sentido 
                        contrario
    Returns:
        (list[dict]): Lita de diccionarios ordenados
    """
    if len(lista_ordenar) < 2:
        return lista_ordenar
    
    proyectos_copia = lista_ordenar.copy()
    for elemeto in proyectos_copia:
        elemeto['monto_pagar'] = float(elemeto['monto_pagar'])
    
    pivot = proyectos_copia.pop()
    pivot_valor = pivot.get(key)
    mayor = []
    menor = []
    
    for proyecto in proyectos_copia:
        if men_may:
            if proyecto.get(key) > pivot_valor:
                mayor.append(proyecto)
            else:
                menor.append(proyecto)
        else:
            if proyecto.get(key) < pivot_valor:
                mayor.append(proyecto)
            else:
                menor.append(proyecto)
    
    return ordenar_tabla_valor(menor, key, men_may) + [pivot] + ordenar_tabla_valor(mayor, key, men_may)


def mc_mostrar_tabla_ordenada(lista_ordenar: list[dict]) -> (None):
    """
    Muestra por consola lista de diccionario ordenada segun criterio
    Args:
        personajes (list[dict]): Lista de diccionarios 
        key (str): Clave a evaluar
        may_men (str): Opcion de sentido de orde debe ser 'menor' o 'mayor'
    Returns:
        (int): Devuelve -1 si la lista es uan lista vacio o muestra por consola la lista 
        ordenada segun criterio
    """
    if lista_ordenar:
        menu_ordenamiento()
        opcion = input("\nIngrese opcion: ")
        if validar_entero(opcion, 1, 2):
            if opcion == "1":
                proyectos_ordenados = ordenar_tabla_valor(lista_ordenar, 'especialidad')
            else:
                proyectos_ordenados = ordenar_tabla_valor(lista_ordenar, 'monto_pagar', False)
            
            mc_mostrar_turnos(proyectos_ordenados)
        
        else:
            print("\nEleccion incorrecta se cancela ordenamiento.")
    else:
        print("\nLista de proyectos vacia.")


def mc_pacientes_espera(lista_turnos: list[dict], lista_pacientes: list[dict]) -> (list[dict]):
    """
    Muestra todos los pacientes que aún tienen el turno en “Activo”.
    Args:
        lista_turnos (list[dict]): Lista de diccionarios con los turnos.
        lista_pacientes (list[dict]): Lista de diccionarios con los pacientes.
    """
    lista_activos = filter(lambda turno: turno['estado_turno'] == 'Activo', lista_turnos)
    
    pacientes_espera = [paciente for turno in lista_activos for paciente in lista_pacientes if paciente['id'] == turno['id_paciente']]
    
    mc_mostrar_pacientes(pacientes_espera)


def atender_pacientes(lista_turnos: list[dict]) -> (list[dict]):
    """
    Selecciona los primeros 2 pacientes cuyo estado del turno sea "Activo" y cambia el estado a "Finalizado".
    En caso de haber un solo paciente, se seleccionará ese mismo para ser atendido.
    En caso de no haber ninguno en espera, se informará en consola.
    Args:
        lista_turnos (list[dict]): Lista de diccionarios con los turnos.
    Returns:
        list[dict]: Lista actualizada de turnos.
    """
    # Filtrar 
    turnos_activos = [turno for turno in lista_turnos if turno['estado_turno'] == 'Activo']
    
    if len(turnos_activos) == 0:
        print("No hay pacientes en espera.")
    
    turnos_a_atender = turnos_activos[:2]
    
    for turno in turnos_a_atender:
        indice = lista_turnos.index(turno)
        lista_turnos[indice]['estado_turno'] = 'Finalizado'
    
    print(f"Se han atendido {len(turnos_a_atender)} pacientes.")
    
    return lista_turnos


def mc_cobrar_atencion(lista_turnos: list[dict]) -> (list[dict]):
    """
    Selecciona a los pacientes cuyo estado del turno sea "Finalizado" para realizar el cobro,
    cambia su estado a "Pagado" y suma el monto al tributo recaudación de la clase Clínica.
    Args:
        lista_turnos (list[dict]): Lista de diccionarios con los turnos.
    Returns:
        list[dict]: Lista actualizada de turnos.
    """
    from mc_clinica import Clinica
    
    # Filtrar los turnos en estado 'Finalizado'
    turnos_finalizados = [turno for turno in lista_turnos if turno['estado_turno'] == 'Finalizado']
    if not turnos_finalizados:
        print("No hay pacientes con turnos finalizados para cobrar.")
    
    monto_total = 0.0
    
    for turno in turnos_finalizados:
        indice = lista_turnos.index(turno)
        lista_turnos[indice]['estado_turno'] = 'Pagado'
        monto_total += float(turno['monto_pagar'])
        Clinica.agregar_monto(float(turno['monto_pagar']))
    print(f"Se han cobrado atenciones por un total de: {monto_total}")
    
    return lista_turnos


def mc_informe(lista_pacientes: list[dict], lista_turnos: list[dict]) -> (None):
    """
    Filtra la lista de pacientes por aquellos que tienen la obra social "Swiss Medical"
    y suma los montos de los turnos correspondientes.
    
    Args:
        lista_pacientes (list[dict]): Lista de diccionarios de pacientes.
        lista_turnos (list[dict]): Lista de diccionarios de turnos.
    """
    pacientes_swiss_medical = [paciente for paciente in lista_pacientes if paciente.get('obra social') == 'Swiss Medical']
    if not pacientes_swiss_medical:
        print("No se encontraron pacientes con obra social 'Swiss Medical'.")
    
    ids_pacientes_swiss = [paciente['id'] for paciente in pacientes_swiss_medical]
    
    total_recaudado = 0.0
    for turno in lista_turnos:
        if turno['id_paciente'] in ids_pacientes_swiss:
            total_recaudado += float(turno['monto_pagar'])
    
    
    print(f"Total recaudado por pacientes de Swiss Medical: ${total_recaudado:.2f}")




