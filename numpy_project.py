import numpy as np 

board=np.zeros((3,3),dtype=int) # ye board ka bass create kiya hai ye print karega 3x3 matix zero kin 

print(board)

# aab terminal me ek X or O board chahiye to ek small helper function create karege 
def print_board(b):
    symbols={0:' ',1:'X',-1:'O'}
    for r in range(3):
            row=" | ".join(symbols[val] for val in b[r])
            print(" "+row)
            if r<2:
                print("---+---+---")
    print()

def check_winner(b):
    if 3 in np.sum(b,axis=1) or 3 in np.sum(b,axis=0):
        return "X"
    if -3 in np.sum(b,axis=1) or -3 in np.sum(b,axis=0):
        return "O"
    if np.trace(b)==3 or np.trace(np.fliplr(b))==3: 
        return "X"
    if np.trace(b)==-3 or np.trace(np.fliplr(b))==-3:
        return "O"
    if not 0 in b:
        return "Draw"
    return None

current=1# current player ko track karne ke liye 1 for X and -1 for O

print("Welcome to Tic Tac Tow")

print_board(board)

while True:
    if current==1:
         Player="X"
    else:
        Player="O"
        
    try:
        row=int(input(Player+"Enter row (0,1,2)"))
        col=int(input(Player+"Enter column (0,1,2)"))
        
    except ValueError:
        print("Please enter a number only \n")
        continue

    if row<0 or row>2 or col<0 or col>2:
        print("Row and column must be between 0 and 2")
        continue
    
    if board[row,col]!=0:
        print("Cell is already occupied, choose another cell")
        
    board[row,col]=current
    print_board(board)
    
    result=check_winner(board)
    
    if result is not None:
        if result=="Draw":
            print("Ohh! its a Draw")
        else:
            print(result,"Wins")
        
        break
    
    if current==1:
        current=-1
    else:
        current=1