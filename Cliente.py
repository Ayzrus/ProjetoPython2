class Cliente:

    def __init__(self, nif, nome, morada, email, telefone):
        self.Nif = nif
        self.Nome = nome
        self.Morada = morada
        self.Email = email
        self.Telefone = telefone

    def returnNif(self):
        return self.Nif

    def returnNome(self):
        return self.Nome

    def returnMorada(self):
        return self.Morada

    def returnEmail(self):
        return self.Email

    def returnTelefone(self):
        return self.Telefone

    def setNif(self, nif):
        self.Nif = nif

    def setNome(self, nome):
        self.Nome = nome

    def setMorada(self, morada):
        self.Morada = morada

    def setEmail(self, email):
        self.Email = email

    def setTelefone(self, telefone):
        self.Telefone = telefone
