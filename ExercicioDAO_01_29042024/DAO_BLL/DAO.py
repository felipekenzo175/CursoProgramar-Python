import pyodbc   # importa a biblioteca pyodbc
import pandas as pdPreferencias     # importa a biblioteca pandas com o nome de pdPreferencias
from io import StringIO
from DAO_BLL.DBDAL import Conexao

class PreferenciasDAO(Conexao):
    def __init__(self):
        super().__init__()
    def banco_conectado(self):
        try:
            lista = []

            objConexao = self.conexao
            objLeitorBD = objConexao.cursor()

            strSql = StringIO()
            strSql.write("SELECT")
            strSql.write(" Descricao")
            strSql.write(" FROM")
            strSql.write(" Preferencias_3")
            strSql.write(" ORDER BY ID")

            objLeitorBD.execute(strSql.getvalue())

            record = objLeitorBD.fetchone()

            while record != None:
                lista.append(record.Descricao)
                record = objLeitorBD.fetchone()

            objLeitorBD.close()

            return lista
        except Exception as ex:
            return ex

        finally:
            self.fecharConexao()

    def banco_desconectado(self):
        try:
            lista = []

            objConexao = self.conexao
            objLeitorBD = objConexao.cursor()

            strSql = StringIO()
            strSql.write("SELECT")
            strSql.write(" Descricao")
            strSql.write(" FROM")
            strSql.write(" Preferencias_3")
            strSql.write(" ORDER BY ID")

            objLeitorBD.execute(strSql.getvalue())

            records = objLeitorBD.fetchall()

            dfPreferencias = pdPreferencias.DataFrame(records, columns=['Descricao'])

            self.fecharConexao()

            for item in records:
                lista.append(item.Descricao)

            return lista
        except Exception as ex:
            return ex


    def ConsultarBD(self, parPreferenciaDescricao=None):
        try:
            objConexao = self.conexao
            objLeitorBD = objConexao.cursor()

            strSql = StringIO()
            strSql.write("SELECT")
            strSql.write(" ID,")
            strSql.write(" Descricao")
            strSql.write(" FROM")
            strSql.write(" Preferencias_3")

            if parPreferenciaDescricao == None or parPreferenciaDescricao == "":
                strSql.write(" ORDER BY ID")
                objLeitorBD.execute(strSql.getvalue())
            else:
                strSql.write(" WHERE")
                strSql.write(" Descricao = ?")
                strSql.write(" ORDER BY ID")
                objLeitorBD.execute(strSql.getvalue(), parPreferenciaDescricao)

            records = objLeitorBD.fetchall()

            self.fecharConexao()

            return records
        except Exception as ex:
            return ex


    def InserirBD(self, descricao):
        try:
            objConexao = self.conexao
            objLeitorBD = objConexao.cursor()

            strSql = StringIO()
            strSql.write("INSERT")
            strSql.write(" INTO")
            strSql.write(" Preferencias_3 (")
            strSql.write(" Descricao")
            strSql.write(" ) VALUES (")
            strSql.write(" ?")
            strSql.write(" )")

            objLeitorBD.execute(strSql.getvalue(), descricao)

            objConexao.commit()

            return True
        except Exception as ex:
            return ex

        finally:
            self.fecharConexao()


    def ExcluirBD(self, idItemDaLinhaSelecionada):
        try:
            objConexao = self.conexao
            objLeitorBD = objConexao.cursor()

            strSql = StringIO()
            strSql.write("DELETE")
            strSql.write(" FROM")
            strSql.write(" Preferencias_3")
            strSql.write(" WHERE")
            strSql.write(" ID = ?")

            objLeitorBD.execute(strSql.getvalue(), idItemDaLinhaSelecionada)

            objLeitorBD.commit()

            return True
        except Exception as ex:
            return ex

        finally:
            self.fecharConexao()


    def AlterarBD(self, idItemDaLinhaSelecionada, descricao):
        try:
            objConexao = self.conexao
            objLeitorBD = objConexao.cursor()

            strSql = StringIO()
            strSql.write("UPDATE")
            strSql.write(" Preferencias_3")
            strSql.write(" SET")
            strSql.write(" Descricao = ?")
            strSql.write(" WHERE")
            strSql.write(" ID = ?")

            objLeitorBD.execute(strSql.getvalue(), (descricao, idItemDaLinhaSelecionada))

            objLeitorBD.commit()

            return True
        except Exception as ex:
            return ex

        finally:
            self.fecharConexao()