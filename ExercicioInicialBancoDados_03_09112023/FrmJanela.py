import tkinter as tk
from tkinter import messagebox
from tkinter import *
import pyodbc
import pandas as pdPreferencias

class FrmJanela(tk.Frame):

    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        master.title("Janela de Botões")
        master.geometry("550x550+30+30")


        btnMensagem = Button(self, text="Mensagem", fg="black", bg="grey", width=25, height=1, command=self.Mensagem)
        btnMensagem.place(x=35, y=50)
        btnMensagem.grid(row=0, column=0, pady=5)

        btnDesvioCondicional = Button(self, text="Desvio Condicional", fg="black", bg="grey", width=25, height=1,
                                      command=self.DesvioCondicional)
        btnDesvioCondicional.place(x=35, y=100)
        btnDesvioCondicional.grid(row=1, column=0, pady=5)

        btnDesvioCondicionalEncadeado = Button(self, text="Desvio Condicional Encadeado", fg="black", bg="grey",
                                               width=25, height=1, command=self.DesvioCondicionalEncadeado)
        btnDesvioCondicionalEncadeado.place(x=35, y=150)
        btnDesvioCondicionalEncadeado.grid(row=2, column=0, pady=5)

        btnSwitchCase = Button(self, text="Switch Case", fg="black", bg="grey", width=25, height=1,
                               command=self.SwitchCase)
        btnSwitchCase.place(x=35, y=200)
        btnSwitchCase.grid(row=3, column=0, pady=5)

        btnImpTxtWhile = Button(self, text="Importar Texto While", fg="black", bg="grey", width=25, height=1,
                                command=self.impTxtWhile)
        btnImpTxtWhile.place(x=35, y=250)
        btnImpTxtWhile.grid(row=4, column=0, pady=5)

        btnImpTxtFor = Button(self, text="Importar Texto For", fg="black", bg="grey", width=25, height=1,
                              command=self.impTxtFor)
        btnImpTxtFor.place(x=35, y=300)
        btnImpTxtFor.grid(row=5, column=0, pady=5)

        btnImpTxtForEach = Button(self, text="Importar Texto ForEach", fg="black", bg="grey", width=25, height=1,
                                  command=self.impTxtForEach)
        btnImpTxtForEach.place(x=35, y=350)
        btnImpTxtForEach.grid(row=6, column=0, pady=5)

        btnClear = Button(self, text="Clear", fg="black", bg="grey", width=25, height=1, command=self.Clear)
        btnClear.place(x=35, y=400)
        btnClear.grid(row=7, column=0, pady=5)

        btnBancoConectado = Button(self, text="Importar Banco Conectado", fg="black", bg="grey", width=25, height=1,
                                   command=self.impBancoConectado)
        btnBancoConectado.place(x=35, y=450)
        btnBancoConectado.grid(row=8, column=0, pady=5)

        btnBancoDesconectado = Button(self, text="Importar Banco Desconectado", fg="black", bg="grey", width=25,
                                      height=1, command=self.impBancoDesconectado)
        btnBancoDesconectado.place(x=35, y=500)
        btnBancoDesconectado.grid(row=9, column=0, pady=5)

        lstbxPreferencias = Listbox(self, width=35, height=30, selectmode="multiple")
        lstbxPreferencias.place(x=250, y=50)
        lstbxPreferencias.grid(row=0, column=1, pady=5)


    def Mensagem():
        messagebox.showinfo("MENSAGEM","Olá, Mundo!")


    def DesvioCondicional():
        if messagebox.askyesno("desvio condiconal", "escolha sim ou não") == True:
            messagebox.showinfo("opção", "você escolheu sim")
        else:
            messagebox.showinfo("opção", "você escolheu não")


    def DesvioCondicionalEncadeado():
        resultado = messagebox.askyesnocancel("desvio condicional encadeado", "escolha sim, não ou cancelar")
        if resultado == True:
            messagebox.showinfo("opção", "você escolheu sim")
        elif resultado == False:
            messagebox.showinfo("opção", "você escolheu não")
        else:
            messagebox.showinfo("opção", "você escolheu cancelar")


    def SwitchCase():
        resultado = messagebox.askyesnocancel("switch case", "escolha sim, não ou cancelar")
        match(resultado):
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


    def impBancoConectado():
        lstbxPreferencias.delete(0, END)

        connectionString = (
            r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
            r'DBQ=C:\CURSO PROGRAMAR\Python\Preferencias_1_05072023.accdb;'
        )

        objConexao = pyodbc.connect(connectionString)
        objLeitorBD = objConexao.cursor()

        strSQL = "SELECT Descricao FROM Preferencias_3;"

        objLeitorBD.execute(strSQL)

        record = objLeitorBD.fetchone()

        while record != None:
            lstbxPreferencias.insert(END, record.Descricao)
            record = objLeitorBD.fetchone()

        objLeitorBD.close()
        objConexao.close()


    def impBancoDesconectado():
        lstbxPreferencias.delete(0, END)

        connectionString = (
            r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
            r'DBQ=C:\CURSO PROGRAMAR\Python\Preferencias_1_05072023.accdb;'
        )

        objConexao = pyodbc.connect(connectionString)
        objLeitorBD = objConexao.cursor()

        strSQL = "SELECT Descricao FROM Preferencias_3;"

        objLeitorBD.execute(strSQL)

        records = objLeitorBD.fetchall()

        dfPreferencias = pdPreferencias.DataFrame(records, columns=['Descricao'])

        for item in records:
            lstbxPreferencias.insert(END, item.Descricao)

        objConexao.close()



