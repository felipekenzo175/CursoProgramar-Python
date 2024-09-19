import tkinter as tk
from tkinter import ttk
from FRONT.frmPreferencias import FrmPreferencias
from FRONT.frmFamiliares import FrmFamiliares
# Importar tudo da classe frmExercicioDAO_01_29042024
from frmExercicioSegundaTabela_01_05092024 import *


class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        tabControl = ttk.Notebook(self)

        tabPreferencias = FrmPreferencias(tabControl)
        tabControl.add(tabPreferencias, text="Preferencias")

        tabFamiliares = FrmFamiliares(tabControl)
        tabControl.add(tabFamiliares, text="Familiares")

        tabControl.pack(expand=1, fill="both")


# # Criar a janela principal da aplicação Tkinter, iniciando ela com o tk.Tk()
# app = tk.Tk()
# # Definir o tamanho da janela principal com 520 pixels de largura e 600 pixels de altura
# app.geometry("520x620")
#
# # Criar uma instância da classe FrmExercicioDAO_01_29042024 e passar a janela principal app como pai.
# objFrmExercicioSegundaTabela_01_05092024 = FrmExercicioSegundaTabela_01_05092024(app)
# # Usar o pack para adicionar a classe ao app, colocar fill=tk.BOTH e expand=True(1) para preencher toda a área disponível.
# objFrmExercicioSegundaTabela_01_05092024.pack(fill=tk.BOTH, expand=True)
#
# # Iniciar o loop principal que mantém a aplicação rodando e aguardando por eventos, até que a janela seja fechada.
# app.mainloop()