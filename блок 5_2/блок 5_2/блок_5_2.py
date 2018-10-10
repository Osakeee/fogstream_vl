"""Дан файл. Определите сколько в нем букв (латинского алфавита), слов, строк. Выведите три найденных числа в формате, приведенном в примере"""

kline=int(0)
kwords=int(0)
kletter=int(0)

file = open('textik.txt','r')
for line in file:
    kletter=kletter+len(line)
    kline=kline+1
    kwords=kwords+(line.count(' '))+1
    print(kwords)
file.close()
print('количество строк: ',kline)
print('количество слов',kwords)
print('количество букв',kletter)