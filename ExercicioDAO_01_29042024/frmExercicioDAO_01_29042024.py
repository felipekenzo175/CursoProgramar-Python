import tkinter as tk    # Importar a tkinter com o nome de tk
from tkinter import *   # Importar tudo da biblioteca tkinter
from Business_BLL.Business import Preferencias   # Importar a classe Preferencias da Business
from tkinter import messagebox, ttk  # Importar messagebox da biblioteca tkinter

# Definir uma nova classe chamada FrmExercicioDAO_01_29042024 que herda tk.Frame, ou seja, vai ser um frame da Tkinter.
class FrmExercicioDAO_01_29042024(tk.Frame):
    # Criar o método inicializador da classe, com master(widget pai), *args e **kwargs(flexível ao tk.Frame(parâmetros))
    def __init__(self, master, *args, **kwargs):
        # Chamar o método inicializador da classe base tk.Frame para garantir que ele seja inicializado corretamente.
        super().__init__(master, *args, **kwargs)

        # Definir o título da janela principal para Exercício DAO 01 - 29/04/2024
        master.title('Exercicio DAO 01 - 29/04/2024')

        # Criar uma instância de FrmLstBxPreferencias, passando o self como widget pai.
        objFrmLstBxPreferencias = FrmLstBxPreferencias(self)
        # Posicionar o frame objFrmLstBxPreferencias na linha 0, coluna 1, margem 5px hor., 20px ver. e preencher tudo.
        objFrmLstBxPreferencias.grid(row=0, column=1, padx=5, pady=20, sticky='NSEW')

        # Criar uma instância de FrmBtnPreferencias
        objFrmBtnPreferencias = FrmBtnPreferencias(self, objFrmLstBxPreferencias, Preferencias)
        # Posicionar o frame objFrmBtnPreferencias na linha 0, coluna 0, margem 40px hor., 20px ver. e preencher tudo.
        objFrmBtnPreferencias.grid(row=0, column=0, padx=40, pady=20, sticky='NSEW')

        # Criar uma instância de FrmTrvwPreferencias
        objFrmTrvwPreferencias = FrmTrvwPreferencias(self, Preferencias)
        # Posicionar o frame objFrmBtnPreferencias na linha 1, coluna 1, margem 5px hor., 20px ver. e preencher tudo.
        objFrmTrvwPreferencias.grid(row=1, column=1, padx=5, pady=20, sticky='NSEW')

        # Criar uma instância de FrmBtnTrvwPreferencias
        objFrmBtnTrvwPreferencias = FrmBtnTrvwPreferencias(self, objFrmTrvwPreferencias)
        # Posicionar o frame objFrmBtnPreferencias na linha 1, coluna 0, margem 5px hor., 20px ver. e preencher tudo.
        objFrmBtnTrvwPreferencias.grid(row=1, column=0, padx=5, pady=20, sticky='NSEW')


