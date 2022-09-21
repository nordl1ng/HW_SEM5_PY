# # listt = [["X","_","_"],['_','X','_'],['_', '_', 'X']]

# # def print_list(mas):
# #     for i in range (len(mas)):
# #         for k in range (len(mas)):
# #             print((mas[i][k]),end=" ")
# #         print("")

# # print_list(listt)

# # def check(listt):
# #     a=bool()
# #     a= ((listt[0][0] == listt[0][1] == listt[0][2] !="_")
# #     or (listt[1][0] == listt[1][1] == listt[1][2] !="_")
# #     or (listt[2][0] == listt[2][1] == listt[2][2] !="_")
# #     or(listt[0][0] == listt[1][0] == listt[2][0] !="_")
# #     or(listt[0][1] == listt[1][1] == listt[2][1] !="_")
# #     or(listt[0][2] == listt[1][2] == listt[2][2] !="_")
# #     or(listt[0][0] == listt[1][1] == listt[2][2] !="_")
# #     or(listt[0][2] == listt[1][1] == listt[2][0] !="_"))
# #     return(a)

# x = 11
# XO = lambda x : "X" if (x > 10 and x < 20) else "Y"
# print(XO(x))

def enter_control(a):
    x=int(input())
    if x > a:
        print(f"Количество должно быть до {a}")
    else:
        return x

i = print(f"Введите i:") + {enter_control(2)}

    # number = ''
    # listt=[]
    # listt.append([txt.split("|")])
    # print(listt)
    # res = ''
    # for i in range(len(txt)):
    #     if not txt[i].isalpha():
    #         number += txt[i]
    #     else:
    #         res = res + txt[i] * int(number)
    #         number = ''
    # return res