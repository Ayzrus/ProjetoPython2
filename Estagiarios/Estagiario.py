from datetime import date
from dateutil.relativedelta import relativedelta

# para isto funcionar precisa instalar pip install python-dateutil


def getDataFinal(dataentrada, temp):

    datafinal = str(dataentrada).split('-')

    data_entrada = date(int(datafinal[2]), int(datafinal[1]), int(datafinal[0]))

    meses_estagio = int(temp)

    data_saida = data_entrada + relativedelta(months=+meses_estagio)

    return data_saida


class Estagiarios:
    # Construtor
    def __init__(self, NFuncionario, Nome, Hl, Ba, Nm, DataEntrada):
        self.NFuncionario = NFuncionario
        self.Nome = Nome
        self.Hl = Hl
        self.Ba = Ba
        self.Nm = Nm
        self.DataEntrada = DataEntrada
        self.DataSaida = getDataFinal(dataentrada=self.getDataEntrada(), temp=self.getNm())

    # Métodos
    def getNfuncionario(self):
        return self.NFuncionario

    def getNome(self):
        return self.Nome

    def getHl(self):
        return self.Hl

    def getBa(self):
        return self.Ba

    def getNm(self):
        return self.Nm

    def getDataEntrada(self):
        return self.DataEntrada

    def getDataSaida(self):
        return self.DataSaida

    def setNfuncionario(self, nfuncionario):
        self.NFuncionario = nfuncionario

    def setNome(self, nome):
        self.Nome = nome

    def setHl(self, hl):
        self.Hl = hl

    def setBa(self, ba):
        self.Ba = ba

    def setNm(self, nm):
        self.NFuncionario = nm

    def setDataEntrada(self, dataEntrada):
        self.DataEntrada = dataEntrada

    def setDia(self, datasaida):
        self.DataSaida = datasaida

    def calculaValorEmpresa(self):
        if self.getHl() == '6' or self.getHl() == '9' or self.getHl() == '12':
            percentagem = 0.45
            resultado = float(self.getBa()) * float(percentagem)
            return resultado
        else:
            percentagem = 0.25
            resultado = float(self.getBa()) * float(percentagem)
            return resultado

    def verInfo(self):
        return f"Estagiario n<<{self.getNfuncionario()}>> | <<nome>>  Entrada: <<{self.getDataEntrada()}" \
               f">> | Saida: " \
               f"<<{self.getDataSaida()}>> " \
               f"Montante total a pagar pela empresa: <<{self.calculaValorEmpresa()}>> EUR"
