"""Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента."""

spis=[1,2,3,6,5,8,1,4]
for i in range(len(spis)):
    if i==0:
        continue
    if spis[i-1]<spis[i]:
        print(spis[i])
    i=i+1
