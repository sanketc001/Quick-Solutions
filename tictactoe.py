def see(board):
    if(board[6]==board[7] and board[6]==board[8] or board[2]==board[5] and board[2]==board[8] or board[3]==board[4] and board[3]==board[5] or board[2]==board[4] and board[2]==board[6] or board[1]==board[4] and board[1]==board[7] or board[0]==board[1] and board[0]==board[2] or board[0]==board[4] and board[0]==board[8] or board[0]==board[3] and board[0]==board[6]):
        return 1
    else:
        return 0
b=[]
for i in range(9):
    b.append(i)
def printboard(board):
    print(board[0]," | ",board[1]," | ",board[2],"\n",board[3]," | ",board[4]," | ",board[5],"\n",board[6]," | ",board[7]," | ",board[8])
w=0
while w==0:
    i1=int(input("Player 1(O): "))
    if(b[i1]!="X" or b[i1]!="O" and w==0):
        b[i1]="O"
    else:
        print("Invalid input")
    w=see(b)
    printboard(b)
    if(w==1):
        print("Player 1 wins")
        break
    i2=int(input("Player 2(X): "))
    if(b[i2]!="X" or b[i2]!="O" and w==0):
        b[i2]="X"
    else:
        print("Invalid input")
    w=see(b)
    printboard(b)
    if (w == 1):
        print("Player 2 wins")