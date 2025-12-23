import random

print("=" * 50)
print("ЗАДАНИЕ 1: ВЕКТОРНОЕ ПРОИЗВЕДЕНИЕ")
print("=" * 50)

print("\nВведите 6 чисел - координаты двух векторов (x1 y1 z1 x2 y2 z2):")
coords = list(map(float, input().split()))

x1, y1, z1, x2, y2, z2 = coords

i = y1 * z2 - z1 * y2
j = z1 * x2 - x1 * z2
k = x1 * y2 - y1 * x2

result = [i, j, k]
print(f"\nВекторное произведение: {result}")

print("\n" + "=" * 50)
print("ЗАДАНИЕ 2: ИГРА НА СУММУ")
print("=" * 50)

n = random.randint(10, 100)
k = random.randint(2, 6)

print(f"\nЧисло: {n}")
print(f"Количество чисел: {k}")
print(f"Введите {k} РАЗНЫХ чисел, сумма которых равна {n}:")

numbers = list(map(float, input().split()))

if len(numbers) != k:
    print("Ты проиграл! Количество чисел не совпадает!")
elif len(numbers) != len(set(numbers)):
    print("Ты проиграл! Есть одинаковые числа!")
elif sum(numbers) == n:
    print("Ты выиграл! Правильно!")
else:
    print(f"Ты проиграл! Сумма равна {sum(numbers)}, а должна быть {n}!")