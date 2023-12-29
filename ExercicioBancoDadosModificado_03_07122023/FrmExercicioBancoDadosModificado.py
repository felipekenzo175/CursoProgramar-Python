import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
import pyodbc
import pandas as pdPreferencias

class FrmExercicioBancoDadosModificado(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        # self é o próprio objeto criado que equivale ao this que é o operador de objeto criado do c# e do java.
        super().__init__(master, *args, **kwargs)
        # __init__ é um construtor que no caso da linha de cima está instanciando a superclasse da tk.Frame
        # master é o objeto da tk.Frame
        master.title("Janela de Botões e ListBox")

        objFrmLstBxPreferencias = FrmLstBxPreferencias(self)
        objFrmLstBxPreferencias.grid(row=0, column=1, pady=20, padx=5, stick='NSEW')
        # padx = margem esquerda, pady = margem do topo.

        objFrmBtnPreferencias = FrmBtnPreferencias(self, objFrmLstBxPreferencias)
        objFrmBtnPreferencias.grid(row=0, column=0, pady=20, padx=5, stick='NSEW')

        objFrmTrvwPreferencias = FrmTrvwPreferencias(self)
        objFrmTrvwPreferencias.grid(row=1, column=1, pady=20, padx=5, stick='NSEW', ipadx=5, ipady=5)
        #stick='NSEW' -> para se adequar ao uso que está sendo solicitado, facilitador(para não precisar dizer posicionamento).
        #stick é a responsividade do grid.
class FrmBtnPreferencias(tk.Frame):
    def __init__(self, master, objFrmLstBxPreferencias, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.objFrmLstBxPreferencias = objFrmLstBxPreferencias

        btnMensagem = Button(self, text="Mensagem", fg="black", bg="grey", width=25, height=1, command=self.Mensagem)
        btnMensagem.place(x=35, y=50)
        btnMensagem.grid(row=0, column=0, pady=5)

        btnDesvioCondicional = Button(self, text="Desvio Condicional", fg="black", bg="grey", width=25, height=1, command=self.DesvioCondicional)
        btnDesvioCondicional.place(x=35, y=100)
        btnDesvioCondicional.grid(row=1, column=0, pady=5)

        btnDesvioCondicionalEncadeado = Button(self, text="Desvio Condicional Encadeado", fg="black", bg="grey", width=25, height=1, command=self.DesvioCondicionalEncadeado)
        btnDesvioCondicionalEncadeado.place(x=35, y=150)
        btnDesvioCondicionalEncadeado.grid(row=2, column=0, pady=5)

        btnSwitchCase = Button(self, text="Switch Case", fg="black", bg="grey", width=25, height=1, command=self.SwitchCase)
        btnSwitchCase.place(x=35, y=200)
        btnSwitchCase.grid(row=3, column=0, pady=5)

        btnImpTxtWhile = Button(self, text="Importar Texto While", fg="black", bg="grey", width=25, height=1, command=self.ImpTxtWhile)
        btnImpTxtWhile.place(x=35, y=250)
        btnImpTxtWhile.grid(row=4, column=0, pady=5)

        btnImpTxtFor = Button(self, text="Importar Texto For", fg="black", bg="grey", width=25, height=1, command=self.ImpTxtFor)
        btnImpTxtFor.place(x=35, y=300)
        btnImpTxtFor.grid(row=5, column=0, pady=5)

        btnImpTxtForEach = Button(self, text="Importar Texto For Each", fg="black", bg="grey", width=25, height=1, command=self.ImpTxtForEach)
        btnImpTxtForEach.place(x=35, y=350)
        btnImpTxtForEach.grid(row=6, column=0, pady=5)

        btnClear = Button(self, text="Clear", fg="black", bg="grey", width=25, height=1, command=self.Clear)
        btnClear.place(x=35, y=400)
        btnClear.grid(row=7, column=0, pady=5)

        btnImpBancoConectado = Button(self, text="Importar Banco Conectado", fg="black", bg="grey", width=25, height=1, command=self.ImpBancoConectado)
        btnImpBancoConectado.place(x=35, y=450)
        btnImpBancoConectado.grid(row=8, column=0, pady=5)

        btnImpBancoDesconectado = Button(self, text="Importar Banco Desconectado", fg="black", bg="grey", width=25, height=1, command=self.ImpBancoDesconectado)
        btnImpBancoDesconectado.place(x=35, y=500)
        btnImpBancoDesconectado.grid(row=9, column=0, pady=5)


    def Mensagem(self):
        messagebox.showinfo("MENSAGEM", "Olá, Mundo!")

    def DesvioCondicional(self):
        if messagebox.askyesno("DESVIO CONDICIONAL", "escolha sim ou não") == True:
            messagebox.showinfo("OPÇÃO", "você escolheu sim")
        else:
            messagebox.showinfo("OPÇÃO", "você escolheu não")

    def DesvioCondicionalEncadeado(self):
        resultado = messagebox.askyesnocancel("DESVIO CONDICIONAL ENCADEADO", "escolha sim, não ou cancelar")
        if resultado == True:
            messagebox.showinfo("OPÇÃO", "você escolheu sim")
        elif resultado == False:
            messagebox.showinfo("OPÇÃO", "você escolheu não")
        else:
            messagebox.showinfo("OPÇÃO", "você escolheu cancelar")

    def SwitchCase(self):
        resultado = messagebox.askyesnocancel("DESVIO CONDICIONAL ENCADEADO", "escolha sim, não ou cancelar")
        match (resultado):
            case True:
                messagebox.showinfo("OPÇÃO", "você escolheu sim")
            case False:
                messagebox.showinfo("OPÇÃO", "você escolheu não")
            case None:
                messagebox.showinfo("OPÇÃO", "você escolheu cancelar")
            case _:
                messagebox.showinfo("OPÇÃO", "você escolheu errado, escolha sim, não ou cancelar")

    def ImpTxtWhile(self):
        objLeitorTxt = open("C:\CURSO PROGRAMAR\Python\preferencias.txt")
        strLinhaLida = objLeitorTxt.readline()

        dados = []
        while (strLinhaLida != ""):
            dados.append(strLinhaLida)
            strLinhaLida = objLeitorTxt.readline()

        objLeitorTxt.close()

        self.objFrmLstBxPreferencias.preencherLstBxPreferencias(dados)

    def ImpTxtFor(self):
        objLeitorTxt = open("C:\CURSO PROGRAMAR\Python\preferencias.txt")
        strLinhasLidas = objLeitorTxt.readlines()

        dados = []
        for item in range(len(strLinhasLidas)):
            dados.append(strLinhasLidas[item])

        objLeitorTxt.close()

        self.objFrmLstBxPreferencias.preencherLstBxPreferencias(dados)

    def ImpTxtForEach(self):
        objLeitorTxt = open("C:\CURSO PROGRAMAR\Python\preferencias.txt")
        strLinhasLidas = objLeitorTxt.readlines()

        dados = []
        for item in strLinhasLidas:
            dados.append(item)

        objLeitorTxt.close()

        self.objFrmLstBxPreferencias.preencherLstBxPreferencias(dados)

    def Clear(self):
        self.objFrmLstBxPreferencias.limpaLstBxPreferencias()

    def ImpBancoConectado(self):
        connectionString = (
            r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
            r'DBQ=C:\CURSO PROGRAMAR\Python\Preferencias_1_05072023.accdb;'
        )

        objConexao = pyodbc.connect(connectionString)
        objLeitorBD = objConexao.cursor()

        strSQL = "SELECT Descricao FROM Preferencias_3;"

        objLeitorBD.execute(strSQL)

        record = objLeitorBD.fetchone()

        dados = []
        while record != None:
            dados.append(record.Descricao)
            record = objLeitorBD.fetchone()

        objLeitorBD.close()
        objConexao.close()

        self.objFrmLstBxPreferencias.preencherLstBxPreferencias(dados)

    def ImpBancoDesconectado(self):
        connectionString = (
            r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
            r'DBQ=C:\CURSO PROGRAMAR\Python\Preferencias_1_05072023.accdb;'
        )

        objConexao = pyodbc.connect(connectionString)
        objLeitorBD = objConexao.cursor()

        strSQL = "SELECT Descricao FROM Preferencias_3;"

        objLeitorBD.execute(strSQL)

        records = objLeitorBD.fetchall()

        dfPreferencias = pdPreferencias.DataFrame(records, columns=["Descricao"])

        dados = []
        for item in records:
            dados.append(item.Descricao)

        objConexao.close()

        self.objFrmLstBxPreferencias.preencherLstBxPreferencias(dados)



class FrmLstBxPreferencias(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.lstBxPreferencias = Listbox(self, width=32, height=22)
        self.lstBxPreferencias.pack(fill='both', expand=False, pady=5)




    def limpaLstBxPreferencias(self):
        self.lstBxPreferencias.delete(0, END)


    def preencherLstBxPreferencias(self, linhas):
        self.limpaLstBxPreferencias()
        for linha in linhas:
            self.lstBxPreferencias.insert(END, linha)


    def importarFamiliares(self, linhas):
        try:
            self.treeview.delete(*self.treeview.get_children())
            for linha in linhas:
                self.treeview.insert('', 'end', values=list(linha))
        except Exception as e:
            raise e

class FrmTrvwPreferencias(tk.LabelFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.btnWidth = 25
        self.btnPady = 5
        self.btnPadx = 35

        self.FrmBotoes = tk.Frame(self)
        self.FrmBotoes.pack(side='left')

        self.btnConsultarBD = tk.Button(self.FrmBotoes, width=self.btnWidth, background='grey', text="Consultar", command=self.ConsultarBancoDados)
        self.btnConsultarBD.pack(side='top', padx=self.btnPadx, pady=self.btnPady)

        self.btnIncluirBD = tk.Button(self.FrmBotoes, width=self.btnWidth, background='grey', text="Inserir", command=self.AdicionarPreferencia)
        self.btnIncluirBD.pack(side='top', padx=self.btnPadx, pady=self.btnPady)

        # Configurações da tabela para visualizar os dados
        self.cols = ["ID", "Descricao"]
        self.colsSize = [100, 100]
        self.colsAnchor = [tk.CENTER, tk.W]

        # Declaração da tabela e atribuição das propriedades de cada coluna
        self.treeview = ttk.Treeview(self, columns=self.cols, height=6, show='headings')
        self.treeview.pack(side='left')

        for i in range(len(self.cols)):
            self.treeview.heading(self.cols[i], text=self.cols[i])
            self.treeview.column(self.cols[i], width=self.colsSize[i], anchor=self.colsAnchor[i])

        linhas = self.ConsultarBancoDados()

        self.treeview.delete(*self.treeview.get_children()) #função limpar treeview

        for linhaBD in linhas:
            self.treeview.insert('', 'end', values=list(linhaBD))

    def ConsultarBancoDados(self):
        connectionString = (
            r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
            r'DBQ=C:\CURSO PROGRAMAR\Python\Preferencias_1_05072023.accdb;'
        )

        objConexao = pyodbc.connect(connectionString)
        objLeitorBD = objConexao.cursor()

        strSQL = "SELECT ID, Descricao FROM Preferencias_3;"

        objLeitorBD.execute(strSQL)

        records = objLeitorBD.fetchall()

        objConexao.close()

        dados = []
        for item in records:
            dados.append(item)

        return dados


    def AdicionarPreferencia(self):
        try:
            frmAddPreferencia()

            for i in range(len(self.cols)):
                self.treeview.heading(self.cols[i], text=self.cols[i])
                self.treeview.column(self.cols[i], width=self.colsSize[i], anchor=self.colsAnchor[i])

            linhas = self.ConsultarBancoDados()

            self.treeview.delete(*self.treeview.get_children())  # função limpar treeview

            for linhaBD in linhas:
                self.treeview.insert('', 'end', values=list(linhaBD))

        except Exception as ex:
            messagebox.showinfo('ERRO', str(ex))

class BuilderEntry(tk.Frame):
    def __init__(self, master, labelText, entryWidth = 20, varType = str, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.entryVar = tk.StringVar()
        self.varType = varType

        self.lblDescricao = tk.Label(self, text=labelText, anchor='w')
        self.lblDescricao.pack(side='top', fill='x')

        self.txtDescricao = tk.Entry(self, textvariable=self.entryVar, width=entryWidth)
        self.txtDescricao.pack(side='bottom', anchor='w')


    def get(self):
        valor = self.txtDescricao.get()
        try:
            return (self.varType(valor))
        except (ValueError, TypeError):
            return None


    def set(self, valor):
        self.txtDescricao.delete(0, tk.END)
        self.txtDescricao.insert(0, valor)


class frmAddPreferencia(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('Adicionar Preferencia')

        self.txtDescricao = BuilderEntry(self, 'Descricao')
        self.txtDescricao.pack(side='top', padx=5, pady=5)

        self.btnSalvar = tk.Button(self, text='Salvar', width=10, command=self.AddPreferencia)
        self.btnSalvar.pack(side='top', padx=5, pady=5)

        self.mainloop()

    def AddPreferencia(self):
        if messagebox.askokcancel('Confirmar Inclusão', f'Confirma inclusão de Preferencia {self.txtDescricao.get()}?') is True:
            try:
                connectionString = (
                    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                    r'DBQ=C:\CURSO PROGRAMAR\Python\Preferencias_1_05072023.accdb;'
                )

                objConexao = pyodbc.connect(connectionString)
                objLeitorBD = objConexao.cursor()

                strDescricao = self.txtDescricao.get()

                strSQL = "INSERT INTO Preferencias_3 (Descricao) VALUES (?);"


                objLeitorBD.execute(strSQL, (strDescricao))

                objLeitorBD.commit()

            except Exception as ex:
                messagebox.showinfo('ERRO', str(ex))
            else:
                messagebox.showinfo('SUCESSO', 'Preferencia adicionada com Sucesso!')
                self.destroy()

            finally:
                objConexao.close()