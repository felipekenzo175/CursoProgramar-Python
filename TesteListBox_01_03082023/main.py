from tkinter import *

from tkinter import messagebox

frmJanela = Tk()

def Mensagem():
    messagebox.showinfo("Mensagem","Olá Mundo")


def DesvCond():
    if messagebox.askyesno("Desvio Condicional", "Escolha Sim ou Não") == True:
        messagebox.showinfo("Opção", "Você escolheu Sim")
    else:
        messagebox.showinfo("Opção", "Você escolheu Não")


def DesvCondAninhado():
    resposta = messagebox.askyesnocancel("Desvio Condicional Aninhado", "Escolha Sim, Não ou Cancelar")

    if resposta == True:
        messagebox.showinfo("Opção", "Você escolheu Sim")
    elif resposta == False:
        messagebox.showinfo("Opção", "Você escolheu Não")
    else:
        messagebox.showinfo("Opção", "Você escolheu Cancelar")


def SwitchCase():
    resposta = messagebox.askyesnocancel("Desvio Condicional Aninhado", "Escolha Sim, Não ou Cancelar")

    match resposta:
        case True:
            messagebox.showinfo("Opção", "Você escolheu Sim")
        case False:
            messagebox.showinfo("Opção", "Você escolheu Não")
        case None:
            messagebox.showinfo("Opção", "Você escolheu Cancelar")
        case _:
            messagebox.showinfo("Opção", "Você escolheu Errado, Escolha Sim, Não ou Cancelar")


btnMensagem = Button(frmJanela, text="Mensagem", fg="black", bg="gray", width="25", height="1", command=Mensagem)
btnMensagem.place(x=35, y=50)

btnDesvCond = Button(frmJanela, text="Desvio Condicional", fg="black", bg="gray", width="25", height="1", command=DesvCond)
btnDesvCond.place(x=35, y=100)

btnDesvCondAninhado = Button(frmJanela, text="Desvio Condicional Aninhado", fg="black", bg="gray", width="25", height="1", command=DesvCondAninhado)
btnDesvCondAninhado.place(x=35, y=150)

btnSwitchCase = Button(frmJanela, text="Switch Case", fg="black", bg="gray", width="25", height="1", command=SwitchCase)
btnSwitchCase.place(x=35, y=200)

btnWhile = Button(frmJanela, text="Texto While", fg="black", bg="gray", width="25", height="1")
btnWhile.place(x=35, y=250)

lstbxPreferencias = Listbox(frmJanela, width=35, height=14, selectmode="multiple")

lstDados = ('primeiro', 'segundo', 'terceiro', 'quarto', 'quinto', 'sexto')

for item in lstDados:
    lstbxPreferencias.insert(END, item)

lstbxPreferencias.place(x=250, y=50)

frmJanela.title("Teste ListBox 1")
frmJanela.geometry("500x300+30+30")

frmJanela = mainloop()
