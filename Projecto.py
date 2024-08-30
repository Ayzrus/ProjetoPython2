class Projetos:

    def __init__(self, cod, Descricao, Tipo, NifCliente):
        self.Cod = cod
        self.Descricao = Descricao
        self.Tipo = Tipo
        self.NifCliente = NifCliente

    def returnCod(self):
        return self.Cod

    def returnDescricao(self):
        return self.Descricao

    def returnTipo(self):
        return self.Tipo

    def returnNifCliente(self):
        return self.NifCliente

    def setCod(self, codigo):
        self.Cod = codigo

    def setDescricao(self, descricao):
        self.Descricao = descricao

    def setTipo(self, tipo):
        self.Tipo = tipo

    def setNifCliente(self, nif):
        self.NifCliente = nif
