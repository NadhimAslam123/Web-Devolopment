import random
from colorama import Fore , Style , init
init (autoreset=True)
def show(b):
    c = lambda x:(Fore.RED if x=='X'else Fore.BLUE if x=='O'else Fore.YELLOW)+x
    +Style.RESET_ALL
    print(f"{c(b[0])}|{c(b[1])}|{c(b[2])}\n-+-+-\n{c(b[3])}|{c(b[4])}|{c(b[5])}|\n-+-+-\n{c(b[6])}|{c(b[7])}|{c(b[8])}|")
def win (b,s): return any (b[a]==b[b1]==b[c]s for a,b1,c in [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(2,4,6)])
def full(b): return all(not x.isdigit() for x in b)
def move(b,s):
    while True:
        m=input("Move (1-9): ")
        if m.isdigit() and b[int(m)-1].isdigit(): b[int(m)-1]=s; break
        print("Invalid!")

    def ai(b,a,p):
        for s in [a,p]:
            for i in range(9):
              if b[i].isdigit():
                t=b.copy(); t[i]=s
                if win(t,s): b[i]=a; return
b[random.choice([i for i in range])]                               
                    