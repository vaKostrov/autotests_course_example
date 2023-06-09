# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

# Здесь пишем код

with open("test_file/task_3.txt", 'r', encoding='utf-8') as file:
    list_sum = [0]
    for i in file:
        if i == "\n":
            list_sum.append(0)
        else:
            list_sum[-1] += int(i.rstrip("\n"))
    list_sum.sort(reverse=True)
    three_most_expensive_purchases = sum(list_sum[0:3])
    print(three_most_expensive_purchases)

assert three_most_expensive_purchases == 202346
