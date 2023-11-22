# list-список

# list(список)— это изменяемая коллекция объектов свободного типа в Python.
# (аналогично массиву, но типы могут быть разными). Чтобы использовать списки
# должно быть сделано. Как мы уже упоминали, список — это упорядоченный и изменяемый список. Список другой
# могут быть созданы с использованием подходов. Создадим его с помощью квадратных скобок:

# # 1-пример
# a= ["Audi", "Mustang", "Ferrari","BWE"]
# print(a)

# # py list-список.py --> ['Audi', 'Mustang', 'Ferrari', 'BWE']

# # 2-пример
# #index->
# #      |         |         |        |
# #      0         1         2        3
##Минус -4        -3        -2       -1
# a= ["Audi", "Mustang", "Ferrari","BWE"]
# print(a[0]) # Audi
# print(a[1]) #Mustang
# print(a[2]) #Ferrari
# print(a[3]) #BWE
## Минус index
# print(a[-4]) # Audi
# print(a[-3]) #Mustang
# print(a[-2]) #Ferrari
# print(a[-1]) #BWE

# ---------------------------------

# #for and list
## 1-пример

# miva=["Anor","Banan","Uzim"]

# for x in miva:
#     print(x)


## 2-пример
# miva=["Anor", 200,"Banan",300,"Uzim",500]

# for x in miva:
#     print(x)


## 2-пример
# meva = ["olma", "banan", "apelsin", "nok", "uzum"]
# if "nok" in meva:
#  print("Да, есть")
# else:
#  print("нет такого фрукта")


# list-method

# List.append(x) -Добавить элемент из конца списка
# List.extend(L)-Добавить все элементы в конец списка расширяется.
# List.insert(i,x) -Вставляет значение x в i-й элемент
# List.remove(x)-Удаляет элемент со значением x из списка.
# List.pop([i])-Удаляет и возвращает i-й элемент списка. Если индекс если не указано, последний элемент будет удален
# List.index(x,[start],[end]) -Первый элемент от начала до конца равен значению x возвращает
# List.count(x) -Возвращает количество элементов, равное значению x
# List.sort([key=funksiya]) -Сортирует список на основе функции
# List.reverse()-Открывает список
# List.copy() -Копирует список
# List.clear() -Очищает список

# # 1-len(L)
# m = ["olma", "banan", "apelsin", "nok", "uzum"]
# print(len(m)) 

# #  2-append(x)
# m= ["olma", "banan", "apelsin", "nok", "uzum"]
# m.append("bexi")                                         |
# print(m) #['olma', 'banan', 'apelsin', 'nok', 'uzum', 'bexi']

# #  3-insert(x)
# m= ["olma", "banan", "apelsin", "nok", "uzum"]
# m.insert(0,"bexi")
# #               |
# print(m) #['bexi','olma', 'banan', 'apelsin', 'nok', 'uzum']

# #  4-remove(x)
# m = ["olma", "banan", "apelsin", "nok", "uzum"]
# m.remove("banan")
# print(m) #['olma', 'apelsin', 'nok', 'uzum']

# #  5-remove(x)
# m = ["olma", "banan", "apelsin", "nok", "uzum"]
# m.pop(2)
# print(m) #['olma', 'banan', 'nok', 'uzum']
## 6-del 
# meva = ["olma", "banan", "apelsin", "nok", "uzum"]
# del meva[1]
# print(meva)
# del meva[:]
# print(meva)