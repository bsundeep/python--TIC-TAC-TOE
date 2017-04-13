X)# python--TIC-TAC-TOE
TIC-TAC-TOE game is very simple to write in python. All you need is the basic knowledge of python constructs.

// list with 9 elements as tic tac toe game is 3x3 matrix game and require 9 places.
t=['0','1','2','3','4','5','6','7','8']
// tuples to check for the winning conditions.
winc=(('0','1','2'),('3','4','5'),('6','7','8'),('0','3','6'),('1','4','7'),('2','5','8'),('0','4','8'),('2','4','6'))
//declaring x as a dictionary.
x=dict()
//disp() method to display.
def disp():
    c=0
    for i in t:
        if(c==2 or c==5 or c==8):
            print(i,end='\n')
        else:
            print(i,'\t|',end='\t')
        c=c+1
        if (c%3==0 and c!=9):
            print('________','_______________','__________\n')
// win() method to check whether winner or not.
def win():
    for d in winc:
        p1=p2=0
        for f in d:
            try:
                if x[f]=='X':
                    p1=p1+1
                elif x[f]=='O':
                    p2=p2+1
                else:
                    break
            except:
                break
        if p1==3:
            return 'p1'
        elif p2==3:
            return 'p2'
//calling disp() method      
disp()
print('player-1: X and player-2: O')
cnt=1
while cnt<=9:
    if cnt%2:
        print('player1 turn')
        y=str(input())
        try:    
            if t[int(y)]=='X' or t[int(y)]=='O':
                               print('invalid move')
                               continue
            else:
                x[y]=t[int(y)]='X'
        except:
            print('invalid move')
            continue
        
    else:
        print('player2 turn')
        y=str(input())
        try:
            if t[int(y)]=='X' or t[int(y)]=='O':
                               print('invalid move')
                               continue
            else:
                x[y]=t[int(y)]='O'
        except:
            print('invalid move')
            continue
    disp()
    if cnt>4:
        s=win()
        if s=='p1':
            print('player1 won')
            break
        elif s=='p2':
            print('player2 won')
            break
    cnt=cnt+1
if cnt==10:
    print('draw match')
