from tkinter import messagebox
from tkinter import *
import pyodbc
import pandas as pdPreferencias

frmJanela = Tk()

def Mensagem():
    messagebox.showinfo("mensagem", "Olá, Mundo!")


def DesvioCondicional():
    if messagebox.askyesno("desvio condicional", "escolha sim ou não") == True:
        messagebox.showinfo("opção", "você escolheu sim")
    else:
        messagebox.showinfo("opção", "você escolheu não")


def DesvioCondicionalEncadeado():
    resposta = messagebox.askyesnocancel("desvio condicional", "escolha sim, não ou cancelar")

    if resposta == True:
        messagebox.showinfo("opção", "você escolheu sim")
    elif resposta == False:
        messagebox.showinfo("opção", "você escolheu não")
    else:
        messagebox.showinfo("opção", "você escolheu cancelar")


def SwitchCase():
    match(messagebox.askyesnocancel("desvio condicional", "escolha sim, não ou cancelar")):
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

    objLeitorTxt = open("C:\CURSO PROGRAMAR\Python\preferencias.txt", "r")
    strLinhaLida = objLeitorTxt.readline()

    while(strLinhaLida != ""):
        lstbxPreferencias.insert(END, strLinhaLida)
        strLinhaLida = objLeitorTxt.readline()

    objLeitorTxt.close()


def impTxtFor():
    lstbxPreferencias.delete(0, END)

    objLeitorTxt = open("C:\CURSO PROGRAMAR\Python\preferencias.txt", "r")
    strLinhaLida = objLeitorTxt.readlines()

    for item in range(len(strLinhaLida)):
        item = strLinhaLida[item]
        lstbxPreferencias.insert(END, item)

    objLeitorTxt.close()


def impTxtForEach():
    lstbxPreferencias.delete(0, END)

    objLeitorTxt = open("C:\CURSO PROGRAMAR\Python\preferencias.txt", "r")
    strLinhaLida = objLeitorTxt.readlines()

    for item in strLinhaLida:
        lstbxPreferencias.insert(END, item)

    objLeitorTxt.close()

def Clear():
    selecao = lstbxPreferencias.curselection()

    for item in selecao[::-1]:
        lstbxPreferencias.delete(item)


def ImpBDCon():
    lstbxPreferencias.delete(0, END)

    connectionString = (
        r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
        r'DBQ=C:\CURSO PROGRAMAR\Python\Preferencias_1_05072023.accdb;'
    )

    objConexao = pyodbc.connect(connectionString)
    objLeitorBD = objConexao.cursor()

    strSQL = "SELECT Descricao from Preferencias_3;"

    objLeitorBD.execute(strSQL)

    record = objLeitorBD.fetchone()

    while record != None:
        lstbxPreferencias.insert(END, record.Descricao)
        record = objLeitorBD.fetchone()

    objLeitorBD.close()
    objConexao.close()


def ImpBDDes():
    lstbxPreferencias.delete(0, END)

    connectionString = (
        r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
        r'DBQ=C:\CURSO PROGRAMAR\Python\Preferencias_1_05072023.accdb;'
    )

    objConexao = pyodbc.connect(connectionString)
    objLeitorBD = objConexao.cursor()

    strSQL = "SELECT Descricao from Preferencias_3;"

    objLeitorBD.execute(strSQL)

    records = objLeitorBD.fetchall()

    objConexao.close()

    dfPreferencias = pdPreferencias.DataFrame(records, columns=['Descricao'])

    for item in records:
        lstbxPreferencias.insert(END, item.Descricao)

    print(dfPreferencias.items)
    print(dfPreferencias)


btnMensagem = Button(frmJanela, fg="black", bg="gray", text="mensagem", width=25, height=1, command=Mensagem)
btnMensagem.place(x=35, y=50)

btnDesvioCondicional = Button(frmJanela, fg="black", bg="gray", text="desvio condicional", width=25, height=1, command=DesvioCondicional)
btnDesvioCondicional.place(x=35, y=100)

btnDesvioCondicionalEncadeado = Button(frmJanela, fg="black", bg="gray", text="desvio condicional encadeado", width=25, height=1, command=DesvioCondicionalEncadeado)
btnDesvioCondicionalEncadeado.place(x=35, y=150)

btnSwitchCase = Button(frmJanela, fg="black", bg="gray", text="switch case", width=25, height=1, command=SwitchCase)
btnSwitchCase.place(x=35, y=200)

btnImpTxtWhile = Button(frmJanela, fg="black", bg="gray", text="importar texto while", width=25, height=1, command=impTxtWhile)
btnImpTxtWhile.place(x=35, y=250)

btnImpTxtFor = Button(frmJanela, fg="black", bg="gray", text="importar texto for", width=25, height=1, command=impTxtFor)
btnImpTxtFor.place(x=35, y=300)

btnImpTxtForEach = Button(frmJanela, fg="black", bg="gray", text="importar texto foreach", width=25, height=1, command=impTxtForEach)
btnImpTxtForEach.place(x=35, y=350)

btnClear = Button(frmJanela, fg="black", bg="gray", text="clear", width=25, height=1, command=Clear)
btnClear.place(x=35, y=400)

btnBDCon = Button(frmJanela, fg="black", bg="gray", text="BD conectado", width=25, height=1, command=ImpBDCon)
btnBDCon.place(x=35, y=450)

btnBDDes = Button(frmJanela, fg="black", bg="gray", text="BD desconectado", width=25, height=1, command=ImpBDDes)
btnBDDes.place(x=35, y=500)

lstbxPreferencias = Listbox(frmJanela, width=35, height=30, selectmode="multiple")
lstbxPreferencias.place(x=250, y=50)

frmJanela.title("Janela de Botões")
frmJanela.geometry("500x550+30+30")

frmJanela.mainloop()