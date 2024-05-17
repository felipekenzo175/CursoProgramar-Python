import pyodbc
import pandas as pdPreferencias
from io import StringIO
from abc import abstractmethod #abc é a classe abstrata do python

class Conexao:
    _conexao = None
    _pathBD = None

    def __init__(self):
        Conexao.getConexao()

    @staticmethod
    def getConexao():
        if Conexao._conexao is None:
            Conexao.setConexao()

        return Conexao._conexao

    @staticmethod
    def setConexao():
        with (open(".\\config.ini", "r") as arquivoIni):
            connectionString = StringIO()
            connectionString.write(arquivoIni.readline())
            connectionString.write(arquivoIni.readline())
            connectionString = connectionString.getvalue()

        lstConexao = connectionString.split('\n')
        tplConexao = (fr'{lstConexao[0]}' +
                        fr'{lstConexao[1]}')
        objConexao = pyodbc.connect(tplConexao)
        Conexao._conexao = objConexao

    @staticmethod
    def fecharConexao():
        if Conexao._conexao is not None:
            #usando o exec para escrever o código usando string.
            #pyodbc.Connection(Conexao._conexao).close()
            exec("Conexao._conexao.close()",globals(),{})
            #linha de código criada para testar se a conexão fechou
            #exec("Conexao._conexao.cursor().execute('SELECT Descricao FROM Preferencias_3')", globals(), {})
            Conexao._conexao = None

    @property
    def conexao(self):
        return Conexao.getConexao()

