import csv
import os.path
from Reserva import Reservas

op = 1

reservas = []

pasta = os.path.isdir('Ficheiros')

if pasta:
    path = 'Ficheiros/Taloes.csv'

    check_file = os.path.isfile(path)

    if check_file:

        def validarReserva(idReserva, idReserva2):
            if idReserva2 != '':
                debounce = True

                for r in reservas:
                    if r[1] == idReserva:
                        debounce = False

                return debounce
            else:
                debounce = False

                for rr in reservas:
                    if rr[1] == idReserva2:
                        debounce = True

                return debounce


        while op != 0:
            op = str(input('1 - Registar Reservas: \n'
                           '2 - Listar Reservas: \n'
                           '3 - Imprimir talão: \n'))

            if op == '1':
                IdReserva = int(input('Insira o Id Da Reserva: \n'))
                re = Reservas(IdReserva,
                              input('Insira o Nif Do Cliente: \n'),
                              int(input('Insira o Id do Quarto: \n')),
                              float(input('Insira o Preço: \n')),
                              int(input('Insira o numero de noites: \n'))
                              )
                if validarReserva(IdReserva, 'ntavazinho'):
                    reservas.append({
                        1: re.get_Id(),
                        2: re.get_NifCliente(),
                        3: re.get_IdQuarto(),
                        4: re.get_Preco(),
                        5: re.get_NumNoites(),
                        6: re.imprimeTalao()
                    })
                else:
                    print('O Id: ' + str(IdReserva) + ' já foi registrado no nosso sistema!')
            elif op == '2':
                for x in reservas:
                    print('Id Da Reserva: ' + str(x[1]) + ' Nif Do Cliente: ' + str(x[2]) +
                          ' Id do Quarto: ' + str(x[3]) +
                          ' Preço: ' + str(x[4]) +
                          ' Número de Noites: ' + str(x[5]))
            elif op == '3':
                op1 = int(input('Insira o Id Da Reserva: '))
                if validarReserva('', op1):
                    for x in reservas:
                        if x[1] == op1:
                            with open('Ficheiros/Taloes.csv', 'a+', newline='') as file:
                                writer = csv.writer(file)
                                writer.writerow([x[2], x[6]])
                                print(x[6])
            else:
                print('Erro Insira uma opção valida do menu!')
    else:
        new = open("Ficheiros/Taloes.csv", "x")
        with open('Ficheiros/Taloes.csv', 'a+', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['NifCliente', 'Talao'])
else:
    os.mkdir('Ficheiros')
