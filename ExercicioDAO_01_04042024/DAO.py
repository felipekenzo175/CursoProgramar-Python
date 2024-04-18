import pyodbc
import pandas as pdPreferencias

class PreferenciasDAO():
    def banco_conectado(self):
        try:
            lista = []

            connectionString = (
                r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                r'DBQ=C:\CURSO PROGRAMAR\Python\Preferencias_1_05072023.accdb;'
            )

            objConexao = pyodbc.connect(connectionString)
            objLeitorBD = objConexao.cursor()

            strSql = "SELECT"
            strSql += " Descricao"
            strSql += " FROM"
            strSql += " Preferencias_3"
            strSql += " ORDER BY ID;"

            objLeitorBD.execute(strSql)

            record = objLeitorBD.fetchone()

            while record != None:
                lista.append(record.Descricao)
                record = objLeitorBD.fetchone()

            objLeitorBD.close()

            return lista
        except Exception as ex:
            return ex

        finally:
            objConexao.close()

    def banco_desconectado(self):
        try:
            lista = []

            connectionString = (
                r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                r'DBQ=C:\CURSO PROGRAMAR\Python\Preferencias_1_05072023.accdb;'
            )

            objConexao = pyodbc.connect(connectionString)
            objLeitorBD = objConexao.cursor()

            strSql = "SELECT"
            strSql += " Descricao"
            strSql += " FROM"
            strSql += " Preferencias_3"
            strSql += " ORDER BY ID;"

            objLeitorBD.execute(strSql)

            records = objLeitorBD.fetchall()

            dfPreferencias = pdPreferencias.DataFrame(records, columns=['Descricao'])

            objConexao.close()

            for item in records:
                lista.append(item.Descricao)

            return lista
        except Exception as ex:
            return ex


    def ConsultarBD(self, parPreferenciaDescricao=None):
        try:
            connectionString = (
                r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                r'DBQ=C:\CURSO PROGRAMAR\Python\Preferencias_1_05072023.accdb;'
            )

            objConexao = pyodbc.connect(connectionString)
            objLeitorBD = objConexao.cursor()
            strSql = "SELECT"
            strSql += " ID,"
            strSql += " Descricao"
            strSql += " FROM"
            strSql += " Preferencias_3"

            if parPreferenciaDescricao == None or parPreferenciaDescricao == "":
                strSql += " ORDER BY ID;"
                objLeitorBD.execute(strSql)
            else:
                strSql += " WHERE"
                strSql += " Descricao = ?"
                strSql += " ORDER BY ID;"
                objLeitorBD.execute(strSql, parPreferenciaDescricao)

            records = objLeitorBD.fetchall()

            objConexao.close()

            return records
        except Exception as ex:
            return ex


    def InserirBD(self, descricao):
        try:
            connectionString = (
                r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                r'DBQ=C:\CURSO PROGRAMAR\Python\Preferencias_1_05072023.accdb;'
            )

            objConexao = pyodbc.connect(connectionString)
            objLeitorBD = objConexao.cursor()

            strSql = "INSERT"
            strSql += " INTO"
            strSql += " Preferencias_3 ("
            strSql += " Descricao"
            strSql += " ) VALUES ("
            strSql += " ?"
            strSql += " );"

            objLeitorBD.execute(strSql, descricao)

            objConexao.commit()

            return True
        except Exception as ex:
            return ex

        finally:
            objConexao.close()


    def ExcluirBD(self, idItemDaLinhaSelecionada):
        try:
            connectionString = (
                r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                r'DBQ=C:\CURSO PROGRAMAR\Python\Preferencias_1_05072023.accdb;'
            )

            objConexao = pyodbc.connect(connectionString)
            objLeitorBD = objConexao.cursor()

            strSql = "DELETE"
            strSql += " FROM"
            strSql += " Preferencias_3"
            strSql += " WHERE"
            strSql += " ID = ?;"

            objLeitorBD.execute(strSql, idItemDaLinhaSelecionada)

            objLeitorBD.commit()

            return True
        except Exception as ex:
            return ex

        finally:
            objConexao.close()


    def AlterarBD(self, idItemDaLinhaSelecionada, descricao):
        try:
            connectionString = (
                r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                r'DBQ=C:\CURSO PROGRAMAR\Python\Preferencias_1_05072023.accdb;'
            )

            objConexao = pyodbc.connect(connectionString)
            objLeitorBD = objConexao.cursor()
            strSql = "UPDATE"
            strSql += " Preferencias_3"
            strSql += " SET"
            strSql += " Descricao = ?"
            strSql += " WHERE"
            strSql += " ID = ?;"

            objLeitorBD.execute(strSql, (descricao, idItemDaLinhaSelecionada))

            objLeitorBD.commit()

            return True
        except Exception as ex:
            return ex

        finally:
            objConexao.close()