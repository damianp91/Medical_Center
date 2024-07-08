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
import mc_validaciones as val

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





