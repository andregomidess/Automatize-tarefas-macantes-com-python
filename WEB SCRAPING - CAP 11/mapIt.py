#!/usr/bin/python3
import webbrowser, sys, pyperclip


if len(sys.argv) > 1:
# Obtém o endereço da linha de comando.
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()
    
webbrowser.open('https://www.google.com/maps/place/' + address)    
    