import tkinter as tk    # Importar a tkinter com o nome de tk
from tkinter import *   # Importar tudo da biblioteca tkinter
from Business_BLL.preferencias import Preferencias   # Importar a classe Preferencias da Business
from tkinter import messagebox, ttk  # Importar messagebox da biblioteca tkinter
from MODEL.preferenciasVO import PreferenciasVO

# Definir uma nova classe chamada FrmExercicioDAO_01_29042024 que herda tk.Frame, ou seja, vai ser um frame da Tkinter.
class FrmExercicioSegundaTabela_01_05092024(tk.Frame):
    # Criar o método inicializador da classe, com master(widget pai), *args e **kwargs(flexível ao tk.Frame(parâmetros))
    def __init__(self, master, *args, **kwargs):
        # Chamar o método inicializador da classe base tk.Frame para garantir que ele seja inicializado corretamente.
        super().__init__(master, *args, **kwargs)

        # Definir o título da janela principal para Exercício DAO 01 - 29/04/2024
        master.title('Projeto Segunda Tabela Python')

        # Criar uma instância de FrmLstBxPreferencias, passando o self como widget pai.
        objFrmLstBxPreferencias = FrmLstBxPreferencias(self)
        # Posicionar o frame objFrmLstBxPreferencias na linha 0, coluna 1, margem 5px hor., 20px ver. e preencher tudo.
        objFrmLstBxPreferencias.grid(row=0, column=1, padx=5, pady=20, sticky='NSEW')

        # Criar uma instância de FrmBtnPreferencias
        objFrmBtnPreferencias = FrmBtnPreferencias(self, objFrmLstBxPreferencias, Preferencias)
        # Posicionar o frame objFrmBtnPreferencias na linha 0, coluna 0, margem 40px hor., 20px ver. e preencher tudo.
        objFrmBtnPreferencias.grid(row=0, column=0, padx=40, pady=20, sticky='NSEW')

        # Criar uma instância de FrmTrvwPreferencias
        objFrmTrvwPreferencias = FrmTrvwPreferencias(self, Preferencias, PreferenciasVO)
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


