# Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его 
# кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух 
# считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения 
# одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются 
# дефисами. Фразы отделяются друг от друга пробелами. Стихотворение Винни-Пух вбивает в программу 
# с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если 
# с ритмом все не в порядке 
# Ввод: пара-ра-рам рам-пам-папам па-ра-па-дам    Вывод: Парам пам-пам

stryng = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
text = stryng.split()
listRes = []
for word in text:
    sumVowels = 0
    for i in word:
        if i in 'аеиоуыэюя':
            sumVowels += 1
    listRes.append(sumVowels)
    
def comparison(listRes):
    for i in range (len(listRes)-1):
        if listRes[len(listRes)] == listRes[i]:
            return listRes
print(comparison(listRes))

# def searchVowels(str):
#     str = stryng.split()
#     listRes = []
#     for word in str:
#         sumVowels = 0
#         for i in word:
#             if i in 'аеиоуыэюя': 
#                 sumVowels += 1
#         listRes.append(searchVowels)               
#     return len(listRes) == listRes.count(listRes[0])

# if searchVowels(stryng):
#     print('Парам пам-пам')
# else:
#     print('Пам парам')



# myDict = {1:'а', 2:'е', 3:'о'}
# for i, v in myDict.items():
#     if v in myString:
#         print(v)
#     if myString.count(item) == 'а':
#         myList.append(myString.count(item) == 'а')
# print(myList)

