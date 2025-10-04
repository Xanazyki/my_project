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

#4. Класс-итератор, обратное возвращение
class Countdown:
    def __init__(self, n):
        self.n = n
        self.current = n
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < 1:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

n = int(input("Введите число n"))
for x in Countdown(n):
    print(x)

