#Este ficheiro contem o programa pedido para o projecto final da desciplina de algoritmia
import os

#Bloco destinado aos varios tipos de pedidos
#funcão para tratar adição de estações
def criarEstacao():
    print('Indique codigo da estação')
    codigo = input().upper()

    while not codigo.isalpha():
        if not codigo.isalpha():
            print('insira so letras')
            codigo = input().upper()

    print('Indique o nome')
    nome = input().upper()

    while not nome.replace(" ", "").isalpha():
        if not nome.replace(" ", "").isalpha():
            print('insira so letras')
            nome = input().upper()
    
    print('Indique a latitude')
    latitude = input()

    while not latitude.isdigit():
        if not latitude.isdigit():
            print('insira so algarismos')
            latitude = input()

    
    
    print('Indique a longitude')
    longitude =input()

    while not longitude.isdigit():
        if not longitude.isdigit():
            print('insira so algarismos')
            longitude = input()

    estacao = "\n" + codigo + "," + nome + "," + 'Latitude:' + latitude + "," + 'Longitude:' + longitude
    gravarFicheiro = open("estacoes.csv", 'a')
    gravarFicheiro.write(estacao)
    gravarFicheiro.close()

#funcão para tratar adição de carris
def criarCarril():
    print('Indique nome da primeira estação')
    nome1 = input().upper()
    print('Indique o nome da segunda estação')
    nome2 = input()
    print('distancia')
    dist = input()
    carril = "\n" + nome1 + "," + nome2 + "," + dist
    gravarFicheiro = open("carris.csv", 'a')
    gravarFicheiro.write(carril)
    gravarFicheiro.close()
#função para tratar da adição de comboios
def criarComboio():
    print('Indique modelo')
    modelo = input().upper()
    print('Indique nº de serie')
    nSerie = input().upper()
    print('Indique nº de passageiros')
    nPax = input()
    print('indique serviço')
    servico = input().upper()
    comboio = "\n" + modelo + "," + nSerie  + "," + nPax + "," + servico
    gravarFicheiro = open("comboios.csv", 'a')
    gravarFicheiro.write(comboio)
    gravarFicheiro.close()  

#Função destinada a gerir a criação dos varios pedidos de criação comboios e etc
def menuGestao():
    escolhaGestao = ''
    while escolhaGestao != 'x' :
        print('Escolha uma das opções :\n A:Adicionar estação \n B:Adicionar carril \n C:Adicionar comboio \n X:sair')
        escolhaGestao = input().lower()
            
        if escolhaGestao == 'a':
            criarEstacao()
            
        elif escolhaGestao == 'b':
            criarCarril()
        
        elif escolhaGestao == 'c':
            criarComboio()
            
        elif escolhaGestao == 'x':
            print('A sair')
            
        else :
            print('Opção de menu gestão invalida')
            
#função para criar linha(incompleto)
def criarLinha():
    lerLinhas = open('./carris.csv', 'r')
    linhas = lerLinhas.readlines()
    lerLinhas.close() 
    sair = False
     
    while sair == False:
        print('Indique as duas estações para criar a linha /n Indique estação Inicial')
        estacaoA = input()
        print('insira estação B')
        estacaoB = input()
        criarLinha=''

        # Verificar Carris
        for line in linhas:
            if estacaoA  in line and estacaoB in line:  
                break  
            else:
               print("não existe linha")
            

#Função para gestão da criação de linhas e viagens(incompleto)
def menuLinha():
    escolha = ''
    while escolha!= 'x':
        print('Escolha uma das opções :\n A:criar linhas \n B:Criar viagem \n X:sair')

        escolha = input().lower()
        if escolha == 'a':
            criarLinha()

        if escolha == 'b':
            criarViagen()
#Bloco destinado as funções destinadas as listagens
#Função para tratar da listagem das estações
def listaEstacoes():
    lerEstacoes = open('./Estacoes.csv','r')
    estacoes = lerEstacoes.readlines()
    lerEstacoes.close()
    
    for estacao in estacoes:
        print(estacao)

