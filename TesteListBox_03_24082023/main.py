from tkinter import messagebox

from tkinter import *

frmJanela = Tk()

def Mensagem():
    messagebox.showinfo("mensagem", "Olá, Mundo!")


def DesvCond():
    if messagebox.askyesno("desvio condicional", "escolha sim ou não") == True:
        messagebox.showinfo("opção", "você escolheu sim")
    else:
        messagebox.showinfo("opção", "você escolheu não")


def DesvCondAninhado():
    resposta = messagebox.askyesnocancel("desvio condicional aninhado", "escolha sim, não ou cancelar")

    if resposta == True:
        messagebox.showinfo("opção", "você escolheu sim")
    elif resposta == False:
        messagebox.showinfo("opção", "você escolheu não")
    else:
        messagebox.showinfo("opção", "você escolheu cancelar")


def SwitchCase():
    resposta = messagebox.askyesnocancel("desvio condicional aninhado", "escolha sim, não ou cancelar")
    match resposta:
        case True:
            messagebox.showinfo("opção", "você escolheu sim")
        case False:
            messagebox.showinfo("opção", "você escolheu não")
        case None:
            messagebox.showinfo("opção", "você escolheu cancelar")
        case _:
            messagebox.showinfo("opção", "você escolheu errado, escolha sim, não ou cancelar")


def impTxtWhile():
    lstbxPreferencias.delete(0, END)
    arqPreferencias = open("C:\CURSO PROGRAMAR\Python\preferencias.txt", "r")
    strLinhaLida = arqPreferencias.readline()

    while(strLinhaLida != ""):
        lstbxPreferencias.insert(END, strLinhaLida)
        strLinhaLida = arqPreferencias.readline()

    arqPreferencias.close()

def For():
    lstbxPreferencias.delete(0, END)
    arqPreferencias = open("C:\CURSO PROGRAMAR\Python\preferencias.txt", "r")

    lstDados = arqPreferencias.readlines()

    for i in range(len(lstDados)):
        item = lstDados[i]
        lstbxPreferencias.insert(END, item)

    arqPreferencias.close()


def ForEach():
    lstbxPreferencias.delete(0, END)
    arqPreferencias = open("C:\CURSO PROGRAMAR\Python\preferencias.txt", "r")

    lstDados = arqPreferencias.readlines()

    for item in lstDados:
        lstbxPreferencias.insert(END, item)

    arqPreferencias.close()

def Clear():
    # limpa a listbox de acordo com o que o usuário selecionou
    selecao = lstbxPreferencias.curselection()

    for item in selecao[::-1]:
        lstbxPreferencias.delete(item)


btnMensagem = Button(frmJanela, text="mensagem", fg="black", bg="grey", width=25, height=1, command=Mensagem)
btnMensagem.place(x=35, y=50)

btnDesvCond = Button(frmJanela, text="desvio condicional", fg="black", bg="grey", width=25, height=1, command=DesvCond)
btnDesvCond.place(x=35, y=100)

btnDesvCondAninhado = Button(frmJanela, text="desvio condicional aninhado", fg="black", bg="grey", width=25, height=1, command=DesvCondAninhado)
btnDesvCondAninhado.place(x=35, y=150)

btnSwitchCase = Button(frmJanela, text="switch case", fg="black", bg="grey", width=25, height=1, command=SwitchCase)
btnSwitchCase.place(x=35, y=200)

btnWhile = Button(frmJanela, text="while", fg="black", bg="grey", width=25, height=1, command=impTxtWhile)
btnWhile.place(x=35, y=250)

btnFor = Button(frmJanela, text="for", fg="black", bg="grey", width=25, height=1, command=For)
btnFor.place(x=35, y=300)

btnForEach = Button(frmJanela, text="foreach", fg="black", bg="grey", width=25, height=1, command=ForEach)
btnForEach.place(x=35, y=350)

btnClear = Button(frmJanela, text="clear", fg="black", bg="grey", width=25, height=1, command=Clear)
btnClear.place(x=35, y=400)

lstbxPreferencias = Listbox(frmJanela, width=35, height=23, selectmode="multiple")
lstbxPreferencias.place(x=250, y=50)

frmJanela.title("Janela de botões")
frmJanela.geometry("500x450+30+30")

frmJanela.mainloop()






