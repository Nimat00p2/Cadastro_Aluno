
import os
import sys
import random

# ---------------------------------------------------------------

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def remover(indice):
    for i, aluno in enumerate(alunos, 1):
            if indice == i:
                alunos.remove(aluno)
                input('Removido com Sucesso\nEnter para continuar...\n')
                limpar_tela()

def nome_aluno():
    nome = input('Nome do aluno: ').title().replace(' ', '-')
    limpar_tela()
    for i, aluno in enumerate(alunos, 1):
        if nome == aluno['nome']:
            informacoes(i, aluno)
            input('\nEnter para continuar...\n')
            limpar_tela()
            return i
    input(f'Aluno {nome} não existe\nEnter para continuar...\n')
    limpar_tela()
    return 

def id_aluno():
    while True:
        id_ = input('id do aluno: ').replace(' ', '')
        limpar_tela()
        if not id_.isdecimal():
            print('Digite apenas numeros')
            continue
        for i, aluno in enumerate(alunos, 1):
            if id_ == aluno['id']:
                informacoes(i, aluno)
                input('\nEnter para continuar...\n')
                limpar_tela()
                return i
        input(f'id {id_} não existe\nEnter para continuar...\n')
        limpar_tela()
        return 

def informacoes(i, aluno):
    print(
            f'{i}. Aluno: {aluno['nome']}  |  '
            f'id: {aluno['id']}\n'
            f'Nota 1°.Bimestre: {aluno['1°Bimestre']}  -  '
            f'Nota 2°.Bimestre: {aluno['2°Bimestre']}  -  '
            f'Nota 3°.Bimestre: {aluno['3°Bimestre']}  -  '
            f'Nota 4°.Bimestre: {aluno['4°Bimestre']} | '
            f'Media: {aluno['media']}\n'
            )

def nota_verificador(bimestre):
    print(bimestre)
    while True:
        valor = input().replace(' ','')
        limpar_tela()
        if not valor.isdigit():
            print('Digite apenas numeros')
            continue
        return valor

def nota_modificador(indice):
    for i, aluno in enumerate(alunos, 1):
        if indice == i:
            nota_primeiro = nota_verificador('Nota do Primeiro Bimestre - ')
            nota_segundo = nota_verificador('Nota do Segundo Bimestre - ')
            nota_terceiro = nota_verificador('Nota do Terceiro Bimestre - ')
            nota_quarto = nota_verificador('Nota do Quarto Bimestre - ')
            media = (int(nota_primeiro) + int(nota_segundo) + int(nota_terceiro) + int(nota_quarto)) / 4
            aluno['1°Bimestre'] = nota_primeiro
            aluno['2°Bimestre'] = nota_segundo
            aluno['3°Bimestre'] = nota_terceiro
            aluno['4°Bimestre'] = nota_quarto
            aluno['media'] = media
            informacoes(i, aluno)
            input(f'Aluno {aluno['nome']} alterado com sucesso\nEnter para continuar...\n')
            limpar_tela()


# ---------------------------------------------------------------

def cadastra_aluno():
    while True:
        nome = input('Nome do aluno - ').title().replace(' ', '-')
        limpar_tela()
        if any(aluno['nome'] == nome for aluno in alunos):
            print('Aluno ja cadastrado')
            continue
        break
    nota_primeiro = nota_verificador('Nota do Primeiro Bimestre - ')
    nota_segundo = nota_verificador('Nota do Segundo Bimestre - ')
    nota_terceiro = nota_verificador('Nota do Terceiro Bimestre - ')
    nota_quarto = nota_verificador('Nota do Quarto Bimestre - ')
    media = (int(nota_primeiro) + int(nota_segundo) + int(nota_terceiro) + int(nota_quarto)) / 4
    id_aluno = ''
    while True:
        id_aluno = ''
        for _ in range(5):
            id_aluno += str(random.randint(0, 9))
        if any(id_existe['id'] == id_aluno for id_existe in alunos):
            continue
        break
    aluno = {
        'nome': nome,
        '1°Bimestre': nota_primeiro,
        '2°Bimestre': nota_segundo,
        '3°Bimestre': nota_terceiro,
        '4°Bimestre': nota_quarto,
        'media': media,
        'id': id_aluno
    }
    alunos.append(aluno)
    limpar_tela()
    input(f'Aluno {nome} registrado com sucesso | id {id_aluno}\nEnter para continuar...\n')
    limpar_tela()

