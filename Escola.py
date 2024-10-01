def verificaAlunoTurma(nome1, turma2, turmaEscolha):
    l = False
    for i in range(0, turma2):
        if turmaEscolha == turma2[i]:
            for e in range(0, turma2[i]):
                if nome1 in turma2[i][e]:
                    l = True
    return l


def vericaAluno():
    x=x
def verificaTurma():
    x=0

def cadastroTurma(e,d):

    nome = input("Digite o nome da disciplina: ")
    turma = []

    while nome in d:
        print("Disciplina ja cadastrada!")
        print("tente novamente")
        nome = input("Digite o nome da disciplina: ")
        
    return [nome, turma]

        

        




    
    nAuno = input("Digite o nome do aluno que deseja adicionar")


        

def cadastroAluno(a, t, d, e):
    
    existe = False

    nome = input("Digite o nome do aluno: ")


    def mostraTurmas(e, d)
    turma3 = int(input("Digite o ID da turma: "))
    

    vef = verificaAlunoTurma(nome, t, turma3)

    while vef == False:
        
        print("ERRO! aluno ja cadastrado nessa turma!")
        print("Escolha uma opção: ")
        print("1--trocar turma e manter o aluno--")
        print("2--trocar aluno e manter a turma--")
        op = int(input("Digite sua opção: "))

        if op == 1:
            def mostraTurmas(e, d)
            turma3 = int(input("Digite a turma: "))
            vef = verificaAlunoTurma(nome, t, turma3)

        elif op == 2:
            nome = input("Digite o nome do aluno: ")
            idade = int(input("Digite a idade do aluno: "))
            vef = verificaAlunoTurma(nome, t, turma3)
    
    notas = []
    n = ("Digite quantas avaliaçoes foram feitas: ")

    for i in range(0, n):
        nota = input("Digite a nota ", i, ": ")
        notas.append(nota)

    


    return [nome, idade, notas]
    



def removeAluno():
    print("---------- Seja Bem-Vindo ----------")

def removeTurma(e, t, d):
    print("-----------------------")
    def mostraTurmas(e, d)
    print("-----------------------")
    op = int(input("Digite o ID da turma a ser excluida: "))
    if op > len(e):
        print("Turma não existente!")
    else:
        e.del(op)
        d.del(op)

    return [e, d]

def removeDisciplina():
    print("---------- Seja Bem-Vindo ----------")


def mostraMediaMaior():
    print("---------- Seja Bem-Vindo ----------")

def mostraTurmas(e, d):
    print("--Turmas cadastradas--")
    for i in range(0, len(e)):
        print("ID: ", i , " turma de "d[i])
    
    print("-----------------------")

        
    

def mostraAluno():
    print("---------- Seja Bem-Vindo ----------")



def menu(escola, disciplina, turma, aluno):
    
    

    opcao = 1

    while opcao != 0:
        print("")
        print("1 - Cadastra Turma -")
        print("2 - Cadastra Aluno -")
        print("3 - Remove turma")
        print("4 - Remover aluno")
        print("5 - mostrar turma -")
        print("6 - mostrar aluno")
        print("7 - mostrar Disciplina")
        print("0 - Sair")
        opcao = int(input("Digite a opcao escolhida: "))


        if opcao == 1:
            x = cadastroTurma(aluno, turma, Disciplina)
            escola.append(x[1])
            disciplina.append(z[0])

        elif opcao == 2:
            x = cadastroAluno(aluno, turma, disciplina, escols)
            aluno.append(x)
            turma.append
   
        elif opcao == 3:
            escola = removeTurma(escola, turma, disciplina)

        elif opcao == 4:
            removeAluno()

        elif opcao == 5:
            mostraTurmas(escola, disciplina)

        elif opcao == 6:
            mostraAluno()

        elif opcao == 7:
            mostraDisciplinas()





Escola = []
Disciplina = []
Turma = []
Aluno = []


print("---------- Seja Bem-Vindo ----------")
menu(Escola, Disciplina, Turma, Aluno)
print("---------- volte sempre ------------")

print(Escola[Turma[Aluno]])