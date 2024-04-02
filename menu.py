import time
import random

def menu1():
    dados = []
    while True:
        gerar = input('\n1 - Gerar lista\n2 - Inserir lista\n3 - Sair\nOque deseja fazer?: ')
        if gerar == '1':
            dados = random.sample(range(-100000000000000,100000000000000), 10000)
            print(f'{dados} Esses serão seus 10000 números.')
            menu2(dados)
        elif gerar == '2':
            dado = input('Digite os valores que deseja inserir: ').split(', ')
            for i in dado:
                int(i)
                dados.append(i)
            print(f'{dados} Esses serão seus 10000 números.')
            menu2(dados)
        else:
            print('Você escolheu sair.')
            False

def menu2(lista):
    escolha = input('1 - Selection Sort\n2 - Insertion Sort\n3 - Bubble Sort\n4 - Voltar ao menu inicial\nComo deseja organizar a lista?: ')
    if escolha == '1':
        pass
    elif escolha == '2':
        pass
    elif escolha == '3':
        pass
    else:
        menu1()
        
        


