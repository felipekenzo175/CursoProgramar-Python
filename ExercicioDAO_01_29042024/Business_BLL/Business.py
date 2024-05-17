from DAO_BLL.DAO import PreferenciasDAO     # importa a classe PreferenciasDAO da DAO

class Preferencias:
    resultado = False
    def imp_txt_while(self):
        try:
            lista = []
            objLeitorTxt = open(r"C:\Curso Programar\preferencias.txt")
            strLinhaLida = objLeitorTxt.readline()

            while strLinhaLida != "":
                lista.append(strLinhaLida)
                strLinhaLida = objLeitorTxt.readline()

            return lista
        except Exception as ex:
            return ex

        finally:
            objLeitorTxt.close()


    def imp_txt_for(self):
        try:
            lista = []
            objLeitorTxt = open(r"C:\Curso Programar\preferencias.txt")
            strLinhasLidas = objLeitorTxt.readlines()

            for linha in range(len(strLinhasLidas)):
                lista.append(strLinhasLidas[linha])

            objLeitorTxt.close()

            return lista
        except Exception as ex:
            return ex


    def imp_txt_for_each(self):
        try:
            lista = []
            objLeitorTxt = open(r"C:\Curso Programar\preferencias.txt")
            strLinhasLidas = objLeitorTxt.readlines()

            for linha in strLinhasLidas:
                lista.append(linha)

            objLeitorTxt.close()

            return lista
        except Exception as ex:
            return ex


    def banco_conectado(self):
        try:
            objPreferenciasDAO = PreferenciasDAO()
            return objPreferenciasDAO.banco_conectado()
        except Exception as ex:
            return ex

    def banco_desconectado(self):
        try:
            objPreferenciasDAO = PreferenciasDAO()
            return objPreferenciasDAO.banco_desconectado()
        except Exception as ex:
            return ex

    def ConsultarBD(self, parPreferenciaDescricao=None):
        try:
            objPreferenciasDAO = PreferenciasDAO()
            return objPreferenciasDAO.ConsultarBD(parPreferenciaDescricao)
        except Exception as ex:
            return ex


    def InserirBD(self, descricao):
        try:
            objPreferenciasDAO = PreferenciasDAO()
            return objPreferenciasDAO.InserirBD(descricao)
        except Exception as ex:
            return ex

    def ExcluirBD(self, idItemDaLinhaSelecionada):
        try:
            objPreferenciasDAO = PreferenciasDAO()
            return objPreferenciasDAO.ExcluirBD(idItemDaLinhaSelecionada)
        except Exception as ex:
            return ex

    def AlterarBD(self, idItemDaLinhaSelecionada, descricao):
        try:
            objPreferenciasDAO = PreferenciasDAO()
            return objPreferenciasDAO.AlterarBD(idItemDaLinhaSelecionada, descricao)
        except Exception as ex:
            return ex