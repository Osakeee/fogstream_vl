"""Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000,
и возвращающую True, если оно простое, и False - иначе."""

def is_prime(quan):
    if quan == 1:
        return False
    elif quan==2:
        return True
    for i in range(2, quan):
        if quan % i == 0:
            return False
        else:
            return True

print(is_prime(int(input())))


