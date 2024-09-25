def cadastroTurma(e):

    if len(e) == 0:
        


    turma=[]




    


def cadastroAluno(a, t):
    
    existe = False

    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))
    notas = []
    n = ("Digite quantas avaliaçoes foram feitas: ")



    


    

    for i in range(0, n):
        nota = input("Digite a nota ", i, ": ")
        notas.append(nota)


    a.append([nome,idade,notas])
    

def cadastroDisciplina():
    print("---------- Seja Bem-Vindo ----------")


def removeAluno():
    print("---------- Seja Bem-Vindo ----------")

def removeTruma():
    print("---------- Seja Bem-Vindo ----------")

def removeDisciplina():
    print("---------- Seja Bem-Vindo ----------")


def mostraMediaMaior():
    print("---------- Seja Bem-Vindo ----------")

def mostraTurmas():
    print("---------- Seja Bem-Vindo ----------")

def mostraAluno():
    print("---------- Seja Bem-Vindo ----------")

def mostraDisciplinas():
    print("---------- Seja Bem-Vindo ----------")


def menu(escola, disciplina, turma, aluno):
    
    

    opcao = 1

    while opcao != 0:
        print("")
        print("1 - Cadastra Turma")
        print("2 - Cadastra Aluno")
        print("3 - Cadastra Disciplina")
        print("4 - Remove turma")
        print("5 - Remover aluno")
        print("6 - Remover Disciplina")
        print("7 - mostrar turma")
        print("8 - mostrar aluno")
        print("9 - mostrar Disciplina")
        print("0 - Sair")
        opcao = int(input("Digite a opcao escolhida: "))


        if opcao == 1:
            escola.append(cadastroTurma(escola))

        elif opcao == 2:
            cadastroAluno(aluno, turma)
        
        elif opcao == 3:
            cadastroDisciplina()
   
        elif opcao == 4:
            removeTruma()

        elif opcao == 5:
            removeAluno()
        
        elif opcao == 6:
            removeDisciplina()

        elif opcao == 7:
            mostraTurmas()

        elif opcao == 8:
            mostraAluno()

        elif opcao == 9:
            mostraDisciplinas()





Escola = []
Disciplina = []
Turma = []
Aluno = []


print("---------- Seja Bem-Vindo ----------")
menu(Escola, Disciplina, Turma, Aluno)
print("---------- volte sempre ------------")

print(Escola)