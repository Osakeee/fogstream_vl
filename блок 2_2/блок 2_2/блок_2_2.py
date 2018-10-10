"""Дана строка. Разрежьте ее на две равные части (если длина строки — четная, а если длина строки нечетная, то длина первой
части должна быть на один символ больше). Переставьте эти две части местами, результат запишите в новую строку и выведите на
экран."""
first=str()
second=str()

stroka=input()
if len(stroka)%2==0:
   # print('dadaya')
    first=stroka[0:len(stroka)//2]
    second=stroka[len(stroka)//2:]
    print(second+first)
if len(stroka)%2!=0:
    #print('dadaya')
    first=stroka[0:len(stroka)//2+1]
    second=stroka[len(stroka)//2+1:]
    print(second+first)