def printboard(xst,yst):
    zero='X' if xst[0] else ('0' if yst[0] else 0)
    one='X' if xst[1] else ('0' if yst[1] else 1)
    two='X' if xst[2] else ('0' if yst[2] else 2)
    three='X' if xst[3] else ('0' if yst[3] else 3)
    four='X' if xst[4] else ('0' if yst[4] else 4)
    five='X' if xst[5] else ('0' if yst[5] else 5)
    six='X' if xst[6] else ('0' if yst[6] else 6)
    seven='X' if xst[7] else ('0' if yst[7] else 7)
    eight='X' if xst[8] else ('0' if yst[8] else 8)
    print(f" {zero} | {one} | {two} ")
    print(f" --|---|--")
    print(f" {three} | {four} | {five} ")
    print(f" --|---|--")
    print(f" {six} | {seven} | {eight} ")
    print(f" --|---|--")
    
def sum(a,b,c):
    return a+b+c

def win(xst,yst):
    wins=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in wins:
        if(sum(xst[win[0]],xst[win[1]],xst[win[2]])==3):
            return 1
        if(sum(yst[win[0]],yst[win[1]],yst[win[2]])==3):
            return 0
    return -1
        
if __name__ =="__main__":
    cont=1
    while(cont==1):
        xst=[0,0,0,0,0,0,0,0,0]
        yst=[0,0,0,0,0,0,0,0,0]
        turn=1
        print("welcome To TIC TAC TOA Game")
        while(True):
            printboard(xst,yst)
            if(turn==1):
                print("X's Chance")
                val=int(input("Enter your choice field: "))
                xst[val]=1
            else:
                print("O's Chance")
                val=int(input("Enter your choice field: "))
                yst[val]=1
            ch=win(xst,yst)
            if(ch==1):
                printboard(xst,yst)
                print("X wins")
                print("Game Over!")
                break
            if(ch==0):
                printboard(xst,yst)
                print("O wins")
                print("Game Over!")
                break
            turn= 1-turn
        cont=int(input("Play again?(1/0): "))
    print("Thanks for playing MY GAME")