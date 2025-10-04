#1. Список возведения в квадрат
kvadrat = [x**2 for x in range(1, 11)]
print(kvadrat)


#2. все четные числа
chet = [x for x in range(1, 20) if x % 2 == 0]
print(chet)

#3. Все слова длиннее трех символов
words = ["python", "Java", "c++", "Rust", "go"]
result = [word.upper() for word in words if len(word) > 3]
print(result)