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
            # print(f"длина текста {len(txt)}")
            # print(i)
            if txt[i]=='|':
                # print(f"номер i = {i}")
                string_move=txt[:i]
                # print(f"Текст для разбора: {string_move}")
                index = string_move.find("х", 0,len(string_move))
                # print(f"x расположен на позиции: {index}")
                count=int(string_move[:index])
                # print(f"множитель равен: {count}")
                data=data+(string_move[index+1:])*count
                # print(count)
                # print(data)
                txt=txt[i+1:]
                # print(f"длина остатка текста: {len(txt)}")
                # print(f"Новый текст для разбора {txt}")
                i=0
            else:
                i=i+1

        return(data)


s = str(input("введите текста для кодировки: "))
a=code(s)
print(f"кодировка {a}")

b=decode(a,"")
print(f"расшифровка {b}")
