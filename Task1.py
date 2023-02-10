n = int(input('Введите кол-во элементов первого массива: '))
m = int(input('Введите кол-во элементов второго массива: '))
list_n = list()
list_m = list()
for i in range(n):
    list_n.append(int(input('N --> ')))
for i in range(m):
    list_m.append(int(input('M --> ')))
list_merge = list(set(list_n) & set(list_m))
print(sorted(list_merge))