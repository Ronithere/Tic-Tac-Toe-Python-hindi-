import os    
import time    
    
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '] #board ke andar ki jagah    
player = 1    
   
  
Win = 1    
Draw = -1    
Running = 0    
Stop = 1    
'''''''''''' 
Game = Running    
Mark = 'X'    
     
def Board():    #game ka board banaya
    print(" %c | %c | %c " % (board[1],board[2],board[3]))    
    print("___|___|___")    
    print(" %c | %c | %c " % (board[4],board[5],board[6]))    
    print("___|___|___")    
    print(" %c | %c | %c " % (board[7],board[8],board[9]))    
    print("   |   |   ")    
      
def jagah(x):#yeh dekhta ke jagah khali hai ke nahi andar already  
    if(board[x] == ' '):    
        return True    
    else:    
        return False    
     
def jitega(): #isme dekhege ke jita ke nai koi  
    global Game    
    #horizontal jia ke nai  
    if(board[1] == board[2] and board[2] == board[3] and board[1] != ' '):    
        Game = Win    
    elif(board[4] == board[5] and board[5] == board[6] and board[4] != ' '):    
        Game = Win    
    elif(board[7] == board[8] and board[8] == board[9] and board[7] != ' '):    
        Game = Win    
    #Vertical jita ke nai  
    elif(board[1] == board[4] and board[4] == board[7] and board[1] != ' '):    
        Game = Win    
    elif(board[2] == board[5] and board[5] == board[8] and board[2] != ' '):    
        Game = Win    
    elif(board[3] == board[6] and board[6] == board[9] and board[3] != ' '):    
        Game=Win    
    #Diagonal jita ke nai  
    elif(board[1] == board[5] and board[5] == board[9] and board[5] != ' '):    
        Game = Win    
    elif(board[3] == board[5] and board[5] == board[7] and board[5] != ' '):    
        Game=Win    
    #Match Tie hua ya draw hua woh dekhega  
    elif(board[1]!=' ' and board[2]!=' ' and board[3]!=' ' and board[4]!=' ' and board[5]!=' ' and board[6]!=' ' and board[7]!=' ' and board[8]!=' ' and board[9]!=' '):    
        Game=Draw    
    else:            
        Game=Running    
    
print("Welcome To Tic-Tac-Toei")    
print("Player 1 [X] --- Player 2 [O]\n")    
print()       
print("Wait kar...")    
time.sleep(2)    
while(Game == Running):    
    os.system('cls')    
    Board()    
    if(player % 2 != 0):    
        print("Player 1's khelega")    
        Mark = 'X'    
    else:    
        print("Player 2's khelega")    
        Mark = 'O'    
    choice = int(input("[1-9] ke andar koi bhi position choose karo jaha mark karwana hai:\n "))    
    if(jagah(choice)):    
        board[choice] = Mark    
        player+=1    
        jitega()    
    
os.system('cls')    
Board()    
if(Game==Draw):    
    print("Draw hogya ")    
elif(Game==Win):    
    player-=1    
    if(player%2!=0):    
        print("Player 1 jitgaya")    
    else:    
        print("Player 2 jitgaya") 