import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import Scrollbar
from tkinter import messagebox
import pyodbc
import pandas as pdPreferencias


class FrmAlterarBD_03_29022024(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        master.title('Alterar BD - 03 - 29/02/2024')

        objFrmLstBxPreferencias = FrmLstBxPreferencias(self)
        objFrmLstBxPreferencias.grid(row=0, column=1, padx=5, pady=20, sticky='NSEW')

        objFrmBtnPreferencias = FrmBtnPreferencias(self, objFrmLstBxPreferencias)
        objFrmBtnPreferencias.grid(row=0, column=0, padx=40, pady=20, sticky='NSEW')

        objFrmTrvwPreferencias = FrmTrvwPreferencias(self)
        objFrmTrvwPreferencias.grid(row=1, column=1, padx=5, pady=20, sticky='NSEW')

        objFrmBtnTrvwPreferencias = FrmBtnTrvwPreferencias(self, objFrmTrvwPreferencias)
        objFrmBtnTrvwPreferencias.grid(row=1, column=0, padx=5, pady=20, sticky='NSEW')


class FrmLstBxPreferencias(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.LstBxPreferencias = Listbox(self, width=32, height=22)
        self.LstBxPreferencias.pack(fill='both', expand=False, pady=5)


    def limpaLstBxPreferencias(self):
        self.LstBxPreferencias.delete(0, END)


class FrmBtnPreferencias(tk.Frame):
    def __init__(self, master, objFrmLstBxPreferencias, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.objFrmLstBxPreferencias = objFrmLstBxPreferencias

        btnMensagem = Button(self, text="Mensagem", fg="black", bg="grey", width=25, height=1, command=self.mensagem)
        btnMensagem.place(x=100, y=50)
        btnMensagem.grid(row=0, column=0, pady=5)

        btnDesvioCondicional = Button(self, text="Desvio Condicional", fg="black", bg="grey", width=25, height=1, command=self.desvioCondicional)
        btnDesvioCondicional.place(x=100, y=100)
        btnDesvioCondicional.grid(row=1, column=0, pady=5)

        btnDesvioCondicionalEncadeado = Button(self, text="Desvio Condicional Encadeado", fg="black", bg="grey", width=25, height=1, command=self.desvioCondicionalEncadeado)
        btnDesvioCondicionalEncadeado.place(x=100, y=150)
        btnDesvioCondicionalEncadeado.grid(row=2, column=0, pady=5)

        btnSwitchCase = Button(self, text="Switch Case", fg="black", bg="grey", width=25, height=1, command=self.switchCase)
        btnSwitchCase.place(x=100, y=200)
        btnSwitchCase.grid(row=3, column=0, pady=5)

        btnImpTxtWhile = Button(self, text="Importar Texto While", fg="black", bg="grey", width=25, height=1, command=self.impTxtWhile)
        btnImpTxtWhile.place(x=100, y=250)
        btnImpTxtWhile.grid(row=4, column=0, pady=5)

        btnImpTxtFor = Button(self, text="Importar Texto For", fg="black", bg="grey", width=25, height=1, command=self.impTxtFor)
        btnImpTxtFor.place(x=100, y=300)
        btnImpTxtFor.grid(row=5, column=0, pady=5)

        btnImpTxtForEach = Button(self, text="Importar Texto For Each", fg="black", bg="grey", width=25, height=1, command=self.impTxtForEach)
        btnImpTxtForEach.place(x=100, y=350)
        btnImpTxtForEach.grid(row=6, column=0, pady=5)

        btnClear = Button(self, text="Clear", fg="black", bg="grey", width=25, height=1, command=self.clear)
        btnClear.place(x=100, y=400)
        btnClear.grid(row=7, column=0, pady=5)

        btnBancoConectado = Button(self, text="Banco Conectado", fg="black", bg="grey", width=25, height=1, command=self.bancoConectado)
        btnBancoConectado.place(x=100, y=450)
        btnBancoConectado.grid(row=8, column=0, pady=5)

        btnBancoDesconectado = Button(self, text="Banco Desconectado", fg="black", bg="grey", width=25, height=1, command=self.bancoDesconectado)
        btnBancoDesconectado.place(x=100, y=500)
        btnBancoDesconectado.grid(row=9, column=0, pady=5)


    def mensagem(self):
        messagebox.showinfo("mensagem", "Olá, Mundo!")


    def desvioCondicional(self):
        if messagebox.askyesno("desvio condicional", "Escolha Sim ou Não") == True:
            messagebox.showinfo("opção", "Você escolheu Sim")
        else:
            messagebox.showinfo("opção", "Você escolheu Não")


    def desvioCondicionalEncadeado(self):
        resultado = messagebox.askyesnocation("Desvio Condicional Encadeado", "Escolha sim, não ou cancelar")

        if resultado == True:
            messagebox.showinfo("opção", "Você escolheu Sim")
        elif resultado == False:
            messagebox.showinfo("opção", "Você escolheu Não")
        else:
            messagebox.showinfo("opção", "Você escolheu Cancelar")


    def switchCase(self):
        resultado = messagebox.askyesnocancel("Switch Case", "Escolha sim, não ou cancelar")

        match(resultado):
            case True:
                messagebox.showinfo("opção", "Você escolheu Sim")
            case False:
                messagebox.showinfo("opção", "Você escolheu Não")
            case None:
                messagebox.showinfo("opção", "Você escolheu Cancelar")
            case _:
                messagebox.showinfo("opção", "Opção Inválida")


    def impTxtWhile(self):
        objLeitorTxt = open("C:\CURSO PROGRAMAR\Python\preferencias.txt")
        strLinhaLida = objLeitorTxt.readline()

        self.objFrmLstBxPreferencias.limpaLstBxPreferencias()

        while strLinhaLida != "":
            self.objFrmLstBxPreferencias.LstBxPreferencias.insert(END, strLinhaLida)
            strLinhaLida = objLeitorTxt.readline()

        objLeitorTxt.close()


    def impTxtFor(self):
        objLeitorTxt = open("C:\CURSO PROGRAMAR\Python\preferencias.txt")
        strLinhaLidas = objLeitorTxt.readlines()

        self.objFrmLstBxPreferencias.limpaLstBxPreferencias()

        for linha in range(len(strLinhaLidas)):
            self.objFrmLstBxPreferencias.LstBxPreferencias.insert(END, strLinhaLidas[linha])

        objLeitorTxt.close()


    def impTxtForEach(self):
        objLeitorTxt = open("C:\CURSO PROGRAMAR\Python\preferencias.txt")
        strLinhaLidas = objLeitorTxt.readlines()

        self.objFrmLstBxPreferencias.limpaLstBxPreferencias()

        for linha in strLinhaLidas:
            self.objFrmLstBxPreferencias.LstBxPreferencias.insert(END, linha)

        objLeitorTxt.close()


    def clear(self):
        self.objFrmLstBxPreferencias.limpaLstBxPreferencias()


    def bancoConectado(self):
        connectionString = (
            r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
            r'DBQ=C:\CURSO PROGRAMAR\Python\Preferencias_1_05072023.accdb;'
        )

        objConexao = pyodbc.connect(connectionString)
        objLeitorBD = objConexao.cursor()

        strSql = "SELECT Descricao FROM Preferencias_3;"

        objLeitorBD.execute(strSql)

        record = objLeitorBD.fetchone()

        self.objFrmLstBxPreferencias.limpaLstBxPreferencias()

        while record != None:
            self.objFrmLstBxPreferencias.LstBxPreferencias.insert(END, record.Descricao)
            record = objLeitorBD.fetchone()

        objLeitorBD.close()
        objConexao.close()


    def bancoDesconectado(self):
        connectionString = (
            r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
            r'DBQ=C:\CURSO PROGRAMAR\Python\Preferencias_1_05072023.accdb;'
        )

        objConexao = pyodbc.connect(connectionString)
        objLeitorBD = objConexao.cursor()

        strSql = "SELECT Descricao FROM Preferencias_3;"

        objLeitorBD.execute(strSql)

        records = objLeitorBD.fetchall()

        dfPreferencias = pdPreferencias.DataFrame(records, columns=['Descricao'])

        self.objFrmLstBxPreferencias.limpaLstBxPreferencias()

        objConexao.close()

        for item in records:
            self.objFrmLstBxPreferencias.LstBxPreferencias.insert(END, item.Descricao)


class FrmBtnTrvwPreferencias(tk.Frame):
    def __init__(self, master, objFrmTrvwPreferencias, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.objFrmTrvwPreferencias = objFrmTrvwPreferencias

        self.btnWidth = 25
        self.btnPady = 5
        self.btnPadx = 35

        self.FrmBotoes = tk.Frame(self)
        self.FrmBotoes.pack(side='left')

        self.btnConsultarBD = tk.Button(self.FrmBotoes, width=self.btnWidth, background='grey', text='Consultar', command=self.objFrmTrvwPreferencias.ConsultBD)
        self.btnConsultarBD.pack(side='top', padx=self.btnPadx, pady=self.btnPady)

        self.btnIncluirBD = tk.Button(self.FrmBotoes, width=self.btnWidth, background='grey', text='Inserir', command=self.objFrmTrvwPreferencias.InserirBD)
        self.btnIncluirBD.pack(side='top', padx=self.btnPadx, pady=self.btnPady)

        self.btnExcluirBD = tk.Button(self.FrmBotoes, width=self.btnWidth, background='grey', text='Excluir', command=self.objFrmTrvwPreferencias.ExcluirBD)
        self.btnExcluirBD.pack(side='top', padx=self.btnPadx, pady=self.btnPady)

        self.btnAlterarBD = tk.Button(self.FrmBotoes, width=self.btnWidth, background='grey', text='Alterar', command=self.objFrmTrvwPreferencias.AlterarBD)
        self.btnAlterarBD.pack(side='top', padx=self.btnPadx, pady=self.btnPady)


class FrmTrvwPreferencias(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.cols = ["ID", "Descricao"]
        self.colsSize = [100, 100]
        self.colsAnchor = [tk.CENTER, tk.W]

        self.treeview = ttk.Treeview(self, columns=self.cols, height=6, show='headings')
        self.treeview.pack(side='left')

        for i in range(len(self.cols)):
            self.treeview.heading(self.cols[i], text=self.cols[i])
            self.treeview.column(self.cols[i], width=self.colsSize[i], anchor=self.colsAnchor[i])

        linhas = self.ConsultarBD()

        self.treeview.delete(*self.treeview.get_children())

        for linhaBD in linhas:
            self.treeview.insert('','end', values=list(linhaBD))

        estiloDtgdvw = ttk.Style()
        estiloDtgdvw.theme_use('clam')
        estiloDtgdvw.configure("Treeview.Heading", font="Robolt 10 bold", background="white", foreground="blue")
        estiloDtgdvw.configure("Treeview", font="Robolt 10 bold", background="white", foreground="blue")

        barraDeRolagem = Scrollbar(master, orient="vertical", command=self.treeview.yview)
        barraDeRolagem.place(x=474, y=427, width=20, height=155)

        self.treeview.configure(yscrollcommand=barraDeRolagem.set)


    def ConsultBD(self):
        try:
            objFrmConsPreferencia = FrmConsPreferencia(self)

        except Exception as ex:
            messagebox.showinfo(title='Erro', message=str(ex))

    def ConsultarBD(self, parPreferenciaDescricao = None):
        try:
            connectionString = (
                r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                r'DBQ=C:\CURSO PROGRAMAR\Python\Preferencias_1_05072023.accdb;'
            )

            objConexao = pyodbc.connect(connectionString)
            objLeitorBD = objConexao.cursor()

            if parPreferenciaDescricao == None or parPreferenciaDescricao == "":
                strSql = "SELECT ID, Descricao FROM Preferencias_3;"
                objLeitorBD.execute(strSql)
            else:
                strSql = "SELECT ID, Descricao FROM Preferencias_3 WHERE Descricao = ?;"
                objLeitorBD.execute(strSql, parPreferenciaDescricao)

            records = objLeitorBD.fetchall()

            objConexao.close()

            return records

        except Exception as ex:
            messagebox.showinfo(title='Erro', message=str(ex))


    def InserirBD(self):
        try:
            objFrmAddPreferencia = FrmAddPreferencia(self)

        except Exception as ex:
            messagebox.showinfo(title='Erro', message=str(ex))


    def ExcluirBD(self):
        try:
            objFrmDelPreferencia = FrmDelPreferencia(self)

        except Exception as ex:
            messagebox.showinfo(title='Erro', message=str(ex))


    def AlterarBD(self):
        try:
            objFrmAltPreferencia = FrmAltPreferencia(self)

        except Exception as ex:
            messagebox.showinfo(title='Erro', message=str(ex))


    def Refresh(self, records = None):
        for i in range(len(self.cols)):
            self.treeview.heading(self.cols[i])
            self.treeview.column(self.cols[i],
                                width=self.colsSize[i],
                                anchor=self.colsAnchor[i])
        if records == None:
            linhas = self.ConsultarBD()
        else:
            linhas = records

        self.treeview.delete(*self.treeview.get_children())

        for linhaBD in linhas:
            self.treeview.insert('', 'end', values=list(linhaBD))

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
            return self.varType(valor)
        except (ValueError, TypeError):
            return None

    def set(self, valor):
        self.txtDescricao.delete(0, tk.END)
        self.txtDescricao.insert(0, valor)

class FrmConsPreferencia(tk.Tk):
    def __init__(self, objFrmTrvwPreferencias, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.objFrmTrvwPreferencias = objFrmTrvwPreferencias

        self.title('Consultar Preferencia')

        self.txtDescricao = BuilderEntry(self, 'Descricao')
        self.txtDescricao.pack(side='top', padx=5, pady=5)

        self.btnConsultar = tk.Button(self, text='Consultar', command=self.ConsultarPreferencia)
        self.btnConsultar.pack(side='top', padx=5, pady=5)

    def ConsultarPreferencia(self):
        descricao = self.txtDescricao.get()

        if messagebox.askokcancel('Consulta de Preferência', f'Confirma consulta de Preferencia {descricao}?'):
            try:
                self.objFrmTrvwPreferencias.Refresh(self.objFrmTrvwPreferencias.ConsultarBD(descricao))

            except Exception as ex:
                messagebox.showinfo('Erro', str(ex))

            self.destroy()

class FrmAddPreferencia(tk.Tk):
    def __init__(self, objFrmTrvwPreferencias, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.objFrmTrvwPreferencias = objFrmTrvwPreferencias

        self.title('Adicionar Preferencia')

        self.txtDescricao = BuilderEntry(self, 'Descricao')
        self.txtDescricao.pack(side='top', padx=5, pady=5)

        self.btnSalvar = tk.Button(self, text='Salvar', command=self.AddPreferencia)
        self.btnSalvar.pack(side='top', padx=5, pady=5)

        self.mainloop()


    def AddPreferencia(self):
        if  messagebox.askokcancel('Inclusão de Preferência', f'Confirma inclusão de Preferencia {self.txtDescricao.get()}?') == True:
            try:
                connectionString = (
                    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                    r'DBQ=C:\CURSO PROGRAMAR\Python\Preferencias_1_05072023.accdb;'
                )

                objConexao = pyodbc.connect(connectionString)
                objLeitorBD = objConexao.cursor()

                strSql = "INSERT INTO Preferencias_3 (Descricao) VALUES (?);"

                objLeitorBD.execute(strSql, (self.txtDescricao.get()))

                objLeitorBD.commit()

            except Exception as ex:
                self.destroy()
                messagebox.showinfo('Erro', 'Você deve colocar uma descricao antes de adicioná-la')

            else:
                messagebox.showinfo('Sucesso', 'Adicionado com sucesso')
                self.objFrmTrvwPreferencias.Refresh()

            finally:
                objConexao.close()

        self.destroy()

class FrmDelPreferencia(tk.Tk):
    def __init__(self, objFrmTrvwPreferencias, *args, **kwargs):
        super().__init__(*args, **kwargs)

        try:
            self.objFrmTrvwPreferencias = objFrmTrvwPreferencias
            self.title('Excluir Preferencia')

            self.indiceLinhaSelecionada = self.objFrmTrvwPreferencias.treeview.focus()
            self.itemDaLinhaSelecionada = self.objFrmTrvwPreferencias.treeview.item(self.indiceLinhaSelecionada)
            self.idItemDaLinhaSelecionada = self.itemDaLinhaSelecionada["values"][0]
            self.descricaoItemDaLinhaSelecionada = self.itemDaLinhaSelecionada["values"][1]

            self.lblDescricao = BuilderLable(self, self.descricaoItemDaLinhaSelecionada)
            self.lblDescricao.pack(side='top', padx=5, pady=5)

            self.btnExcluir = tk.Button(self, text='Excluir', command=self.DelPreferencia)
            self.btnExcluir.pack(side='top', padx=5, pady=5)

            self.mainloop()
        except Exception as ex:
            self.destroy()
            messagebox.showinfo('Erro', 'Selecione uma linha para Excluí-la')

    def DelPreferencia(self):
        if messagebox.askokcancel('Exclusão de Preferência',f'Confirma exclusão de Preferencia {self.lblDescricao.get()}?') == True:
            try:
                connectionString = (
                    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                    r'DBQ=C:\CURSO PROGRAMAR\Python\Preferencias_1_05072023.accdb;'
                )

                objConexao = pyodbc.connect(connectionString)
                objLeitorBD = objConexao.cursor()

                strSql = "DELETE FROM Preferencias_3 WHERE ID = (?);"

                objLeitorBD.execute(strSql, (self.idItemDaLinhaSelecionada))

                objLeitorBD.commit()

            except Exception as ex:
                messagebox.showinfo('Erro', str(ex))

            else:
                messagebox.showinfo('Sucesso', 'Excluído com sucesso')
                self.objFrmTrvwPreferencias.Refresh()

            finally:
                objConexao.close()
                self.destroy()

class FrmAltPreferencia(tk.Tk):
    def __init__(self, objFrmTrvwPreferencias, *args, **kwargs):
        super().__init__(*args, **kwargs)

        try:
            self.objFrmTrvwPreferencias = objFrmTrvwPreferencias

            self.title('Alterar Preferencia')

            self.indiceLinhaSelecionada = self.objFrmTrvwPreferencias.treeview.focus()
            self.itemDaLinhaSelecionada = self.objFrmTrvwPreferencias.treeview.item(self.indiceLinhaSelecionada)
            self.idItemDaLinhaSelecionada = self.itemDaLinhaSelecionada["values"][0]
            self.descricaoItemDaLinhaSelecionada = self.itemDaLinhaSelecionada["values"][1]

            self.lblDescricao = BuilderLable(self, self.descricaoItemDaLinhaSelecionada)
            self.lblDescricao.pack(side='top', padx=5, pady=5)

            self.txtDescricao = BuilderEntry(self, 'Descricao')
            self.txtDescricao.pack(side='top', padx=5, pady=5)

            self.btnAlterar = tk.Button(self, text='Alterar', command=self.AltPreferencia)
            self.btnAlterar.pack(side='top', padx=5, pady=5)

            self.mainloop()
        except Exception as ex:
            self.destroy()
            messagebox.showinfo('Erro', 'Selecione uma linha para Alterá-la')

    def AltPreferencia(self):
        if messagebox.askokcancel('Alteração de Preferência',f'Confirma alteração de Preferencia {self.lblDescricao.get()} pela Preferência {self.txtDescricao.get()}?') == True:
            try:
                connectionString = (
                    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                    r'DBQ=C:\CURSO PROGRAMAR\Python\Preferencias_1_05072023.accdb;'
                )

                objConexao = pyodbc.connect(connectionString)
                objLeitorBD = objConexao.cursor()

                strSql = "UPDATE Preferencias_3 SET Descricao = (?) WHERE ID = (?);"

                objLeitorBD.execute(strSql, (self.txtDescricao.get(), self.idItemDaLinhaSelecionada))

                objLeitorBD.commit()

            except Exception as ex:
                self.destroy()
                messagebox.showinfo('Erro', 'Você deve colocar uma descricao antes de alterá-la')

            else:
                messagebox.showinfo('Sucesso', 'Alterado com sucesso')
                self.objFrmTrvwPreferencias.Refresh()

            finally:
                objConexao.close()

        self.destroy()

class BuilderLable(tk.Frame):
    def __init__(self, master, labelText, varType=str, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.lableVar = tk.StringVar()
        self.varType = varType
        self.lableText = labelText

        self.lblDescricao = tk.Label(self, text=self.lableText, anchor='w')
        self.lblDescricao.pack(side='top', fill='x')

    def get(self):
        valor = self.lableText
        try:
            return (self.varType(valor))
        except (ValueError, TypeError):
            return None

    def set(self, valor):
        self.lblDescricao.delete(0, tk.END)
        self.lblDescricao.insert(0, valor)
