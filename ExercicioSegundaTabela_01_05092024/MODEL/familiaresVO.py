from datetime import datetime


class FamiliaresVO:

    def __init__(self, COD=None, Nome=None, Sexo=None, Idade=None, Data_Nascimento=None, Ganho_Mensal=None, Gasto_Mensal=None, Observacao=None):
        if COD is not None:
            if COD != int(COD):
                raise Exception('COD inválido')

        if Nome is not None:
            if Nome != str(Nome):
                raise Exception('Nome inválido')

        if Sexo is not None:
            if Sexo != str(Sexo):
                raise Exception('Sexo inválido')

        if Idade is not None:
            if Idade != int(Idade):
                raise Exception('Idade inválida')

        if Data_Nascimento is not None:
            if Data_Nascimento != datetime(Data_Nascimento):
                raise Exception('Data de Nascimento inválido')

        if Ganho_Mensal is not None:
            if Ganho_Mensal != float(Ganho_Mensal):
                raise Exception('Ganho Mensal inválido')

        if Gasto_Mensal is not None:
            if Gasto_Mensal != float(Gasto_Mensal):
                raise Exception('Gasto Mensal inválido')

        if Observacao is not None:
            if Observacao != str(Observacao):
                raise Exception('Observacao inválida')

        self._cod = COD
        self._nome = Nome
        self._sexo = Sexo
        self._idade = Idade
        self._dataNascimento = Data_Nascimento
        self._ganhoMensal = Ganho_Mensal
        self._gastoMensal = Gasto_Mensal
        self._observacao = Observacao

    def getCod(self):
        return self._cod

    def setCod(self, COD):
        self._cod = COD

    def getNome(self):
        return self._nome

    def setNome(self, Nome):
        self._nome = Nome

    def getSexo(self):
        return self._sexo

    def setSexo(self, Sexo):
        self._sexo = Sexo

    def getIdade(self):
        return self._idade

    def setIdade(self, Idade):
        self._idade = Idade

    def getDataNascimento(self):
        return self._dataNascimento

    def setDataNascimento(self, Data_Nascimento):
        self._dataNascimento = Data_Nascimento

    def getGanhoMensal(self):
        return self._ganhoMensal

    def setGanhoMensal(self, Ganho_Mensal):
        self._ganhoMensal = Ganho_Mensal

    def getGastoMensal(self):
        return self._gastoMensal

    def setGastoMensal(self, Gasto_Mensal):
        self._gastoMensal = Gasto_Mensal

    def getObservacao(self):
        return self._observacao

    def setObservacao(self, Observacao):
        self._observacao = Observacao

    COD = property(getCod, setCod)

    Nome = property(getNome, setNome)

    Sexo = property(getSexo, setSexo)

    Idade = property(getIdade, setIdade)

    Data_Nascimento = property(getDataNascimento, setDataNascimento)

    Ganho_Mensal = property(getGanhoMensal, setGanhoMensal)

    Gasto_Mensal = property(getGastoMensal, setGastoMensal)

    Observacao = property(getObservacao, setObservacao)

    # PreferenciasVOCollection = [PreferenciasVO()]

