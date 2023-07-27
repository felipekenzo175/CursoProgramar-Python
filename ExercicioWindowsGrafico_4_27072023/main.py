from tkinter import *

from tkinter import messagebox

frmJanela = Tk()

def Mensagem():
    messagebox.showinfo('Mensagem', 'Olá, Mundo!')


def DesvCond():
    if messagebox.askyesno('Desvio Condicional', 'Escolha Sim ou Não') == True:
        messagebox.showinfo('Opção', 'Você escolheu Sim')
    else:
        messagebox.showinfo('Opção', 'Você escolheu Não')


def DesvCondAninhado():
    resultado = messagebox.askyesnocancel('Desvio Condicional Aninhado', 'Escolha Sim, Não ou Cancelar')

    if resultado == True:
        messagebox.showinfo('Opção', 'Você escolheu Sim')
    elif resultado == False:
        messagebox.showinfo('Opção', 'Você escolheu Não')
    else:
        messagebox.showinfo('Opção', 'Você escolheu Cancelar')


def SwitchCase():
    resultado = messagebox.askyesnocancel('Switch Case', 'Escolha Sim, Não ou Cancelar')

    match resultado:
        case True:
            messagebox.showinfo('Opção', 'Você escolheu Sim')
        case False:
            messagebox.showinfo('Opção', 'Você escolheu Não')
        case None:
            messagebox.showinfo('Opção', 'Você escolheu Cancelar')
        case _:
            messagebox.showinfo('Opção', 'Você escolheu Errado, Escolha Sim, Não ou Cancelar')


btnMensagem = Button(frmJanela, text="Mensagem", fg="black", bg="grey", width=25, height=1, command=Mensagem)
btnMensagem.place(x=170, y=50)

btnDesvCond = Button(frmJanela, text="Desvio Condicional", fg="black", bg="grey", width=25, height=1, command=DesvCond)
btnDesvCond.place(x=170, y=100)

btnDesvCondAninhado = Button(frmJanela, text="Desvio Condicional Aninhado", fg="black", bg="grey", width=25, height=1, command=DesvCondAninhado)
btnDesvCondAninhado.place(x=170, y=150)

btnSwitchCase = Button(frmJanela, text="Switch Case", fg="black", bg="grey", width=25, height=1, command=SwitchCase)
btnSwitchCase.place(x=170, y=200)

frmJanela.title("Exercicio Windows Grafico 4")
frmJanela.geometry("500x300+30+30")

frmJanela.mainloop()