"""В ответе напишите “Парам пам-пам”, если с ритмом все в порядке 
и “Пам парам”, если с ритмом все не в порядке
*Пример:*

**Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
    **Вывод:** Парам пам-пам  """
# str = input('Введите стихотворение: ')
str = 'пара-ра-рам рам-пам-папам па-ра-па-да '
str = str.split()
print(str)
count = 0
array_a = []
for i in range(len(str)):
    dic = str[i]
    for x in dic:
        if x == 'а':
            count += 1
    array_a.append(count)
print(array_a)
if len(array_a) > 1:
    for i in range(len(array_a)):
        for j in range(i + 1,len(array_a)):
            if array_a[i] * 2 == array_a[j]:
                print('Парам пам-пам')
            else:
                print('Пам парам')
            
            
else:
    print('фраза состоит из одного слова')


"""Напишите функцию 
print_operation_table(operation, num_rows=6, num_columns=6), 
которая принимает в качестве аргумента функцию, вычисляющую элемент
по номеру строки и столбца. Аргументы num_rows и num_columns указывают
число строк и столбцов таблицы, которые должны быть распечатаны. 
Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). 
Примечание: бинарной операцией называется любая операция, у которой 
ровно два аргумента, как, например, у операции умножения."""

num_rows = int(input('Введите кол-во строк: '))
num_columns = int(input('Введите кол-во столбцов: '))
list = []
count = 1
def print_operation_table(num_rows, num_columns):
    for i in range(1, num_columns + 1):
        list = []
        for x in range(count, num_rows + 1):
            g = i * x
            list.append(g)
        print(*list)
        
print_operation_table(num_rows, num_columns)
