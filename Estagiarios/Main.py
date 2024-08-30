from Estagiario import Estagiarios
import csv
import os.path

op = 1

estagiario = []

pasta = os.path.isdir('Ficheiros')

if pasta:
    path = 'Ficheiros/Estagiarios.csv'

    check_file = os.path.isfile(path)

    if check_file:

        def validaEstagiario(neste, val):
            if val != '':
                debounce = True

                with open('Ficheiros/Estagiarios.csv', 'r') as file2:
                    reader3 = csv.reader(file2)
                    for row3 in reader3:
                        if row3[0] == str(neste):
                            debounce = False

                return debounce
            else:
                debounce = False

                with open('Ficheiros/Estagiarios.csv', 'r') as file2:
                    reader2 = csv.reader(file2)
                    for row2 in reader2:
                        if row2[0] == str(neste):
                            debounce = False

                return debounce


        while op != 0:
            op = str(input('Insira 1 para abertura de Novo estagiario: \n'
                           'Insira 2 para ver informações: \nInsira 0 para '
                           'sair: \n'))

            if op == '1':
                nest = int(input('Insira o Numero Do Estagiario: \n'))
                est = Estagiarios(nest,
                                  str(input('Insira o Nome Do Estagiario: \n')),
                                  str(input('Insira as habilitações literárias(Ex: 9, 6, 12): \n')),
                                  str(input('Insira a Bolsa de Estagio(Euros): \n')),
                                  str(input('Insira o número de meses do estágio: \n')),
                                  str(input('Insira o Data De Entrada do estágiario (Ex: 18-04-2023): \n')),
                                  )
                if validaEstagiario(nest, 'val'):
                    with open('Ficheiros/Estagiarios.csv', 'a+', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow([est.getNfuncionario(), est.getNome(), est.getHl(), est.getBa(), est.getNm(),
                                         est.getDataEntrada(), est.verInfo()])
                else:
                    print('Já existe um estagiario com o numero: ' + str(nest) + ' registrado!')
            elif op == '2':
                with open('Ficheiros/Estagiarios.csv', 'r') as file:
                    reader = csv.reader(file)
                    for row in reader:
                        if row[6] == ' verInfo':
                            nada = False
                        else:
                            print(row[6])
            elif op == '0':
                break
            else:
                print('Insira uma opção valida do menu!')
    else:
        new = open("Ficheiros/Estagiarios.csv", "x")
else:
    os.mkdir('Ficheiros')

