import os, shutil
from tkinter import *
from tkinter import filedialog


def copia_seletiva(pasta_origem, pasta_destino):
    pasta_origem = os.path.abspath(pasta_origem)
    pasta_destino = os.path.abspath(pasta_destino)
    for foldername, subfolders, filenames in os.walk(pasta_origem):
        for filename in filenames:
            if filename.endswith('.py'):
                shutil.copy(os.path.join(foldername, filename), pasta_destino)

if __name__ == '__main__':
    copia_seletiva('/home/andre/teste', '/home/andre/aquii')                