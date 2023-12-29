from FrmExercicioBancoDadosModificado import *

app = tk.Tk()
# está passando a biblioteca Tk() inteira para o FrmExercicioBancoDadosModificado
objFrmExercicioBancoDadosModificado = FrmExercicioBancoDadosModificado(app)
objFrmExercicioBancoDadosModificado.pack()
# pack é o comando tkinter que faz com que a tkinter assuma a exibição do form sem ter que colocar a geometria nele.

app.mainloop()