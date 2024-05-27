import os

# 1ª opção: Menu funcionários, Fazer a parte de registrar usando matriz e depois aamazenar em uma lista, também devem ser incluídas as funções listar, pesquisar e remover funcionários.
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
        funcionario2[i] = [str] * 3

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
        if funcionario[i][2] == str:
            print("Funcionario: ", funcionario[i][0], ", codigo: ", funcionario[i][1], ", IMC não cadastrado! ")
        else:
            print("Funcionario: ", funcionario[i][0], ", codigo: ", funcionario[i][1], ", IMC: ", funcionario[i][2])

def pesquisarFuncionario(funcionario, codigo):
    dado = [str] * 1
    for o in range(len(dado)):
        dado[o] = [str] * 3
    n = 0
    for i in range(len(funcionario)):
        for l in range(len(funcionario[i])):
            if funcionario[i][l] == codigo:
                dado.append(funcionario[i])
                n += 1
    if n == 1:
        if dado[i][2] == str:
            print("Funcionario: ", dado[i][0], ", codigo: ", dado[i][1], ", IMC não cadastrado! ")
        else:
            print("Funcionario: ", dado[i][0], ", codigo: ", dado[i][1], ", IMC: ", dado[i][2])
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
        if funcionario[indice][2] == str:
            print("Funcionario: ", funcionario[indice][0], ", codigo: ", funcionario[indice][1], "IMC não cadastrado! ")
            temCerteza = int(input("Tem certeza que deseja excluir esse funcionario? \n"
                                    "[ 1 ] - Sim \n"
                                    "[ 2 ] - Não \n"
                                    "Digite: "))
            if temCerteza == 1:
                funcionario.pop(indice)
                print("Funcionário excluído! ")   
            elif temCerteza == 2:
                print("FUncionário não excluído! ")
            else:
                print("Erro! valor digitado não corresponde a nenhuma opção fornecida! ")  
        else:
            print("Funcionario: ", funcionario[indice][0], ", codigo: ", funcionario[indice][1], "IMC: ", funcionario[indice][2])    
            temCerteza = int(input("Tem certeza que deseja excluir esse funcionario? \n"
                                    "[ 1 ] - Sim \n"
                                    "[ 2 ] - Não \n"
                                    "Digite: "))
            if temCerteza == 1:
                funcionario.pop(indice)
                print("Funcionário excluído! ")   
            elif temCerteza == 2:
                print("FUncionário não excluído! ")
            else:
                print("Erro! valor digitado não corresponde a nenhuma opção fornecida! ")     

    
# 2ª opção: Avaliação de saúde. Inicialmente fazer uma opção para calcular IMC, informar ao usuário e armazenar o IMC na matriz de funcionários, caso outras ideias apareçam, elas devem ser descritas ou mencionadas nesse comentário.
def medirIMC(altura, peso):
    imc = peso/(altura*altura)
    if imc < 18.5:
        return 1, str(f'{imc:.2f}')
    elif imc >= 18.5 and imc < 25.0:
        return 2, str(f'{imc:.2f}')
    elif imc >= 25.0 and imc < 30.0:
        return 3, str(f'{imc:.2f}')
    elif imc >= 30.0 and imc < 35.0:
        return 4, str(f'{imc:.2f}')
    elif imc >= 35.0 and imc < 40.0:
        return 5, str(f'{imc:.2f}')
    else:
        return 6, str(f'{imc:.2f}')
    
def registrarIMC(funcionario, imc, indice):
    funcionario[indice][2] = imc

# 3ª opção do menu: programa de exercio, criar uma pilha contendo alguns exercicios, cada exercicio deve ser feito na ordem da pilha e ao ser realizado deve ser retirado da pilha, quando todos os exercicios tiverem completos a pilha deve reiniciar.
exercicios = []
def pushPilha(pilha, valor):
    pilha.append(valor)

def isEmpyt(pilha):
    if len(pilha) == 0:
        return True
    else:
        return False

def removerPilha(pilha):
    if isEmpyt(pilha) == False:
        return pilha.pop()
    else:
        return None
    

pushPilha(exercicios, '15 Flexões')
pushPilha(exercicios, '15 Abdominal')
pushPilha(exercicios, '1,5km Caminhada')
pushPilha(exercicios, '20 Polichinelos')
pushPilha(exercicios, '45s Prancha')
pushPilha(exercicios, '20 Agachamentos')

exercicio = [str] * len(exercicios)
exercicio2 = [str] * len(exercicios)
for i in range(len(exercicio)):
    exercicio[i] = removerPilha(exercicios)
for l in range(len(exercicio2)):
    exercicio2[l] = exercicio[i]
    pushPilha(exercicios, exercicio2[l])
    i -= 1


