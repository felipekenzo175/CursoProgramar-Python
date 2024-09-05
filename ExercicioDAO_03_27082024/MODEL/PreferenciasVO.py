class PreferenciasVO:

    def __init__(self, iD=None, descricao=None):
        if iD is not None:
            if iD != int(iD):
                raise Exception('ID inválido')

        if descricao is not None:
            if descricao != str(descricao):
                raise Exception('Descricao inválida')

        self._id = iD
        self._descricao = descricao

    def getId(self):
        return self._id

    def setId(self, iD):
        self._id = iD

    def getDescricao(self):
        return self._descricao

    def setDescricao(self, descricao):
        self._descricao = descricao

    id = property(getId, setId)

    descricao = property(getDescricao, setDescricao)

    # PreferenciasVOCollection = [PreferenciasVO()]

