import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
import pyodbc
import pandas as pdPreferencias

class FrmExercicioBancoDeDadosModificado_06_18012024(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        master.title("Exercicio Banco De Dados Modificado 06 18/01/2024")

        objFrmLstbxPreferencias = FrmLstBxPreferencias(self)
        objFrmLstbxPreferencias.grid(row=0, column=1, padx=5, pady=20, sticky='NSEW')

        objFrmBtnPreferencias = FrmBtnPreferencias(self, objFrmLstbxPreferencias)
        objFrmBtnPreferencias.grid(row=0, column=0, padx=5, pady=20, sticky='NSEW')

        objFrmTrvwPreferencias = FrmTrvwPreferencias(self)
        objFrmTrvwPreferencias.grid(row=1, column=1, padx=5, pady=20, sticky='NSEW')


class FrmBtnPreferencias(tk.Frame):
    def __init__(self, master, objFrmLstbxPreferencias, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.objFrmLstbxPreferencias = objFrmLstbxPreferencias

        btnMensagem = Button(self, text='Mensagem', fg='black', bg='gray', width=25, height=1, command=self.Mensagem)
        btnMensagem.place(x=35, y=50)
        btnMensagem.grid(row=0, column=0, padx=5, pady=5)

        btnDesvioCondicional = Button(self, text='Desvio Condicional', fg='black', bg='gray', width=25, height=1, command=self.DesvioCondicional)
        btnDesvioCondicional.place(x=35, y=100)
        btnDesvioCondicional.grid(row=1, column=0, padx=5, pady=5)

        btnDesvioCondicionalEncadeado = Button(self, text='Desvio Condicional Encadeado', fg='black', bg='gray', width=25, height=1, command=self.DesvioCondicionalEncadeado)
        btnDesvioCondicionalEncadeado.place(x=35, y=150)
        btnDesvioCondicionalEncadeado.grid(row=2, column=0, padx=5, pady=5)

        btnSwitchCase = Button(self, text='Switch Case', fg='black', bg='gray', width=25, height=1, command=self.SwitchCase)
        btnSwitchCase.place(x=35, y=200)
        btnSwitchCase.grid(row=3, column=0, padx=5, pady=5)

        btnImpTxtWhile = Button(self, text='Importar Texto While', fg='black', bg='gray', width=25, height=1, command=self.ImpTxtWhile)
        btnImpTxtWhile.place(x=35, y=250)
        btnImpTxtWhile.grid(row=4, column=0, padx=5, pady=5)

        btnImpTxtFor = Button(self, text='Importar Texto For', fg='black', bg='gray', width=25, height=1, command=self.ImpTxtFor)
        btnImpTxtFor.place(x=35, y=300)
        btnImpTxtFor.grid(row=5, column=0, padx=5, pady=5)

        btnImpTxtForEach = Button(self, text='Importar Texto For Each', fg='black', bg='gray', width=25, height=1, command=self.ImpTxtForEach)
        btnImpTxtForEach.place(x=35, y=350)
        btnImpTxtForEach.grid(row=6, column=0, padx=5, pady=5)

        btnBancoConectado = Button(self, text='Banco Conectado', fg='black', bg='gray', width=25, height=1, command=self.BancoConectado)
        btnBancoConectado.place(x=35, y=400)
        btnBancoConectado.grid(row=7, column=0, padx=5, pady=5)

        btnBancoDesconectado = Button(self, text='Banco Desconectado', fg='black', bg='gray', width=25, height=1, command=self.BancoDesconectado)
        btnBancoDesconectado.place(x=35, y=450)
        btnBancoDesconectado.grid(row=8, column=0, padx=5, pady=5)

        btnClear = Button(self, text='Clear', fg='black', bg='gray', width=25, height=1, command=self.Clear)
        btnClear.place(x=35, y=500)
        btnClear.grid(row=9, column=0, padx=5, pady=5)

    def Mensagem(self):
        messagebox.showinfo('Mensagem', 'Ola, Mundo')

    def DesvioCondicional(self):
        if messagebox.askyesno('desvio condicional', 'Escolha sim ou não') == True:
            messagebox.showinfo('Mensagem', 'Você escolheu Sim')
        else:
            messagebox.showinfo('Mensagem', 'Você escolheu Não')

    def DesvioCondicionalEncadeado(self):
        resultado = messagebox.askyesnocancel('desvio condicional', 'Escolha sim, não ou cancelar')
        if resultado == True:
            messagebox.showinfo('Mensagem', 'Você escolheu Sim')
        elif resultado == False:
            messagebox.showinfo('Mensagem', 'Você escolheu Não')
        else:
            messagebox.showinfo('Mensagem', 'Você escolheu Cancelar')

    def SwitchCase(self):
        resultado = messagebox.askyesnocancel('desvio condicional', 'Escolha sim, não ou cancelar')
        match(resultado):
            case True:
                messagebox.showinfo('Mensagem', 'Você escolheu Sim')
            case False:
                messagebox.showinfo('Mensagem', 'Você escolheu Não')
            case None:
                messagebox.showinfo('Mensagem', 'Você escolheu Cancelar')
            case _:
                messagebox.showinfo('Mensagem', 'Você escolheu Errado, Escolha sim, não ou cancelar')


    def ImpTxtWhile(self):
        objLeitorTxt = open("C:\CURSO PROGRAMAR\Python\preferencias.txt")
        strLinhaLida = objLeitorTxt.readline()

        self.objFrmLstbxPreferencias.limpaLstBxPreferencias()

        while(strLinhaLida != ""):
            self.objFrmLstbxPreferencias.insert(END, strLinhaLida)
            objLeitorTxt.readline()

        objLeitorTxt.close()

    def ImpTxtFor(self):
        objLeitorTxt = open("C:\CURSO PROGRAMAR\Python\preferencias.txt")
        strLinhasLidas = objLeitorTxt.readlines()

        self.objFrmLstbxPreferencias.limpaLstBxPreferencias()

        for item in range(len(strLinhasLidas)):
            self.objFrmLstbxPreferencias.insert(END, strLinhasLidas[item])

        objLeitorTxt.close()


    def ImpTxtForEach(self):
        objLeitorTxt = open("C:\CURSO PROGRAMAR\Python\preferencias.txt")
        strLinhasLidas = objLeitorTxt.readlines()

        self.objFrmLstbxPreferencias.limpaLstBxPreferencias()

        for item in strLinhasLidas:
            self.objFrmLstbxPreferencias.insert(END, item)

        objLeitorTxt.close()


    def Clear(self):
        self.objFrmLstbxPreferencias.limpaLstBxPreferencias()

    def BancoConectado(self):
        connectionString = {
            r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
            r'DBQ=C:\CURSO PROGRAMAR\Python\Preferencias_1_05072023.accdb;'
        }

        objConexao = pyodbc.connect(connectionString)
        objLeitorBD = objConexao.cursor()

        strSql = 'SELECT Descricao FROM Preferencias_3;'

        objLeitorBD.execute(strSql)

        record = objLeitorBD.fetchone()

        self.objFrmLstbxPreferencias.limpaLstBxPreferencias()

        while record != None:
            self.objFrmLstbxPreferencias.insert(END, record.Descricao)
            record = objLeitorBD.fetchone()

        objLeitorBD.close()
        objConexao.close()

    def BancoDesconectado(self):
        connectionString = {
            r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
            r'DBQ=C:\CURSO PROGRAMAR\Python\Preferencias_1_05072023.accdb;'
        }

        objConexao = pyodbc.connect(connectionString)
        objLeitorBD = objConexao.cursor()

        strSql = 'SELECT Descricao FROM Preferencias_3;'

        objLeitorBD.execute(strSql)

        records = objLeitorBD.fetchall()

        dfPreferencias = pdPreferencias.DataFrame(records, columns=['Descricao'])

        self.objFrmLstbxPreferencias.limpaLstBxPreferencias()

        for item in records:
            self.objFrmLstbxPreferencias.insert(END, item.Descricao)

        objConexao.close()

class FrmLstBxPreferencias(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.LstBxPreferencias = Listbox(self, width=32, height=22)
        self.LstBxPreferencias.pack(fill='both', expand=False, pady=5)

    def limpaLstBxPreferencias(self):
        self.LstBxPreferencias.delete(0, END)


class FrmTrvwPreferencias(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.btnWidth = 25
        self.btnPady = 5
        self.btnPadx = 35

        self.FrmBotoes = tk.Frame(self)
        self.FrmBotoes.pack(side='left')

        self.btnConsultarBD = tk.Button(self.FrmBotoes, width=self.btnWidth, text='Consultar', background='gray', command=self.ConsultarBD)
        self.btnConsultarBD.pack(side='top', padx=self.btnPadx, pady=self.btnPady)

        self.btnIncluirBD = tk.Button(self.FrmBotoes, width=self.btnWidth, text='Incluir', background='gray', command=self.InserirBD)
        self.btnIncluirBD.pack(side='top', padx=self.btnPadx, pady=self.btnPady)

        self.cols = ["ID", "Descricao"]
        self.colsSize = [100, 100]
        self.colsAnchor = [tk.CENTER, tk.W]

        self.treeview = ttk.Treeview(self, columns=self.cols, height=6, show='headings')
        self.treeview.pack(side='left')

        for i in range(len(self.cols)):
            self.treeview.heading(self.cols[i])
            self.treeview.column(self.cols[i], width=self.colsSize[i], anchor=self.colsAnchor[i])

        linhas = self.ConsultarBD()

        self.treeview.delete(*self.treeview.get_children())

        for linhaBD in linhas:
            self.treeview.insert("", "end", values=list(linhaBD))

    def ConsultarBD(self):
        connectionString = {
            r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
            r'DBQ=C:\CURSO PROGRAMAR\Python\Preferencias_1_05072023.accdb;'
        }

        objConexao = pyodbc.connect(connectionString)
        objLeitorBD = objConexao.cursor()

        strSql = 'SELECT ID, Descricao FROM Preferencias_3;'

        objLeitorBD.execute(strSql)

        records = objLeitorBD.fetchall()

        objConexao.close()

        return records


    def InserirBD(self):
        try:
            objFrmAddPreferencia = FrmAddPreferencia()

            for i in range(len(self.cols)):
                self.treeview.heading(self.cols[i])
                self.treeview.column(self.cols[i], width=self.colsSize[i], anchor=self.colsAnchor[i])

            linhas = self.ConsultarBD()

            self.treeview.delete(*self.treeview.get_children())

            for linhaBD in linhas:
                self.treeview.insert('end', values=list(linhaBD))

        except Exception as ex:
            messagebox.showinfo(title='Erro', message=str(ex))


class BuilderEntry(tk.Frame):
    def __init__(self, master, labelText, entryWidth = 20, varType = str, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.varType = varType
        self.entryVar = tk.StringVar()

        self.lblDescricao = tk.Label(self, text=labelText, anchor='w')
        self.lblDescricao.pack(side='top', fill='x')

        self.lblDescricao = tk.Entry(self, textvariable=self.entryVar, width=entryWidth)
        self.lblDescricao.pack(side='bottom', anchor='w')

    def get(self):
        valor = self.txtDescricao.get()
        try:
            return(self.varType(valor))
        except (ValueError, TypeError):
            return None

    def set(self, valor):
        self.txtDescricao.delete(0, tk.END)
        self.txtDescricao.insert(0, valor)

class FrmAddPreferencia(tk.Toplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('Adicionar Preferencia')

        self.txtDescricao = BuilderEntry(self, 'Descricao')
        self.txtDescricao.pack(side='top', padx=5, pady=5)

        self.btnSalvar = tk.Button(self, text='Salvar', command=self.AddPreferencia)
        self.btnSalvar.pack(side='top', padx=5, pady=5)

    def AddPreferencia(self):
        if messagebox.askokcancel('Inclusao de Preferencia', f'Confirma inclusao de Preferencia{self.txtDescricao.get()}?') == True:
            try:
                connectionString = {
                    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                    r'DBQ=C:\CURSO PROGRAMAR\Python\Preferencias_1_05072023.accdb;'
                }

                objConexao = pyodbc.connect(connectionString)
                objLeitorBD = objConexao.cursor()

                strSql = 'SELECT INTO Preferencias_3 (Descricao) VALUES (?);'

                objLeitorBD.execute(strSql, (self.txtDescricao.get()))

                objLeitorBD.commit()

            except Exception as ex:
                messagebox.showerror('Erro', str(ex))
            else:
                messagebox.showerror('Sucesso', 'Adicionado com sucesso')
            finally:
                objConexao.close()

        self.destroy()