#---------------Código principal-----------------
while True:
    escolha = int(input("-------------- MENU -------------- \n"
                    "Escolha uma opção: \n"
                  "[ 1 ] - MENU Funcionários. \n"
                  "[ 2 ] - Avaliação de saúde. \n"
                  "[ 3 ] - Programa de exercícios \n"
                  "[ 4 ] - SAIR \n"
                  "Digite: "))

    if escolha == 1:
        os.system('cls')
        while True:
            escolha1 = int(input("-------------- MENU FUNCIONÁRIOS -------------- \n"
                    "Escolha uma opção: \n"
                  "[ 1 ] - Registrar funcionário. \n"
                  "[ 2 ] - Listar Funcionários. \n"
                  "[ 3 ] - Pesquisar Funcionário. \n"
                  "[ 4 ] - Remover Funcionário. \n"
                  "[ 5 ] - Voltar ao menu. \n"
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

            elif escolha1 == 2:
                os.system('cls')
                print("-------------- Lista de funcionários -------------- \n")
                listarFuncionario(funcionario)
                print()
            
            elif escolha1 == 3:
                os.system('cls')
                print("-------------- Pesquisar funcionário -------------- \n")
                codigoPesquisa = input("Digite qual o codigo do funcionário: ")
                pesquisarFuncionario(funcionario, codigoPesquisa)
                print()
            
            elif escolha1 == 4:
                os.system('cls')
                print("-------------- Remover funcionário -------------- \n")
                codigoPesquisa = input("Digite o codigo do funcionário: ")
                indice = pesquisarFuncionario2(funcionario, codigoPesquisa)
                removerFuncionario(funcionario, indice)

            elif escolha1 == 5:
                os.system('cls')
                break

            else:
                print("Código inválido! ")

    elif escolha == 2:
        os.system('cls')
        while True:
            print("-------------- Avaliação de saúde --------------")
            escolha2 = int(input("Escolha uma opção: \n"
                  "[ 1 ] - Medir IMC. \n"
                  "[ 2 ] - Voltar ao menu. \n"
                  "Digite: "))
            if escolha2 == 1:
                os.system('cls')
                codigoPesquisa = input("Digite o codigo do funcionário: ")
                indice = pesquisarFuncionario2(funcionario, codigoPesquisa)
                if indice == None:
                    print("Erro, funcionário não foi encontrado! ")
                else:
                    altura = float(input("Digite a sua altura(em metros, ex: 1.70): "))
                    peso = float(input("Digite o seu peso(em quilogramas, ex: 68.2): "))
                    resIMC, imc = medirIMC(altura, peso)
                    if resIMC == 1:
                        print("IMC: {imc:.2f}")
                        print("Você está na categoria de magreza, é recomendável a procura de um profissional de saúde!")
                        registrarIMC(funcionario, imc, indice)
                    elif resIMC == 2:
                        print("IMC: ", imc)
                        print("Você está na categoria normal, de acordo com o IMC você está saudável! ")
                        registrarIMC(funcionario, imc, indice)
                    elif resIMC == 3:
                        print("IMC: ", imc)
                        print("Você está com sobrepeso, fique atento! ")
                        registrarIMC(funcionario, imc, indice)
                    elif resIMC == 4:
                        print("IMC: ", imc)
                        print("Você está com obesidade grau I, por favor procure um profissional de saúde! ")
                        registrarIMC(funcionario, imc, indice)
                    elif resIMC == 5:
                        print("IMC: ", imc)
                        print("Você está com obesidade grau II, por favor procure um profissional de saúde!")
                        registrarIMC(funcionario, imc, indice)
                    else:
                        print("IMC: ", imc)
                        print("Você está com obesidade grau III, por favor procure urgentemente um profissional de saúde!")
                        registrarIMC(funcionario, imc, indice)
            elif escolha2 == 2:
                print("Saindo para o menu principal. ")
                os.system('cls')
                break
            else:
                print("Número digitado inválido! ")
    
    elif escolha == 3:
        os.system('cls')
        while True:
            print("Atenção! O recomendado é que os exercícios sejam feitos semanalmente ou a cada 3 dias. \n"
                "Os exercicios devem ser feitos de acordo com a ordem que aparecem na lista. ")
            escolha3 = int(input("-------------- Programa de exercícios -------------- \n"
                                "[ 1 ] - Listar exercícios \n"
                                "[ 2 ] - Completar exercicio \n"
                                "[ 3 ] - Sair \n"
                                "Digite: "))
            if escolha3 == 1:
                os.system('cls')
                print("-------------- Lista de exercícios --------------")
                vetorExercicio = [str] * len(exercicios)
                vetorExercicio2 = [str] * len(exercicios)
                for i in range(len(vetorExercicio)):
                    vetorExercicio[i] = removerPilha(exercicios)
                    print(vetorExercicio[i])
                for l in range(len(vetorExercicio2)):
                    vetorExercicio2[l] = vetorExercicio[i]
                    pushPilha(exercicios, vetorExercicio2[l])
                    i -= 1

            elif escolha3 == 2:
                os.system('cls')
                print("-------------- Completar de exercício --------------")
                if isEmpyt(exercicios) == False:
                    completou = int(input("Você completou o primeiro exercicio da lista? \n"
                                          "[ 1 ] - sim \n"
                                          "[ 2 ] - Não \n"
                                          "Digite: "))
                    if completou == 1:
                        removerPilha(exercicios)
                    elif completou == 2:
                        print("continue tentando! ")
                    else:
                        print("Opção digitada inválida! ")
                else:
                    print("Exercicios completos, Parabens! \n"
                          "Os exercícios seram reiniciados! ")
                    for i in range(len(exercicio2)):
                        pushPilha(exercicios, exercicio2[i])

            elif escolha3 == 3:
                break

            else:
                print("Número digitado inválido! ")

    elif escolha == 4:
        os.system('cls')
        print("Saindo...")
        break
     
    else:
        print("Número digitado inválido! ")

print("FIM")