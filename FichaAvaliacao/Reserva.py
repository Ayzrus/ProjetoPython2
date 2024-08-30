class Reservas:
    # Construtor
    def __init__(self, Id, NifCliente, IdQuarto, Preco, NumNoites):
        self.Id = Id
        self.NifCliente = NifCliente
        self.IdQuarto = IdQuarto
        self.Preco = Preco
        self.NumNoites = NumNoites

    # Métodos

    def get_Id(self):
        return self.Id

    def get_NifCliente(self):
        return self.NifCliente

    def get_IdQuarto(self):
        return self.IdQuarto

    def get_Preco(self):
        return self.Preco

    def get_NumNoites(self):
        return self.NumNoites

    def set_Id(self, Id):
        self.Id = Id

    def set_NifCliente(self, NifCliente):
        self.NifCliente = NifCliente

    def set_IdQuarto(self, IdQuarto):
        self.IdQuarto = IdQuarto

    def set_Preco(self, Preco):
        self.Preco = Preco

    def set_NumNoites(self, NumNoites):
        self.NumNoites = NumNoites

    def calcularValor(self):
        return float(self.Preco) * int(self.NumNoites)

    def imprimeTalao(self):
        return f"###############################" \
               f"HOTEL XPTO \n" \
               f"NIF CLIENTE: <<{self.NifCliente}>>\n" \
               f"Valor a pagar: <<{self.calcularValor()}>> EUR\n" \
               f"geral@hotelxpto.pt | www.hotelxpto.pt\n" \
               f"###############################"
