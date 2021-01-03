filePath = input("Input path: ")
array = []
with open(filePath, "r", encoding='utf-8') as f:
    for string in f.readlines():
        array.append(string.split(","))
for i in range(len(array)-1):
    array[i][3] = array[i][3].rstrip("\n")
while True:
    print("\n")
    print("1. Вивести всю інформацію\n"
          "2. Знайти предмет\n"
          "3. Вийти\n")

    choose = int(input("Виберіть номер:"))
    if choose == 1:
        for item in array:
            print(item)
    elif choose == 2:
        print("Знайти за:\n"
              "1.Назва предмета\n"
              "2.К-ть годин\n"
              "3.Викладач\n"
              "4.Рейтинг\n")
        choose2 = int(input("Виберіть номер:"))
        criteria = input("Введіть значення: ")
        if choose2 == 1:
            for item in array:
                if criteria in item[0]:
                    print(item)
        elif choose2 == 2:
            for item in array:
                if criteria == item[1]:
                    print(item)
        elif choose2 == 3:
            for item in array:
                if criteria in item[2]:
                    print(item)
        elif choose2 == 4:
            for item in array:
                if criteria == item[3]:
                    print(item)
    elif choose==3:
        break
    else: print("Немає такого номеру,повторіть спробу")