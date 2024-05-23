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
    for i in range(len(funcionario)):
        for l in range(len(funcionario[i])):
            if funcionario[i][l] == codigo:
                n = i - 1
    for i in range(len(funcionario)):
        for l in range(len(funcionario[i])):
            if i == n:
                return funcionario[i]

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
                print(pesquisarFuncionario(funcionario, codigo))
                print()
            
            if escolha1 == 4:
                os.system('cls')
                print("-------------- Remover funcionário -------------- \n")

            if escolha1 == 5:
                os.system('cls')
                break

    if escolha == 4:
        os.system('cls')
        print("Saindo...")
        break

print("FIM")