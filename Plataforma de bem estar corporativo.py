import os

funcionario = []

def codRepetidoFuncionario(funcionario, codigo):
    n = 0
    for i in range(len(funcionario)):
        for l in range(len(funcionario[i])):
            if funcionario[i][l] == codigo:
                n += 1
    if n == 0:
        return False
    else:
        return True

def registrarFuncionario(funcionario, nome, codigo):
    tam = len(funcionario) + 1
    funcionario2 = [str] * tam
    for i in range(len(funcionario2)):
        funcionario2[i] = [str] * 2

    if len(funcionario2) == 1:
        for a in range(len(funcionario2)):
            for b in range(len(funcionario2[a])):
                if b == 0:
                    funcionario2[a][b] = nome
                if b == 1:
                    funcionario2[a][b] = codigo

    else:
        for a in range(len(funcionario2)):
            for b in range(len(funcionario2[a])):
                if a < tam - 1:
                    funcionario2[a][b] = funcionario[a][b]
                else:
                    if b == 0:
                        funcionario2[a][b] = nome
                    if b == 1:
                        funcionario2[a][b] = codigo

    return funcionario2

def listarFuncionario(funcionario):
    for i in range(len(funcionario)):
        print("Funcionario: ", funcionario[i][0], ", codigo: ", funcionario[i][1])

def pesquisarFuncionario(funcionario, codigo):
    dado = []
    n = 0
    for i in range(len(funcionario)):
        for l in range(len(funcionario[i])):
            if funcionario[i][l] == codigo:
                dado.append(funcionario[i])
                n += 1
    if n == 1:
        print("Funcionário: ", dado[0][0] , ", Codigo: ", dado[0][1])
    
    else:
        print("Não foi encontrada nenhuma correspondência para o codigo inserido! ")

def pesquisarFuncionario2(funcionario, codigo):
    dado = 0
    n = 0
    for i in range(len(funcionario)):
        for l in range(len(funcionario[i])):
            if funcionario[i][l] == codigo:
                dado = i
                n += 1
    if n == 1:
        return dado
    else:
        return None


def removerFuncionario(funcionario, indice):
    if indice == None:
        print("Funcionário não encontrado! ")
    else:
        print("Funcionário: ", funcionario[indice][0] , ", Codigo: ", funcionario[indice][1])
        print()
        temCerteza = int(input("Tem certeza que deseja excluir esse funcionario? \n"
                                    "[ 1 ] - Sim \n "
                                    "[ 2 ] - Não. \n"
                                    "Digite: "))
        if temCerteza == 1:
            funcionario.pop(indice)
            print("Funcionário excluído! ")   
        elif temCerteza == 2:
            print("FUncionário não excluído! ")
        else:
            print("Erro! valor digitado não corresponde a nenhuma opção fornecida! ")                 

while True:
    escolha = int(input("-------------- MENU -------------- \n"
                        "Escolha uma opção:\n"
                  " [ 1 ] - MENU Funcionários.\n "
                  "[ 4 ] - SAIR\n "
                  "Digite: "))
    
    if escolha == 1:
        while True:
            print("-------------- MENU FUNCIONÁRIOS --------------")
            escolha1 = int(input("Escolha uma opção:\n"
                  " [ 1 ] - Registrar funcionário.\n "
                  "[ 2 ] - Listar Funcionários.\n "
                  "[ 3 ] - Pesquisar Funcionário. \n"
                  "[ 4 ] - Remover Funcionário. \n"
                  " [ 5 ] - Voltar ao menu.\n "
                  "Digite: "))
            
            if escolha1 == 1:
                os.system('cls')
                print("-------------- Registrar funcionário --------------")
                nome = input("Digite o nome do funcionário: ")
                codigo = input("Digite qual o código do funcionário: ")
                
                if codRepetidoFuncionario(funcionario, codigo) == True:
                    print("Erro! codigo fornecido já está relacionado a outro funcionário")
                
                if codRepetidoFuncionario(funcionario, codigo) == False:
                    funcionario = registrarFuncionario(funcionario, nome, codigo)
                    print("Funcionário registrado com sucesso! ")

            if escolha1 == 2:
                os.system('cls')
                print("-------------- Lista de funcionários -------------- \n")
                listarFuncionario(funcionario)
                print()
            
            if escolha1 == 3:
                os.system('cls')
                print("-------------- Pesquisar funcionário -------------- \n")
                codigoPesquisa = input("Digite qual o codigo do funcionário: ")
                pesquisarFuncionario(funcionario, codigoPesquisa)
                print()
            
            if escolha1 == 4:
                os.system('cls')
                print("-------------- Remover funcionário -------------- \n")
                codigoPesquisa = input("Digite o codigo do funcionário: ")
                indice = pesquisarFuncionario2(funcionario, codigoPesquisa)
                removerFuncionario(funcionario, indice)


            if escolha1 == 5:
                os.system('cls')
                break

    if escolha == 4:
        os.system('cls')
        print("Saindo...")
        break

print("FIM")