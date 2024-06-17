lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
lst = filter(lambda lst: lst <= 30, lst)
print(list(lst))
lst = filter(lambda lst: lst % 3, lst)
print(list(lst))
