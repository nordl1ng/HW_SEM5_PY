# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
# candy = int(input("Введите количество конфет на столе: "))
def player_number(t,move):
    if t ==0:
        if move ==-1:
            player = 1
        else:
            player = 2
        return player
    if t ==1:
        if move ==-1:
            player = 1
        else:
            player = "bot"
        return player

def enter_control(x):
        candy_for_player = 0
        while not( 0< candy_for_player < 29) or candy_for_player > x:
            candy_for_player = int(input(f"Игрок {player_number(t,move)}, укажите количество конфет, которые хотите взять (до 28): "))
            if candy_for_player > x:
                print(f"Количество должно быть до {x}")
            elif not( 0< candy_for_player < 29):
                print("Количество должно быть до 28")          
        return(candy_for_player)

def bot_control(x):
    b = 0
    if x < 29:
        b = x
    elif x < 57:
        b = x - 29
    while not( 0< b < 29):
        b = random.randint(1, 29)
    return b
t = int(input("Выберите тип игры 0 - человек / человек, 1 - человек/бот: "))

candy = 150
if t == 0:
    import random
    move = random.choice([-1,1])
    print(f"На столе {candy} конфет")
    print(f"Первый ход за игроком {player_number(t,move)}")
    while candy > 0:
        player_number(t,move)
        candy = candy - enter_control(candy)
        print(f"На столе осталось {candy} конфет")
        move = move*-1
    move = move*-1
    print(f"Победил игрок {player_number(t,move)}")

if t == 1:
    import random
    move = random.choice([-1,1])
    print(f"На столе {candy} конфет")
    print(f"Первый ход за игроком {player_number(t,move)}")
    while candy > 0:
        player_number(t,move)
        if player_number(t,move) == 1:
            candy = candy - enter_control(candy)
        else:
            bot = bot_control(candy)
            print(f"Bot забрал {bot} конфет")
            candy = candy - bot
        print(f"На столе осталось {candy} конфет")
        move = move*-1
    move = move*-1
    print(f"Победил игрок {player_number(t,move)}")



 