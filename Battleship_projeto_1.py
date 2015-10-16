from random import randint
import random
import time

board = []


for x in range(6): #cria o tamanho do tabuleiro
    board.append(["/"] * 6)

def print_board(board): #elimina aspas do tabuleiro 
    for row in board:
        print (" ".join(row))

print ("Let's play Battleship!")
print_board(board)

'''
def random_row(board): #randomiza uma posição de linha
    return randint(0, len(board[2]) - 1)

def random_col(board): #randomiza coluna
    return randint(0, len(board[1]) - 2)
'''


def posnav(nav):
    i=0
    col = 0
    lin = 0
    a=0
    b=0
    c=0
    i = random.randint(0,1)
    if i== 0:
        col =random.randint(0,5)
        lin =random.randint(0,6-nav)
        #vertical
        a = (lin,col)
        if nav >1:
            b=(lin+1,col)
        if nav ==3:
            c=(lin+2,col)
    
    else:
        lin =random.randint(0,5)
        col =random.randint(0,6-nav)
        
        #horizontal
        a = (lin,col) # para navios com tamanho 1
                        
        if nav >1: # para navios com tamanho 2
            b=(lin,col+1)
        if nav ==3: # para navios com tamanho 3
            c=(lin,col+2)
    
    
  
    
    
    return(a,b,c)
    










#ship_row = random_row(board)
#ship_col = random_col(board)
#print (ship_row)
#print (ship_col)
#print (sub_row)
#print (sub_col)

subm = posnav(1) #submarino
fra = posnav(3) #fragata
dest= posnav(2) #destroyer
 
contax = 0
contam = 0

while True:
    print(subm)
    
    
    frota = [subm, fra, dest]    
        
    
    
    
    test=0
    
    print ("Rodada:", +1)
    guess_row = int(input("Guess Row:"))
    guess_col = int(input("Guess Col:"))
    
    chute=(guess_row,guess_col)    
    print(chute)
    print(contax)
    for i in frota:
        
        
        for x in i:
              
            if x == chute :
                test =1
    if test ==1:
        
        board[guess_row][guess_col] = "X" 
        contax = contax +1
                          
    else:
        
        if (guess_row < 0 or guess_row > 6) or (guess_col < 0 or guess_col > 6):
            print ("Oops, that's not even in the ocean.")
        elif(board[guess_row][guess_col] == "X") or (board[guess_row][guess_col] == "O"):
            print ("You guessed that one already.")
        else:
            print ("You missed my battleship!")
            board[guess_row][guess_col] = "O"
            contam += 1

                  
              
    if contax == 6:
        print ("Vc venceu")
        break
               

    
#    if battleships[ship_row][ship_col] == "X"
            
    
    print_board(board)