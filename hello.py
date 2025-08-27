#!/usr/bin/env python3
""" Hello World Multi Linguas.
Dependendo da lingua configurada no ambiente o programa exibe a mensagem
correspondente.

Como usar:
Tenha a variável LANG devidamente configurada ex:
    export LANG=pt_BR

Execução:
    python3 hello.py
"""
__version__ = "1.0.0"
__author__ = "Camila Mota"
__license__ = "Unlicense"

import os

current_language = os.getenv("LANG", "en_US")[:5]

msg = "Hello, world!"

# Aqui aplicamos a condicional

if current_language == "pt_BR":
    msg = "Olá, mundo!"
elif current_language == "fr_FR":
    msg = "Bonjour, le monde!"
elif current_language == "es_ES":
    msg = "¡Hola, mundo!"
else:
    msg = "Hello, world!"

print(msg) 