def alterar_nota(resposta):
    if resposta == '1':
        indice = nome_aluno()
        nota_modificador(indice)
    else:
        indice = id_aluno()
        nota_modificador(indice)

def mostrar_aluno(resposta):
    if resposta == '1':
        for i, aluno in enumerate(alunos, 1):
            informacoes(i, aluno)
        input('\nEnter para continuar...\n')
        limpar_tela()
    elif resposta == '2':
        nome_aluno()
    else:
        id_aluno()

def mostrar_maiores_medias():
    for i, aluno in enumerate(alunos, 1):
        if 7 <= aluno['media']:
            informacoes(i, aluno)
    input('\nEnter para continuar...\n')
    limpar_tela()

def remover_aluno(resposta):
    if resposta == '1':
        indice = nome_aluno()
        remover(indice)
    else:
        indice = id_aluno()
        remover(indice)

# ---------------------------------------------------------------

alunos = []

while True:
    resposta = input(
        'Sistema escolar JoserLagamar\n\n'
        'Selecione uma Opção\n'
        '1 - Cadastrar Aluno\n'
        '2 - Alterar Nota de Aluno\n'
        '3 - Mostras Alunos\n'
        '4 - Mostrar Maiores Medias\n'
        '5 - Remover Aluno\n'
        '6 - Sair\n\n'
        'Opção: '
    )
    limpar_tela()
    
    if resposta == '1':
        cadastra_aluno()

    elif resposta == '2':
        while True:
            resposta = input(
                '---Alterar Nota---\n'
                'Selecione uma Opção\n'
                '1 - Nome de Aluno\n'
                '2 - id do Aluno\n'
                '3 - Voltar\n\n'
                'Opção: '
            )
            limpar_tela()
            if resposta == '1':
                alterar_nota('1')
            elif resposta == '2':
                alterar_nota('2')
            elif resposta == '3':
                break
            else:
                input('Opção invalida\nEnter para continuar...\n')
                limpar_tela()

    elif resposta == '3':
        while True:
            resposta = input(
                '---Mostrar Alunos---\n'
                'Selecione uma Opção\n'
                '1 - Todos os Alunos\n'
                '2 - Nome de Aluno\n'
                '3 - id do Aluno\n'
                '4 - Voltar\n\n'
                'Opção: '
            )
            limpar_tela()
            if resposta == '1':
                mostrar_aluno('1')
            elif resposta == '2':
                mostrar_aluno('2')
            elif resposta == '3':
                mostrar_aluno('3')
            elif resposta == '4':
                break
            else:
                input('Opção invalida\nEnter para continuar...\n')
                limpar_tela()

    elif resposta == '4':
        mostrar_maiores_medias()

    elif resposta == '5':
        while True:
            resposta = input(
                '---Remover Aluno---\n'
                'Selecione uma Opção\n'
                '1 - Nome de Aluno\n'
                '2 - id do Aluno\n'
                '3 - Voltar\n\n'
                'Opção: '
            )
            limpar_tela()
            if resposta == '1':
                remover_aluno('1')
            elif resposta == '2':
                remover_aluno('2')
            elif resposta == '3':
                break
            else:
                input('Opção invalida\nEnter para continuar...\n')
                limpar_tela()

    elif resposta == '6':
        print('Saindo...')
        sys.exit()
    else:
        input('Opção invalida\nEnter para continuar...\n')
        limpar_tela()