class BindingNavigator(tk.Frame):
    def __init__(self, master, treeview, frm_trvw_preferencias, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.treeview = treeview
        self.frm_trvw_preferencias = frm_trvw_preferencias

        self.btn_first = tk.Button(self, text="<<", command=self.first_record)
        self.btn_first.pack(side='left')

        self.btn_prev = tk.Button(self, text="<", command=self.prev_record)
        self.btn_prev.pack(side='left')

        self.btn_next = tk.Button(self, text=">", command=self.next_record)
        self.btn_next.pack(side='left')

        self.btn_last = tk.Button(self, text=">>", command=self.last_record)
        self.btn_last.pack(side='left')

        self.btn_insert = tk.Button(self, text="Inserir", command=self.insert_record)
        self.btn_insert.pack(side='left')

        self.btn_excluir = tk.Button(self, text="Excluir", command=self.excluir_record)
        self.btn_excluir.pack(side='left')

        self.btn_alterar = tk.Button(self, text="Alterar", command=self.alterar_record)
        self.btn_alterar.pack(side='left')

        self.current_index = 0
        self.update_index()

    def update_index(self):
        total_items = len(self.treeview.get_children())
        if total_items == 0:
            self.current_index = -1
        elif self.current_index >= total_items:
            self.current_index = total_items - 1
        elif self.current_index < 0:
            self.current_index = 0
        self.select_record()

    def select_record(self):
        children = self.treeview.get_children()
        if children:
            self.treeview.selection_set(children[self.current_index])
            self.treeview.see(children[self.current_index])

    def first_record(self):
        self.current_index = 0
        self.update_index()

    def prev_record(self):
        self.current_index -= 1
        self.update_index()

    def next_record(self):
        self.current_index += 1
        self.update_index()

    def last_record(self):
        self.current_index = len(self.treeview.get_children()) - 1
        self.update_index()

    def insert_record(self):
        try:
            self.frm_trvw_preferencias.InserirBD()
        except Exception as ex:
            messagebox.showinfo('Erro', str(ex))

    def excluir_record(self):
        try:
            self.frm_trvw_preferencias.ExcluirBD()
        except Exception as ex:
            messagebox.showinfo('Erro', str(ex))

    def alterar_record(self):
        try:
            self.frm_trvw_preferencias.AlterarBD()
        except Exception as ex:
            messagebox.showinfo('Erro', str(ex))
class FrmTrvwPreferencias(tk.Frame):
    def __init__(self, master, Preferencias, PreferenciasVO, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.preferencias = Preferencias()
        objPreferenciasVO = PreferenciasVO()
        self.cols = ["ID", "Descricao"]
        self.colsSize = [100, 100]
        self.colsAnchor = [tk.CENTER, tk.W]

        self.treeview = ttk.Treeview(self, columns=self.cols, height=6, show='headings')
        self.treeview.grid(row=1, column=0, columnspan=2, sticky='NSEW')

        for i in range(len(self.cols)):
            self.treeview.heading(self.cols[i], text=self.cols[i])
            self.treeview.column(self.cols[i], width=self.colsSize[i], anchor=self.colsAnchor[i])

        self.binding_navigator = BindingNavigator(self, self.treeview, self)
        self.binding_navigator.grid(row=0, column=0, columnspan=2, sticky='EW')

        linhas = self.ConsultarBD(objPreferenciasVO)

        self.treeview.delete(*self.treeview.get_children())

        for linhaBD in linhas:
            values = [linhaBD.ID, linhaBD.Descricao]
            self.treeview.insert('', 'end', values=values)

        estiloDtgdvw = ttk.Style()
        estiloDtgdvw.theme_use('clam')
        estiloDtgdvw.configure("Treeview.Heading", font="Roboto 10 bold", background="#084d6e", foreground="white")
        estiloDtgdvw.configure("Treeview", font="Roboto 10 bold", background="white", foreground="black")

        barraDeRolagem = tk.Scrollbar(self, orient="vertical", command=self.treeview.yview)
        barraDeRolagem.grid(row=1, column=2, sticky='NS')

        self.treeview.configure(yscrollcommand=barraDeRolagem.set)

    def ConsultBD(self):
        try:
            objFrmConsPreferencia = FrmConsPreferencia(self)
        except Exception as ex:
            messagebox.showinfo('Erro', str(ex))

    def ConsultarBD(self, objPreferenciasVO):
        try:
            return Preferencias.ConsultarBD(self, objPreferenciasVO)
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

        objPreferenciasVO = PreferenciasVO()
        for i in range(len(self.cols)):
            self.treeview.heading(self.cols[i])
            self.treeview.column(self.cols[i], width=self.colsSize[i], anchor=self.colsAnchor[i])

        if records is None:
            linhas = self.ConsultarBD(objPreferenciasVO)
        else:
            linhas = records

        self.treeview.delete(*self.treeview.get_children())

        for linhaBD in linhas:
            self.treeview.insert('', 'end', values=list(linhaBD))

        # Atualizar o índice da barra de navegação
        self.binding_navigator.update_index()


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
                # Criar uma instância de PreferenciasVO e definir a descrição usando o setter
                objPreferenciasVO = PreferenciasVO(descricao=descricao)

                # Chamar o método ConsultarBD passando a instância de PreferenciasVO
                resultados = self.objFrmTrvwPreferencias.ConsultarBD(objPreferenciasVO)

                # Atualizar a interface com os resultados
                self.objFrmTrvwPreferencias.Refresh(resultados)

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
        descricao = self.txtDescricao.get()

        if messagebox.askokcancel('Inclusão de Preferência', f'Confirma inclusão de Preferência {descricao}?'):
            try:
                # Criar uma instância de PreferenciasVO e definir a descrição usando o setter
                objPreferenciasVO = PreferenciasVO(descricao=descricao)

                # Inserir a preferência no banco de dados utilizando a descrição do objeto PreferenciasVO
                preferencias = Preferencias()
                if preferencias.InserirBD(objPreferenciasVO):
                    messagebox.showinfo('Sucesso', 'Adicionado com Sucesso')
                    self.objFrmTrvwPreferencias.Refresh()
                else:
                    messagebox.showinfo('Erro', 'Erro ao adicionar a preferência')
            except Exception as ex:
                messagebox.showinfo('Erro', str(ex))
            finally:
                self.destroy()
        else:
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
        id = self.idItemDaLinhaSelecionada
        if messagebox.askokcancel('Exclusão de Preferência', f'Confirma exclusão de Preferência {self.lblDescricao.get()}?') == True:
            try:
                preferencias = Preferencias()
                objPreferenciasVO = PreferenciasVO(iD=id)
                if preferencias.ExcluirBD(objPreferenciasVO):
                    messagebox.showinfo('Sucesso', 'Excluído com Sucesso')
                    self.objFrmTrvwPreferencias.Refresh()
                else:
                    messagebox.showinfo('Erro', 'Erro ao excluir a preferência')
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
        id = self.idItemDaLinhaSelecionada
        if messagebox.askokcancel('Alteração de Preferência', f'Confirma alteração de Preferência {self.lblDescricao.get()} pela Preferência {self.txtDescricao.get()}?') == True:
            try:
                preferencias = Preferencias()
                nova_descricao = self.txtDescricao.get()

                # Atualizar a descrição na instância de PreferenciasVO
                objPreferenciasVO = PreferenciasVO(iD=id, descricao=nova_descricao)

                if preferencias.AlterarBD(objPreferenciasVO):
                    messagebox.showinfo('Sucesso', 'Alterado com Sucesso')
                    self.objFrmTrvwPreferencias.Refresh()
                else:
                    messagebox.showinfo('Erro', 'Erro ao alterar a preferência')

            except Exception as ex:
                messagebox.showinfo('Erro', str(ex))

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