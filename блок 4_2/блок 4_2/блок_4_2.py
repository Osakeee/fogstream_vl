"""Дан список результатов попыток одного спортсмена для некоторого соревнования. Написать функцию, которая считает сколько
за сессию был установлен новый рекорд, т.е. текущее значение превышает значение максимального"""
def poschitaem(spisochek):
    max=int(0)
    kol=int(0)

    for i in range(len(spis)):
        if i==0:
            max=spis[0]
        if max<spis[i]:
            max=spis[i]
            kol=kol+1
        i=i+1
    print(kol)

spis=[10,22,20,29,19,30,15,35]
poschitaem(spis)