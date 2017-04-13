t=['0','1','2','3','4','5','6','7','8']
winc=(('0','1','2'),('3','4','5'),('6','7','8'),('0','3','6'),('1','4','7'),('2','5','8'),('0','4','8'),('2','4','6'))
x=dict()
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
disp()
print('player-1: 1 and player-2: 0')
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
