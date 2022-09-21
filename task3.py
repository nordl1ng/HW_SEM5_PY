# Создайте программу для игры в ""Крестики-нолики"".

def print_list(mas):
    for i in range (len(mas)):
        for k in range (len(mas)):
            print((mas[i][k]),end=" ")
        print("")

def player_number(move):
    if move ==-1:
        player = 1
    else:
        player = 2
    return player

def check(listt):
    a=bool()
    a= ((listt[0][0] == listt[0][1] == listt[0][2] !="_")
    or (listt[1][0] == listt[1][1] == listt[1][2] !="_")
    or (listt[2][0] == listt[2][1] == listt[2][2] !="_")
    or(listt[0][0] == listt[1][0] == listt[2][0] !="_")
    or(listt[0][1] == listt[1][1] == listt[2][1] !="_")
    or(listt[0][2] == listt[1][2] == listt[2][2] !="_")
    or(listt[0][0] == listt[1][1] == listt[2][2] !="_")
    or(listt[0][2] == listt[1][1] == listt[2][0] !="_"))
    return(a)

def XO_enter (move,i,j,list):
    if move ==-1:
        list[i][j]= "X"
    else:
        list[i][j]= "O"
    return list[i][j]

listt = [["_","_","_"],['_','_','_'],['_', '_', '_']]
print_list(listt)
import random
move = random.choice([-1,1])

print(f"Первый ход за игроком {player_number(move)}")

count = 0
while (check(listt) == 0 and count <9):
    xo = lambda move : "X" if move==-1 else "O"
    print(f"игрок {player_number(move)} введите {xo(move)}")
    i = int(input("Ввведите i - (строка поля): "))
    j = int(input("Ввведите j - (стобец поля): "))
    XO_enter (move,i,j,listt)
    move = move*-1
    print("________")
    print_list(listt)
    count +=1

if (check(listt) == 1):
    move = move*-1
    print(f"Победил игрок {player_number(move)}")
else:
    print("Ничья")

    
