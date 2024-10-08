def verificaAlunoTurma(nome1, turma2, turmaEscolha):
    l = False
    
    for i in range(0, len(turma2)):
        if len(turma2[i]) == 0 :
            l = False
        else:
            for t in range(-1, len(turma2[i])):
                if nome1 == turma2[i][t][0]:
                    l = True

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
    idade = int(input("Digite a idade do aluno: "))


    mostraTurma(e, d)
    turma3 = int(input("Digite o ID da turma: "))
    if turma3 > len(e) or turma3 < 0:
        print("Erro! turma não existente")
        vef = False
    else:
        vef = verificaAlunoTurma(nome, e , turma3)
    
    while vef == True:
        
        print("ERRO! aluno ja cadastrado em alguma turma!")
        print("Escolha uma opção: ")
        print("1--trocar turma e manter o aluno--")
        print("2--trocar aluno e manter a turma--")
        op = int(input("Digite sua opção: "))

        if op == 1:
            mostraTurma(e, d)
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
            if e[i][l][0]  == a:
                achou = True
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
    

def removeTurma(es, de):
    print("-----------------------")
    mostraTurma(es, de)
    print("-----------------------")
    op = int(input("Digite o ID da turma a ser excluida: "))
    if op > len(es):
        print("Turma não existente!")
    else:
        del(es[op])
        del(de[op])

    return [es, de]




def mostraMediaMaior():
    print("---------- Seja Bem-Vindo ----------")

def mostraTurma(e, d):
    print("--Turmas cadastradas--")
    if len(e) == 0:
        print("Não existe turmas cadastradas ainda")
    else:
        for i in range(0, len(e)):
            print("ID: ", i , " turma de ", d[i])
    
    print("-----------------------")

        
def mostraTurmas(e, d):
    mostraTurma(e, d)
    x = int(input("Digite o ID da turma que vc deseja ver: "))
    if x <= len(e):
        print("-Alunos cadastrados-")
        for i in range(0,len(e[x])):
            print("Aluno: ",e[x][i][0])
    else:
        print("Essa turma não existe!")        


def mostraAluno(e):
    print("--------------------")


    a = input("Digite o nome do aluno que vc deseja ver: ")

    achou = False
    for i in range(0, len(e)):
        for l in range(0, len(e[i])):
            if e[i][l][0]== a:
                achou = True
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
            x = removeTurma(escola, disciplina)
            escola = x[0]
            disciplina = x[1]

        elif opcao == 4:
            escola = removeAluno(escola)

        elif opcao == 5:
            mostraTurmas(escola, disciplina)

        elif opcao == 6:
            mostraAluno(escola)

        


    return escola, disciplina





Escola = [[['kaua', 18, ['10', '8', '9']], ['nicole', 18, ['10', '9', '8']]], [['carolina', 17, ['10', '9', '8', '7']], ['arthut', 19, ['10', '9', '8', '7', '6', '10']]], [['beatrice', 18, ['10', '9', '10', '8']], ['renan', 18, ['10', '2', '8', '10', '9']]]]
Disciplina = ["alg","mat","bio"]



print("---------- Seja Bem-Vindo ----------")
final = menu(Escola, Disciplina)
print("---------- volte sempre ------------")

print(Escola)

print(" ")
print("----------")
print("disciplinas/turmas")

for i in range(len(Escola)):
    
    print("Disciplina ",Disciplina[i]," :")
    
    for l in range(0, len(Escola[i])):
        
        achou = True
        print("Aluno nº",l)
        print(" Nome: ",Escola[i][l][0])
        print(" Idade: ",Escola[i][l][1])
        print(" Notas: ")
        for n in Escola[i][l][2]:
            print("      ", n)
        print()
    print("----------")

print("FIM! obrigado pela visita")


