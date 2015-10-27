#from random import randint
import random
#import time

tamanhos=[]


file = "Battleship_tamanhos.txt"
abrir = open(file,encoding="utf-8",mode="r")
ler = abrir.readlines()

#tamanhos =[1,2,3]


for i in ler:
    x = i.strip()
    if ler != "":
        tamanhos.append(int(x))

board = [] #cria um tabuleiro

print(tamanhos)
for x in range(6): #define o tamanho do tabuleiro
    board.append(["/"] * 6)

def print_board(board): #elimina aspas do tabuleiro 
    for row in board:
        print (" ".join(row))

print ("Almirante, vamos afundar navios!")

print_board(board)

def posnav(nav):
    i=0
    col = 0
    lin = 0
    a=0
    b=0
    c=0
    i = random.randint(0,1)
    if i== 0:
        col =random.randint(0,5) # randomiza a coluna do navio
        lin =random.randint(0,6-nav) # randomiza a posição inicial da linha referente ao tamanho do navio
        #vertical
        a = (lin,col) # para navios de tamanho 1
        if nav >1: # para navios de tamanho 2
            b=(lin+1,col)
        if nav ==3: # para navios de tamanho 3
            c=(lin+2,col)
    
    else:
        lin =random.randint(0,5) # randomiza uma linha para o navios
        col =random.randint(0,6-nav) # randomiza a posição inicial do navio em uma coluna referente 
        
        #horizontal
      
        a = (lin,col) # para navios com tamanho 1
        if nav >1: # para navios com tamanho 2
          b=(lin,col+1)
        if nav ==3: # para navios com tamanho 3
          c=(lin,col+2)
    return(a,b,c)
    


subm = posnav(tamanhos[0]) #submarino
fra = posnav(tamanhos[1]) #fragata
dest= posnav(tamanhos[2]) #destroyer


contax = 0 # contador de acertos
contam = 0 # contador de erros
contador_pontos = 0 #conta os pontos baseado no tamanho dos navios
test=0
rodada = 0 #conta as rodadas

while True:
    print("Voce ja acertou:",contax)
    print("Voce ja errou:",contam)
    print("Pontos:", contador_pontos)    
    #print(subm)
    
    
    frota = [subm, fra, dest] # lista com a frota, valores previamente estabelecidos

    rodada += 1 #adiciona 1 para cada loop
    
    print ("Rodada:", rodada)
    guess_row = int(input("Linha:")) # input do jogador quanto a linha
    guess_col = int(input("Coluna:")) # input do jogador quanto a coluna
    
    chute=(guess_row,guess_col) #define chute como o conjunto de inputs do usuario
    #print(chute)
    #print(contax)

    print (frota)    

    test =0
    for i in frota:
        for p in i:
            if p == chute :
                test =1
    
    if test ==1:
        
        board[guess_row][guess_col] = "X" # verifica se o jogador acertou o navio
        print ("Parabens, vc acertou um navio!")
        contax += 1 # conta o numero de acertos
        '''if i == board[guess_row][guess_col]:
            for i in tamanhos:
                contador_pontos += i
        '''
        
    
    if board[guess_row][guess_col] == "X":
        contax -=1
        print ("Voce já escolheu essa posição!")
                          
    else:
        
        if (guess_row < 0 or guess_row > 6) or (guess_col < 0 or guess_col > 6): # verifica se o input do usuário está no range da matriz
            print ("Essa posição não está no oceano!")

        elif (board[guess_row][guess_col] == "X") or (board[guess_row][guess_col] == "O"): # verifica se o jogador já escolheu uma posição
            print ("Voce já escolheu está posição!")
            #2contax -= 1
            
        else: # verifica se o jogador errou a posição do navio
            print ("Voce errou!")
            board[guess_row][guess_col] = "O"
            contam += 1

    print_board(board)
                  

    if contax == 6: # conta se o jogador acertou o numero total de posiçõess de navios, e sai do loop
        print (print_board)
        print ("Vc venceu!")
        break



    
    