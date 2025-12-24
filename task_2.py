import random
def task1():
    def cross_product(v1, v2):
        x = v1[1] * v2[2] - v1[2] * v2[1]
        y = v1[2] * v2[0] - v1[0] * v2[2]
        z = v1[0] * v2[1] - v1[1] * v2[0]
        return [x, y, z]
    
    print("Введите 6 чисел - координаты двух векторов")
    num1 = float(input("Число 1: "))
    num2 = float(input("Число 2: "))
    num3 = float(input("Число 3: "))
    num4 = float(input("Число 4: "))
    num5 = float(input("Число 5: "))
    num6 = float(input("Число 6: "))
    
    v1 = [num1, num2, num3]
    v2 = [num4, num5, num6]
    
    result = cross_product(v1, v2)
    print("Результат:", result)


def task2():
    n = random.randint(10, 100)
    k = random.randint(2, 7)
    
    print(f"Сумма должна быть: {n}")
    print(f"Введи {k} разных чисел")
    
    numbers = []
    for i in range(k):
        num = float(input(f"Число {i+1}: "))
        numbers.append(num)
    
    print(f"Твои числа: {numbers}")
    
    if len(numbers) != len(set(numbers)):
        print("Ты проиграл! Есть повторяющиеся числа!")
    elif sum(numbers) == n:
        print("Ты выиграл! Сумма правильная!")
    else:
        print(f"Ты проиграл! Сумма равна {sum(numbers)}, а нужно {n}")
