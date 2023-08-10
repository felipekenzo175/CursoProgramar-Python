from tkinter import *

from tkinter import messagebox

frmJanela = Tk()

def Mensagem():
    messagebox.showinfo("MENSAGEM", "Olá, Mundo")


def DesvioCondicional():
    if messagebox.askyesno("DESVIO CONDICIONAL", "Escolha Sim ou Não") == True:
        messagebox.showinfo("OPÇÃO", "Você escolheu Sim")
    else:
        messagebox.showinfo("OPÇÃO", "Você escolheu Não")


def DesvioCondicionalAninhado():
    resultado = messagebox.askyesnocancel("DESVIO CONDICIONAL ANINHADO", "Escolha Sim, Não ou Cancelar")

    if resultado == True:
        messagebox.showinfo("OPÇÃO", "Você escolheu Sim")
    elif resultado == False:
        messagebox.showinfo("OPÇÃO", "Você escolheu Não")
    else:
        messagebox.showinfo("OPÇÃO", "Você escolheu Cancelar")


def SwitchCase():
    resultado = messagebox.askyesnocancel("DESVIO CONDICIONAL ANINHADO", "Escolha Sim, Não ou Cancelar")

    match resultado:
        case True:
            messagebox.showinfo("OPÇÃO", "Você escolheu Sim")
        case False:
            messagebox.showinfo("OPÇÃO", "Você escolheu Não")
        case None:
            messagebox.showinfo("OPÇÃO", "Você escolheu Cancelar")
        case _:
            messagebox.showinfo("OPÇÃO", "Você escolheu Errado, Escolha Sim, Não ou Cancelar")


def impTxtWhile():
    arqPreferencias = open("C:\CURSO PROGRAMAR\Python\preferencias.txt", "r")

    strLinhaLida = arqPreferencias.readline()

    while(strLinhaLida != ""):
        lstbxPreferencias.insert(END, strLinhaLida)
        strLinhaLida = arqPreferencias.readline()

    arqPreferencias.close()

def For():
    arqPreferencias = open("C:\CURSO PROGRAMAR\Python\preferencias.txt", "r")

    lstDados = arqPreferencias.readlines()

#criação do for que vai iterar sobre o índice da lista de dados, o len(lstDados) retorna quantos elementos tem
#na lista e o range() gera os índices da lista, por exemplo, se a lista tivesse 5 items, o len(lstDados) retor-
#naria 5 e o range(len(lstDados)) faria os índices 0, 1, 2, 3, 4, de modo que seja possível percorrer a lista cor-
#retamente.
    for i in range(len(lstDados)):
        item = lstDados[i]
        lstbxPreferencias.insert(END, item)
#o END dentro do método insert é uma constante que sempre vai adicionar os elementos ao final da listbox.
    arqPreferencias.close()

def ForEach():
    arqPreferencias = open("C:\CURSO PROGRAMAR\Python\preferencias.txt", "r")

    lstDados = arqPreferencias.readlines()

#criação do for que vai iterar diretamente sobre a lista de dados.
    for item in lstDados:
        lstbxPreferencias.insert(END, item)
#o END dentro do método insert é uma constante que sempre vai adicionar os elementos ao final da listbox.
    arqPreferencias.close()


btnMensagem = Button(frmJanela, fg="black", bg="grey", text="Mensagem", width=25, height=1, command=Mensagem)
btnMensagem.place(x=35, y=50)

btnDesvioCondicional = Button(frmJanela, fg="black", bg="grey", text="Desvio Condicional", width=25, height=1, command=DesvioCondicional)
btnDesvioCondicional.place(x=35, y=100)

btnDesvioCondicionalAninhado = Button(frmJanela, fg="black", bg="grey", text="Desvio Condicional Aninhado", width=25, height=1, command=DesvioCondicionalAninhado)
btnDesvioCondicionalAninhado.place(x=35, y=150)

btnSwitchCase = Button(frmJanela, fg="black", bg="grey", text="SwitchCase", width=25, height=1, command=SwitchCase)
btnSwitchCase.place(x=35, y=200)

btnWhile = Button(frmJanela, fg="black", bg="grey", text="While", width=25, height=1, command=impTxtWhile)
btnWhile.place(x=35, y=250)

btnFor = Button(frmJanela, fg="black", bg="grey", text="For", width=25, height=1, command=For)
btnFor.place(x=35, y=300)

btnForEach = Button(frmJanela, fg="black", bg="grey", text="ForEach", width=25, height=1, command=ForEach)
btnForEach.place(x=35, y=350)

lstbxPreferencias = Listbox(frmJanela, width=35, height=20, selectmode="multiple")
lstbxPreferencias.place(x=250, y=50)

frmJanela.title("Tela de 7 botões + ListBox")
frmJanela.geometry("500x400+30+30")

frmJanela.mainloop()