class FrmLstBxPreferencias(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.LstBxPreferencias = tk.Listbox(self, width=32, height=22)
        self.LstBxPreferencias.pack(fill='both', expand=False, pady=5)

    def limpaLstBxPreferencias(self):
        self.LstBxPreferencias.delete(0, END)


class FrmBtnPreferencias(tk.Frame):
    def __init__(self, master, objFrmLstBxPreferencias, Preferencias, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.Preferencias = Preferencias
        self.objFrmLstBxPreferencias = objFrmLstBxPreferencias

        btnMensagem = Button(self, text="Mensagem", fg="black", bg="grey", width=25, height=1, command=self.mensagem)
        # btnMensagem.place(x=100, y=50)
        btnMensagem.grid(row=0, column=0, pady=5)

        btnDesvioCondicional = Button(self, text="Desvio Condicional", fg="black", bg="grey", width=25, height=1,
                                      command=self.desvio_condicional)
        # btnDesvioCondicional.place(x=100, y=150)
        btnDesvioCondicional.grid(row=1, column=0, pady=5)

        btnDesvioCondicionalEncadeado = Button(self, text="Desvio Condicional Encadeado", fg="black", bg="grey",
                                               width=25, height=1, command=self.desvio_condicional_encadeado)
        # btnDesvioCondicionalEncadeado.place(x=100, y=200)
        btnDesvioCondicionalEncadeado.grid(row=2, column=0, pady=5)

        btnSwitchCase = Button(self, text="Switch Case", fg="black", bg="grey", width=25, height=1,
                               command=self.switch_case)
        # btnSwitchCase.place(x=100, y=250)
        btnSwitchCase.grid(row=3, column=0, pady=5)

        btnImpTxtWhile = Button(self, text="Importar Texto While", fg="black", bg="grey", width=25, height=1,
                                command=self.imp_txt_while)
        # btnImpTxtWhile.place(x=100, y=300)
        btnImpTxtWhile.grid(row=4, column=0, pady=5)

        btnImpTxtFor = Button(self, text="Importar Texto For", fg="black", bg="grey", width=25, height=1,
                              command=self.imp_txt_for)
        # btnImpTxtFor.place(x=100, y=350)
        btnImpTxtFor.grid(row=5, column=0, pady=5)

        btnImpTxtForEach = Button(self, text="Importar Texto For Each", fg="black", bg="grey", width=25, height=1,
                                  command=self.imp_txt_for_each)
        # btnImpTxtForEach.place(x=100, y=400)
        btnImpTxtForEach.grid(row=6, column=0, pady=5)

        btnClear = Button(self, text="Clear", fg="black", bg="grey", width=25, height=1, command=self.clear)
        # btnClear.place(x=100, y=450)
        btnClear.grid(row=7, column=0, pady=5)

        btnBancoConectado = Button(self, text="Banco Conectado", fg="black", bg="grey", width=25, height=1,
                                   command=self.banco_conectado)
        # btnBancoConectado.place(x=100, y=500)
        btnBancoConectado.grid(row=8, column=0, pady=5)

        btnBancoDesconectado = Button(self, text="Banco Desconectado", fg="black", bg="grey", width=25, height=1,
                                      command=self.banco_desconectado)
        # btnBancoDesconectado.place(x=100, y=550)
        btnBancoDesconectado.grid(row=9, column=0, pady=5)

    def mensagem(self):
        messagebox.showinfo("Mensagem", "Olá, Mundo!")

    def desvio_condicional(self):
        if messagebox.askyesno("Desvio Condicional", "Escolha Sim ou Não") == True:
            messagebox.showinfo("Opção", "Você escolheu Sim")
        else:
            messagebox.showinfo("Opção", "Você escolheu Não")

    def desvio_condicional_encadeado(self):
        resultado = messagebox.askyesnocancel("Desvio Condicional Encadeado", "Escolha Sim, Não ou Cancelar")

        if resultado == True:
            messagebox.showinfo("Opção", "Você escolheu Sim")
        elif resultado == False:
            messagebox.showinfo("Opção", "Você escolheu Não")
        else:
            messagebox.showinfo("Opção", "Você escolheu Cancelar")

    def switch_case(self):
        resultado = messagebox.askyesnocancel("Switch Case", "Escolha Sim, Não ou Cancelar")

        match (resultado):
            case True:
                messagebox.showinfo("Opção", "Você escolheu Sim")
            case False:
                messagebox.showinfo("Opção", "Você escolheu Não")
            case None:
                messagebox.showinfo("Opção", "Você escolheu Cancelar")
            case _:
                messagebox.showinfo("Opção", "Opção Inválida")

    def imp_txt_while(self):
        self.objFrmLstBxPreferencias.limpaLstBxPreferencias()
        preferencias = Preferencias()

        for item in preferencias.imp_txt_while():
            self.objFrmLstBxPreferencias.LstBxPreferencias.insert(END, item)

    def imp_txt_for(self):
        self.objFrmLstBxPreferencias.limpaLstBxPreferencias()
        preferencias = Preferencias()
        for item in preferencias.imp_txt_for():
            self.objFrmLstBxPreferencias.LstBxPreferencias.insert(END, item)

    def imp_txt_for_each(self):
        self.objFrmLstBxPreferencias.limpaLstBxPreferencias()
        preferencias = Preferencias()
        for item in preferencias.imp_txt_for_each():
            self.objFrmLstBxPreferencias.LstBxPreferencias.insert(END, item)

    def clear(self):
        self.objFrmLstBxPreferencias.limpaLstBxPreferencias()

    def banco_conectado(self):
        self.objFrmLstBxPreferencias.limpaLstBxPreferencias()
        preferencias = Preferencias()
        for item in preferencias.banco_conectado():
            self.objFrmLstBxPreferencias.LstBxPreferencias.insert(END, item)

    def banco_desconectado(self):
        self.objFrmLstBxPreferencias.limpaLstBxPreferencias()
        preferencias = Preferencias()
        for item in preferencias.banco_desconectado():
            self.objFrmLstBxPreferencias.LstBxPreferencias.insert(END, item)


class FrmBtnTrvwPreferencias(tk.Frame):
    def __init__(self, master, objFrmTrvwPreferencias, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.objFrmTrvwPreferencias = objFrmTrvwPreferencias

        self.btnWidth = 25
        self.btnPady = 5
        self.btnPadx = 35

        self.FrmBotoes = tk.Frame(self)
        self.FrmBotoes.pack(side='left')

        self.btnConsultarBD = tk.Button(self.FrmBotoes, width=self.btnWidth, background='grey', text='Consultar',
                                        command=self.objFrmTrvwPreferencias.ConsultBD)
        self.btnConsultarBD.pack(side='top', padx=self.btnPadx, pady=self.btnPady)

        self.btnInserirBD = tk.Button(self.FrmBotoes, width=self.btnWidth, background='grey', text='Inserir',
                                      command=self.objFrmTrvwPreferencias.InserirBD)
        self.btnInserirBD.pack(side='top', padx=self.btnPadx, pady=self.btnPady)

        self.btnExcluirBD = tk.Button(self.FrmBotoes, width=self.btnWidth, background='grey', text='Excluir',
                                      command=self.objFrmTrvwPreferencias.ExcluirBD)
        self.btnExcluirBD.pack(side='top', padx=self.btnPadx, pady=self.btnPady)

        self.btnAlterarBD = tk.Button(self.FrmBotoes, width=self.btnWidth, background='grey', text='Alterar',
                                      command=self.objFrmTrvwPreferencias.AlterarBD)
        self.btnAlterarBD.pack(side='top', padx=self.btnPadx, pady=self.btnPady)


class FrmTrvwPreferencias(tk.Frame):
    def __init__(self, master, Preferencias, *args, **kwargs):
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
            self.treeview.insert('', 'end', values=list(linhaBD))

        estiloDtgdvw = ttk.Style()
        estiloDtgdvw.theme_use('clam')
        estiloDtgdvw.configure("Treeview.Heading", font="Robolt 10 bold", background="white", foreground="blue")
        estiloDtgdvw.configure("Treeview", font="Roboto 10 bold", background="white", foreground="black")

        barraDeRolagem = Scrollbar(master, orient="vertical", command=self.treeview.yview)
        barraDeRolagem.place(x=474, y=427, width=20, height=155)

        self.treeview.configure(yscrollcommand=barraDeRolagem.set)

    def ConsultBD(self):
        try:
            objFrmConsPreferencia = FrmConsPreferencia(self)

        except Exception as ex:
            messagebox.showinfo('Erro', str(ex))

    def ConsultarBD(self, parPreferenciaDescricao=None):
        try:
            preferencias = Preferencias()
            return preferencias.ConsultarBD(parPreferenciaDescricao)

        except Exception as ex:
            messagebox.showinfo('Erro', str(ex))

    def InserirBD(self):
        try:
            objFrmAddPreferencia = FrmAddPreferencia(self)

        except Exception as ex:
            messagebox.showinfo('Erro', str(ex))

    def ExcluirBD(self):
        try:
            objFrmDelPreferencia = FrmDelPreferencia(self)

        except Exception as ex:
            messagebox.showinfo('Erro', str(ex))

    def AlterarBD(self):
        try:
            objFrmAltPreferencia = FrmAltPreferencia(self)

        except Exception as ex:
            messagebox.showinfo('Erro', str(ex))

    def Refresh(self, records=None):
        for i in range(len(self.cols)):
            self.treeview.heading(self.cols[i])
            self.treeview.column(self.cols[i], width=self.colsSize[i], anchor=self.colsAnchor[i])

        if records == None:
            linhas = self.ConsultarBD()
        else:
            linhas = records

        self.treeview.delete(*self.treeview.get_children())

        for linhaBD in linhas:
            self.treeview.insert('', 'end', values=list(linhaBD))


class BuilderEntry(tk.Frame):
    def __init__(self, master, labelText, varType=str, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.varType = varType

        self.lblDescricao = tk.Label(self, text=labelText, anchor=CENTER, width=40)
        self.lblDescricao.pack(side='top', fill='x')

        self.txtDescricao = tk.Entry(self, textvariable=tk.StringVar(), width=20)
        self.txtDescricao.pack(side='bottom', anchor=CENTER)

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

        if messagebox.askokcancel('Consulta de Preferencia', f'Confirma consulta de Preferencia {descricao}?'):
            try:
                self.objFrmTrvwPreferencias.Refresh(self.objFrmTrvwPreferencias.ConsultarBD(descricao))

            except Exception as ex:
                messagebox.showinfo('Erro', str(ex))

            self.destroy()


class FrmAddPreferencia(tk.Tk):
    def __init__(self, objFrmTrvwPreferencias, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.objFrmTrvwPreferencias = objFrmTrvwPreferencias

        self.title('Inserir Preferencia')

        self.txtDescricao = BuilderEntry(self, 'Descricao')
        self.txtDescricao.pack(side='top', padx=5, pady=5)

        self.btnSalvar = tk.Button(self, text='Salvar', command=self.AddPreferencia)
        self.btnSalvar.pack(side='top', padx=5, pady=5)

        self.mainloop()

    def AddPreferencia(self):
        if messagebox.askokcancel('Inclusão de Preferência',f'Confirma inclusão de Preferência {self.txtDescricao.get()}?') == True:
            try:
                descricao = self.txtDescricao.get()
                preferencias = Preferencias()
                if preferencias.InserirBD(descricao):
                    messagebox.showinfo('Sucesso', 'Adicionado com Sucesso')
                    self.objFrmTrvwPreferencias.Refresh()
            except Exception as ex:
                self.destroy()
                messagebox.showinfo('Erro', 'Você deve inserir uma descricao antes de adicioná-la')

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

            self.lblDescricao = BuilderLabel(self, self.descricaoItemDaLinhaSelecionada)
            self.lblDescricao.pack(side='top', padx=5, pady=5)

            self.btnExcluir = tk.Button(self, text='Excluir', command=self.DelPreferencia)
            self.btnExcluir.pack(side='top', padx=5, pady=5)

            self.mainloop()
        except Exception as ex:
            self.destroy()
            messagebox.showinfo('Erro', 'Selecione uma linha para Excluí-la')

    def DelPreferencia(self):
        if messagebox.askokcancel('Exclusão de Preferência',f'Confirma exclusão de Preferência {self.lblDescricao.get()}?') == True:
            try:
                preferencias = Preferencias()
                idItemDaLinhaSelecionada = self.itemDaLinhaSelecionada["values"][0]
                if preferencias.ExcluirBD(idItemDaLinhaSelecionada):
                    messagebox.showinfo('Sucesso', 'Excluído com Sucesso')
                    self.objFrmTrvwPreferencias.Refresh()

            except Exception as ex:
                messagebox.showinfo('Erro', str(ex))

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

            self.lblDescricao = BuilderLabel(self, self.descricaoItemDaLinhaSelecionada)
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
        if messagebox.askokcancel('Alteração de Preferência', f'Confirma alteração de Preferência {self.lblDescricao.get()} pela Preferência {self.txtDescricao.get()}?') == True:
            try:
                preferencias = Preferencias()
                idItemDaLinhaSelecionada = self.itemDaLinhaSelecionada["values"][0]
                descricao = self.txtDescricao.get()
                if preferencias.AlterarBD(idItemDaLinhaSelecionada, descricao):
                    messagebox.showinfo('Sucesso', 'Alterado com Sucesso')
                    self.objFrmTrvwPreferencias.Refresh()

            except Exception as ex:
                messagebox.showinfo('Erro', 'Você deve inserir uma descrição antes de atualizá-la')

            self.destroy()

class BuilderLabel(tk.Frame):
    def __init__(self, master, labelText, varType=str, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.varType = varType
        self.labelText = labelText

        self.lblDescricao = tk.Label(self, text=self.labelText, anchor=CENTER, width=40)
        self.lblDescricao.pack(side='top', fill='x')

    def get(self):
        valor = self.labelText
        try:
            return self.varType(valor)
        except (ValueError, TypeError):
            return None

    def set(self, valor):
        self.lblDescricao.delete(0, tk.END)
        self.lblDescricao.insert(0, valor)