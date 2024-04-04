import random
from funcoes import *

def menu1():
    dados = []
    while True:
        gerar = input('\nMenu Inicial\n1 - Gerar lista\n2 - Inserir lista\n3 - Sair\nOque deseja fazer?: ')
        if gerar == '1':
            tam = int(input('Quantos numeros deseja gerar?: '))
            dados = random.sample(range(-100000000000000,100000000000000), tam)
            print(f'{dados}\nEsses serão seus {tam} números.')
            menu2(dados)
        
        elif gerar == '2':
            dados = []
            dado = input('Digite os valores que deseja inserir: ').split(', ')
            
            for i in dado:
                int(i)
                
                if i in dados:
                    opt = input(f'{i} Esse numero já está na lista, deseja inserir mesmo assim?: ')
                    
                    if opt == 'sim':
                        dados.append(i)
                    
                    else:
                        pass
                
                else:
                    dados.append(i)
            print(f'{dados}\nEsses serão seus {len(dados)} números.')
            menu2(dados)
        
        else:
            print('Você escolheu sair.')
            return

def menu2(lista):
    escolha = input('\nOpções de organização\n1 - Selection Sort\n2 - Insertion Sort\n3 - Bubble Sort\n4 - Voltar ao menu inicial\nComo deseja organizar a lista?: ')
    
    if escolha == '1':
        print(selectionSort(lista))
    
    elif escolha == '2':
        print(insertionSort(lista))
    
    elif escolha == '3':
        print('Ainda em desenvolvimento')
    
    else:
        menu1()
        
menu1()


