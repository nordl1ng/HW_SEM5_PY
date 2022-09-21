# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def code(data):
    count = 1
    result = ''
    for i in range(len(data)-1):
        if data[i] == data[i+1]:
            count += 1
        else:
            result = result +str(count) + "х"+ data[i] + "|"
            count = 1
    if count > 1 or (data[len(data)-2] != data[-1]):
        result = result + str(count) + "х" + data[-1]+"|"
    return result

def decode(txt,data):
        i=0
        while i < len(txt):
            if txt[i]=='|':
                string_move=txt[:i]
                index = string_move.find("х", 0,len(string_move))
                count=int(string_move[:index])
                data=data+(string_move[index+1:])*count
                txt=txt[i+1:]
                i=0
            else:
                i=i+1

        return(data)


s = str(input("введите текста для кодировки: "))
a=code(s)
print(f"кодировка {a}")

b=decode(a,"")
print(f"расшифровка {b}")
