from tkinter import messagebox
from tkinter import *
import pyodbc  # Importa BD Conectado e Importa BD Desconectado - tem que ir para o terminal e dar 'pip install pyodbc'
import pandas as pdPreferencias  # Importa BD Desconectado - tem que ir para o terminal e dar 'pip install pandas'

frmJanela = Tk()

def Mensagem():
    messagebox.showinfo("mensagem", "Olá, Mundo!")


def DesvioCondicional():
    if messagebox.askyesno("desvio condicional", "Escolha sim ou não"):
        messagebox.showinfo("opção", "você escolheu sim")
    else:
        messagebox.showinfo("opção", "você escolheu não")


def DesvioCondicionalAninhado():
    resposta = messagebox.askyesnocancel("desvio condicional aninhado", "Escolha sim, não ou cancelar")
    if resposta == True:
        messagebox.showinfo("opção", "você escolheu sim")
    elif resposta == False:
        messagebox.showinfo("opção", "você escolheu não")
    else:
        messagebox.showinfo("opção", "você escolheu cancelar")


def SwitchCase():
    resposta = messagebox.askyesnocancel("desvio condicional aninhado", "Escolha sim, não ou cancelar")

    match resposta:
        case True:
            messagebox.showinfo("opção", "você escolheu sim")
        case False:
            messagebox.showinfo("opção", "você escolheu não")
        case None:
            messagebox.showinfo("opção", "você escolheu cancelar")
        case _:
            messagebox.showinfo("opção", "você escolheu cancelar")


def ImpTxtWhile():
    lstbxPreferencias.delete(0, END)
    arqPreferencias = open(".\preferencias.txt", "r")
    strLinhaLida = arqPreferencias.readline()

    while (strLinhaLida != ""):
        lstbxPreferencias.insert(END, strLinhaLida)
        strLinhaLida = arqPreferencias.readline()

    arqPreferencias.close()


def ImpTxtFor():
    lstbxPreferencias.delete(0, END)
    arqPreferencias = open(".\preferencias.txt", "r")
    strListaLida = arqPreferencias.readlines()

    for i in range(len(strListaLida)):
        item = strListaLida[i]
        lstbxPreferencias.insert(END, item)

    arqPreferencias.close()


def ImpTxtForEach():
    lstbxPreferencias.delete(0,END)
    arqPreferencias = open(".\preferencias.txt", "r")
    strListaLida = arqPreferencias.readlines()

    for item in strListaLida:
        lstbxPreferencias.insert(END, item)

    arqPreferencias.close()


def LstBxClear():
    selecao = lstbxPreferencias.curselection()

    if len(selecao) <= 0:
            lstbxPreferencias.delete(0,END)
    else:
        for i in selecao[::-1]:
            lstbxPreferencias.delete(i)

def ImpBDCon():
    lstbxPreferencias.delete(0, END)

    connectionString = (
        r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
        r'DBQ=D:\Dados\GitHub\felipekenzo175\CursoProgramar-Python\ExercicioBancoDeDadosListBox_01_21092023\BancoDeDadosTeste.accdb;'
    )
    objConexao = pyodbc.connect(connectionString)
    objLeitorBD = objConexao.cursor()

    # for table_info in objLeitorBD.tables(tableType='TABLE'):
    #     print(table_info.table_name)

    strSQL = "SELECT Descricao from Preferencias;"

    objLeitorBD.execute(strSQL)

    # while True:
    #     record = objLeitorBD.fetchone()
    #     if record == None:
    #         break
    #     print(record)

    record = objLeitorBD.fetchone()

    while record != None:
        lstbxPreferencias.insert(END, record.Descricao)
        # print(f'{getattr(record,"Descricao")}')
        # print(f'{record.Descricao}')
        record = objLeitorBD.fetchone()

    objLeitorBD.close()
    objConexao.close()


def ImpBDDesc():
    lstbxPreferencias.delete(0, END)

    connectionString = (
        r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
        r'DBQ=D:\Dados\GitHub\felipekenzo175\CursoProgramar-Python\ExercicioBancoDeDadosListBox_01_21092023\BancoDeDadosTeste.accdb;'
    )
    objConexao = pyodbc.connect(connectionString)
    objLeitorBD = objConexao.cursor()

    strSQL = "SELECT Descricao from Preferencias;"

    objLeitorBD.execute(strSQL)

    records = objLeitorBD.fetchall()

    objConexao.close()

    dfPreferencias = pdPreferencias.DataFrame(records, columns=['Descricao'])

    for itemPreferencia in records:
        lstbxPreferencias.insert(END, itemPreferencia.Descricao)

    print(dfPreferencias.items)
    print(dfPreferencias)


btnMensagem = Button(frmJanela, text="mensagem", fg="black", bg="gray", width=25, height=1, command=Mensagem)
btnMensagem.place(x=35, y=50)

btnDesvCond = Button(frmJanela, text="desvio condicional", fg="black", bg="gray", width=25, height=1, command=DesvioCondicional)
btnDesvCond.place(x=35, y=100)

btnDesvCondAninhado = Button(frmJanela, text="desvio condicional aninhado", fg="black", bg="gray", width=25, height=1, command=DesvioCondicionalAninhado)
btnDesvCondAninhado.place(x=35, y=150)

btnSwitchCase = Button(frmJanela, text="switch case", fg="black", bg="gray", width=25, height=1, command=SwitchCase)
btnSwitchCase.place(x=35, y=200)

btnImpTxtWhile = Button(frmJanela, text="importar texto while", fg="black", bg="gray", width=25, height=1, command=ImpTxtWhile)
btnImpTxtWhile.place(x=35, y=250)

btnFor = Button(frmJanela, text="importar texto for", fg="black", bg="gray", width=25, height=1, command=ImpTxtFor)
btnFor.place(x=35, y=300)

btnForEach = Button(frmJanela, text="importar texto for each", fg="black", bg="gray", width=25, height=1, command=ImpTxtForEach)
btnForEach.place(x=35, y=350)

btnLstBxClear = Button(frmJanela, text="limpar a ListBox", fg="black", bg="gray", width=25, height=1, command=LstBxClear)
btnLstBxClear.place(x=35, y=400)

btnImpBDConectado = Button(frmJanela, text="importar BD Conectado ", fg="black", bg="gray", width=25, height=1, command=ImpBDCon)
btnImpBDConectado.place(x=35, y=450)

btnImpBDDesconectado = Button(frmJanela, text="importar BD Desconectado ", fg="black", bg="gray", width=25, height=1, command=ImpBDDesc)
btnImpBDDesconectado.place(x=35, y=500)

lstbxPreferencias = Listbox(frmJanela, width=35, height=31, selectmode="multiple")
lstbxPreferencias.place(x=250, y=50)

frmJanela.title("Janela de botões")
frmJanela.geometry("500x550+30+30")

frmJanela.mainloop()