#Função para tratar da listagem das linhas
def listaLinhas():
    lerLinhas = open('./Linhas.csv','r')
    linhas = lerLinhas.readlines()
    lerLinhas.close()
    
    for linha in linhas:
        print(linha)

#Função para tratar da listagem dos Comboios 
def listaComboios():
    lerComboios = open('./Comboios.csv','r')
    comboios = lerComboios.readlines()
    lerComboios.close()
    
    for Comboio in comboios:
        print(Comboio)

#função que vai gerir as listagens
def menuListar ():
    escolha=''
    while escolha !='x' :
        print('inidque o que lista deseja aceder \n A:Estações \n B:Linhas \n C:Comboios \n X:sair')  
        escolha=input().lower()

        if escolha == 'a':
            listaEstacoes()

        if escolha == 'b':
            listaLinhas()

        if escolha == 'c':
            listaComboios()

        if escolha == 'x':
            print('A sair')
#Bloco destinado as varias funções de pesquisa
def procuraComboios():
    lerComboios = open('./Comboios.csv','r')
    comboios = lerComboios.readlines()
    lerComboios.close()
    escolha =''

    while escolha !='x':

        print('Indique o Modelo ou deixe em branco para procurar pelo numero de passageiros /n X:Sair')
        print('Modelo: ')
        modelo = str(input().lower())
        if modelo == '':
            print('Nº max passageiros: ')
            maxPax = str(input())
        
        
        if modelo == ''  and maxPax =='' :
            print('valores invalidos insira novamente')
        else:
            for comboio in comboios:
                
                comboio = comboio.split(',')
                
                
                if comboio[0].lower() == modelo or comboio[2] == maxPax:
                    print('comboio Encotrado: ', comboio)

#Função para pesquisar linhas

def procuraLinha ():
    lerLinhas = open('./Linhas.csv','r')
    linhas = lerLinhas.readlines()
    lerLinhas.close()
    escolha =''
    listaLinhas=[]
    
    while escolha != 'x':

        print('indique a estação que deseja procurar as linhas:')
        estacao = input().upper()

        for line in linhas:
            if estacao in line.upper():
                listaLinhas.append(line)
        escolha = 'x'
                
    for linha in listaLinhas:
        print(linha)
        
#Função para procura de Viagens
def procuraViagem():
    lerViagens = open('./Viagens.csv','r')
    viagens = lerViagens.readlines()
    lerViagens.close()
    escolha =''

    print('indique a estação inicial')
    estacaoA = input().lower()
    print('indique a estacao final')
    estacaoB = input().lower()
    lista = []
    
    for viagem in viagens:
        splitViagem = viagem.split(',')

        estacaoInicialViagem = splitViagem[3].split('#')[0].lower()
        estacaoFinalViagem = splitViagem[len(splitViagem) - 1].split('#')[0].lower()
        
        if estacaoInicialViagem == estacaoA and estacaoFinalViagem == estacaoB :
            lista.append(viagem)
            
    print(lista)        
        

#função destinada as pesquisas 
def menuPesquisa ():
    escolha = ''

    while escolha !='x':

        print('Seleccione uma opção \n A:Procurar comboios \n B:Procura de linha \n C:Procurar Viagem \n X:Sair')
        escolha = input().lower()

        if escolha == 'a':
              procuraComboios()
              
        elif escolha == 'b':
              procuraLinha()

        elif escolha == 'c':
              procuraViagem()
              
############ PROGRAMA ############
escolhaPrincipal=''
while escolhaPrincipal != 'x':
    print("Menu informativo \n Escolha uma opção \n A:Gestão \n B:Listagem \n C:Viagens \n D:Criaçao linha/viagem \n E:Pesquisa \n X:sair")

    escolhaPrincipal = input().lower()

    if escolhaPrincipal == 'a':
        menuGestao()

    if escolhaPrincipal == 'b':
        menuListar()

    if escolhaPrincipal =='d':
        menuLinha()

    if escolhaPrincipal =='e':
        menuPesquisa()
                
    elif escolhaPrincipal == 'x':
        print('A sair')
        
    else :
        print('Opção invalida')
                
            





