def verificaAlunoTurma(nome1, turma2, turmaEscolha):
    l = False
    
   
    for i in range(0, len(turma2)):
        print(turmaEscolha, turma2[i], "oi")
        if len(turma2[i]) == 0 :
            l = True
        else:
            if turmaEscolha == turma2[i]:
                print(nome1, turma2[i][0])
                if nome1 == turma2[i][0]:
                    
                    l = True

    print(l)
    return l



def cadastroTurma(e,d):

    nome = input("Digite o nome da disciplina: ")
    turma = []

    while nome in d:
        print("Disciplina ja cadastrada!")
        print("tente novamente")
        nome = input("Digite o nome da disciplina: ")
        
    return [nome, turma]



        

def cadastroAluno(d, e):
    
    existe = False

    nome = input("Digite o nome do aluno: ")


    mostraTurmas(e, d)
    turma3 = int(input("Digite o ID da turma: "))
    if turma3 > len(e) or turma3 < 0:
        print("Erro! turma não existente")
        vef = False
    else:
        vef = verificaAlunoTurma(nome, e , turma3)
    
    while vef == False:
        
        print("ERRO! aluno ja cadastrado nessa turma!")
        print("Escolha uma opção: ")
        print("1--trocar turma e manter o aluno--")
        print("2--trocar aluno e manter a turma--")
        op = int(input("Digite sua opção: "))

        if op == 1:
            mostraTurmas(e, d)
            turma3 = int(input("Digite a turma: "))
            vef = verificaAlunoTurma(nome, e, turma3)

        elif op == 2:
            nome = input("Digite o nome do aluno: ")
            idade = int(input("Digite a idade do aluno: "))
            vef = verificaAlunoTurma(nome, e, turma3)
    
    notas = []
    n = int(input("Digite quantas avaliaçoes foram feitas: "))

    for i in range(0, n):
        nota = input("Digite a nota: ")
        notas.append(nota)

    


    return [[nome, idade, notas],turma3]
    



def removeAluno(e):
    print("--------------------")
    a = input("Digite o nome do aluno que vc deseja remover: ")

    achou = False
    for i in range(0, len(e)):
        for l in range(0, len(e[i])):
            if e[i][l][0]== a:
                achou == True
                del(e[i][l][0])
    
    op = 0
    while achou == False and op != 1:
        print("Aluno não encontrado!")
        print("-----------------------")
        print("------opções-----------")
        print("1 - Sair")
        print("2 - repetir")
        print("-----------------------")
        op = int(input("Digite sua opção"))
        if op == 2:
            print("--------------------")
            a = input("Digite o nome do aluno que vc deseja remover: ")
            achou = False
            for i in range(0, len(e)):
                for l in range(0, len(e[i])):
                    if e[i][l][0]== a:
                        achou == True
                        del(e[i][l][0])

    print("-----------------------")

    return e
    

def removeTurma(e, t, d):
    print("-----------------------")
    mostraTurmas(e, d)
    print("-----------------------")
    op = int(input("Digite o ID da turma a ser excluida: "))
    if op > len(e):
        print("Turma não existente!")
    else:
        del(e[op])
        del(d[op])

    return [e, d]

def removeDisciplina(e, d):
    print("-----------------------")
    mostraTurmas(e, d)
    print("-----------------------")
    op = int(input("Digite o ID da disciplina a ser excluida: "))
    if op > len(e):
        print("Disciplina não existente!")
    else:
        print("-----------------------")
        print("A turma da disciplina que sera excluida tbm sera excluida")
        op2 = input("Ainda quer continuar?[S/N]")
        if op2 == "S":
            del(e[op])
            del(d[op])
        else:
            print("OK! você voltara para o menu")

    return [e, d]




def mostraMediaMaior():
    print("---------- Seja Bem-Vindo ----------")

def mostraTurmas(e, d):
    print("--Turmas cadastradas--")
    for i in range(0, len(e)):
        print("ID: ", i , " turma de ", d[i])
    
    print("-----------------------")

        
    

def mostraAluno(e):
    print("--------------------")
    a = input("Digite o nome do aluno que vc deseja ver: ")

    achou = False
    for i in range(0, len(e)):
        for l in range(0, len(e[i])):
            if e[i][l][0]== a:
                achou == True
            print("Aluno nº",l)
            print("Nome: ",e[i][l][0])
            print("Idade: ",e[i][l][1])
            print("Notas: ")
            for n in e[i][l][2]:
                print("  ", n)
    
    
    if achou == False:
        print("Aluno não encontrado!")
    print("-----------------------")

def menu(escola, disciplina):

    opcao = 1

    while opcao != 0:
        print("")
        print("1 - Cadastra Turma --")
        print("2 - Cadastra Aluno -")
        print("3 - Remove turma -")
        print("4 - Remover aluno -")
        print("5 - mostrar turma --")
        print("6 - mostrar aluno -")
        print("0 - Sair")
        opcao = int(input("Digite a opcao escolhida: "))


        if opcao == 1:
            x = cadastroTurma(escola, disciplina)
            escola.append(x[1])
            disciplina.append(x[0])
            print(escola)

        elif opcao == 2:
            x = cadastroAluno(disciplina, escola)
            escola[x[1]].append(x[0])
   
        elif opcao == 3:
            escola = removeTurma(escola)

        elif opcao == 4:
            e = removeAluno(escola)

        elif opcao == 5:
            mostraTurmas(escola, disciplina)

        elif opcao == 6:
            mostraAluno()

        


    return escola, disciplina





Escola = []
Disciplina = []
Turma = []



print("---------- Seja Bem-Vindo ----------")
final = menu(Escola, Disciplina)
print("---------- volte sempre ------------")

print(Escola)