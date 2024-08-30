from Projecto import Projetos

from Cliente import Cliente

op = 1

clientes = []

projectos = []


def validarCliente(nif, email):
    if email != '':
        debounce = True

        for c in clientes:
            if c[1] == nif or c[4] == email:
                debounce = False

        return debounce
    else:
        debounce = False

        for c in clientes:
            if c[1] == nif:
                debounce = True

        return debounce


def validarProjecto(codigo):
    debounce = True

    for p in projectos:
        if p[1] == codigo:
            debounce = False

    return debounce


while op != 0:
    op = str(input('Insira 1 para registar Clientes\nInsira 2 para registrar Projetos\nInsira 3 para listar '
                   'Clientes\nInsira 4 para listar Projectos\n'))
    if op == '1':
        Nif = str(input('Insira o Nif Do Cliente: \n'))
        Email = str(input('Insira o Email Do Cliente: \n'))
        cl = Cliente(Nif,
                     str(input('Insira o Nome Do Cliente: \n')),
                     str(input('Insira a Morada Do Cliente: \n')),
                     Email,
                     str(input('Insira o Telefone Do Cliente: \n'))
                     )
        if validarCliente(Nif, Email):
            clientes.append({
                1: cl.returnNif(),
                2: cl.returnNome(),
                3: cl.returnMorada(),
                4: cl.returnEmail(),
                5: cl.returnTelefone()
            })
        else:
            print('Já existe um Cliente com esse nif ou email registrado!')
    elif op == '2':
        Nif = str(input('Insira o Nif Do Cliente: \n'))
        Cod = str(input('Insira o Codigo Do Projecto: \n'))
        pr = Projetos(Cod,
                      str(input('Insira a Descrição Do Projecto: \n')),
                      str(input('Insira o Tipo Do Projecto: \n')),
                      Nif
                      )
        if validarCliente(Nif, ''):
            if validarProjecto(Cod):
                projectos.append({
                    1: pr.returnCod(),
                    2: pr.returnDescricao(),
                    3: pr.returnTipo(),
                    4: pr.returnNifCliente()
                })
            else:
                print('Já existe um codigo de projecto: ' + Cod + ' registrado!')
        else:
            print('Não existe nenhum cliente com o nif: ' + Nif + ' registrado!')
    elif op == '3':
        for cli in clientes:
            print('Nif do Cliente: ' + cli[1] + '\n'
                  + 'Nome do Cliente: ' + cli[2] + '\n'
                  + 'Morada do Cliente: ' + cli[3] + '\n'
                  + 'Email do Cliente: ' + cli[4] + '\n'
                  + 'Telefone do Cliente: ' + cli[5])
    elif op == '4':
        for pro in projectos:
            print('Cod do Projecto: ' + pro[1] + '\n'
                  + 'Descrição do Projecto: ' + pro[2] + '\n'
                  + 'Tipo do Projecto: ' + pro[3] + '\n'
                  + 'NifCliente do Projecto: ' + pro[4])
    elif op == '0':
        break
    else:
        print('Insira uma opção valida do menu!')
