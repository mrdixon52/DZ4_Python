import random
n = int(input('Введите число кустов: '))
gryadka = list()
for i in range(n):
    gryadka.append(random.randint(1,9))
print(gryadka)
if n == 3:
    max = gryadka[0] + gryadka[1] + gryadka[2]
else:
    sum1 = gryadka[n - 1] + gryadka[n - 2] + gryadka[0]
    sum2 = gryadka[n - 1] + gryadka[0] + gryadka[1]
    max = gryadka[0] + gryadka[1] + gryadka[2]
    for i in range(3, len(gryadka)):
        if max < gryadka[i] + gryadka[i - 1] + gryadka[i - 2]:
            max = gryadka[i] + gryadka[i - 1] + gryadka[i - 2]
    if sum1 > max > sum2:
        max = sum1
    elif sum2 > max > sum1:
        max = sum2
print(max)