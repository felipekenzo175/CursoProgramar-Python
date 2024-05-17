# Importar tudo da classe frmExercicioDAO_01_29042024
from frmExercicioDAO_01_29042024 import *

'''Criar uma aplicação tkinter, definir o tamanho e adicionar a classe FrmExercicioDAO_01_29042024, 
fazer ela preencher toda a janela e colocar ela em um loop de espera por eventos.'''

# Criar a janela principal da aplicação Tkinter, iniciando ela com o tk.Tk()
app = tk.Tk()
# Definir o tamanho da janela principal com 520 pixels de largura e 600 pixels de altura
app.geometry("520x600")

# Criar uma instância da classe FrmExercicioDAO_01_29042024 e passar a janela principal app como pai.
objFrmExercicioDAO_01_29042024 = FrmExercicioDAO_01_29042024(app)
# Usar o pack para adicionar a classe ao app, colocar fill=tk.BOTH e expand=True para preencher toda a área disponível.
objFrmExercicioDAO_01_29042024.pack(fill=tk.BOTH, expand=True)

# Iniciar o loop principal que mantém a aplicação rodando e aguardando por eventos, até que a janela seja fechada.
app.mainloop()