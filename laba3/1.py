#1. Список возведения в квадрат
kvadrat = [x**2 for x in range(1, 11)]
print(kvadrat)


#2. все четные числа
print('/n')
chet = [x for x in range(1, 20) if x % 2 == 0]
print(chet)


#3. Все слова длиннее трех символов
print('/n')
words = ["python", "Java", "c++", "Rust", "go"]
result = [word.upper() for word in words if len(word) > 3]
print(result)


#4. Класс-итератор, обратное возвращение
print('/n')
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

n = int(input("Введите число n: "))
for x in Countdown(n):
    print(x)


#5. негеработ Финаччи
print('/n')
def fibonacci(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

n = int(input("Введите число n: "))
print(f"Первые {n} чисел Фибоначчи:")
for num in fibonacci(n):
    print(num)


#6. Калькулятор вклада
print('/n')
from decimal import Decimal

def deposit_calculator():
    nach = Decimal(input("Начальная сумма (рубли.копейки): "))
    stavka = Decimal(input("Процентная ставка (например, 12.5): "))
    srok = Decimal(input("Срок в годах (в годах): "))
    
    monthly_rate = stavka / (Decimal('12') * Decimal('100'))
    months = Decimal('12') * srok
    itog = nach * (Decimal('1') + monthly_rate) ** months
    itog = itog.quantize(Decimal('0.01'))
    
    profit = itog - nach
    print('\n')
    print(f"Итоговая сумма: {itog} руб.")
    print(f"Общая прибыль: {profit} руб.")

deposit_calculator()


#7. Калькулятор дробей
print('/n')
from fractions import Fraction

frac1 = Fraction(3, 4)
frac2 = Fraction(5, 6)

print(f"Первая дробь: {frac1}")
print(f"Вторая дробь: {frac2}")

sum = frac1 + frac2
vich = frac1 - frac2
umn = frac1 * frac2
delit = frac1 / frac2

print(f"Сложение: {frac1} + {frac2} = {sum}")
print(f"Вычитание: {frac1} - {frac2} = {vich}")
print(f"Умножение: {frac1} * {frac2} = {umn}")
print(f"Деление: {frac1} / {frac2} = {delit}")


#8. Дата
print('/n')
from datetime import datetime

data_time = datetime.now()

print(f"Текущая дата и время: {data_time}")
print(f"Текущая дата: {data_time.date()}")
print(f"Текущее время: {data_time.time()}")


#9. Расчет дат
print('/n')
from datetime import datetime, date

birthday = date(2005, 7, 27)
today = date.today()

print(f"Дата рождения: {birthday}")
print(f"Сегодняшняя дата: {today}")

proshlo = (today - birthday).days
print(f"Дней прошло с момента рождения: {proshlo}")

next_birthday = date(today.year, birthday.month, birthday.day)
if next_birthday < today:
    next_birthday = date(today.year + 1, birthday.month, birthday.day)
days_to_next_birthday = (next_birthday - today).days

print(f"Следующий день рождения: {next_birthday}")
print(f"Дней до следующего дня рождения: {days_to_next_birthday}")


#10. Строка с Date
print('/n')
from datetime import datetime

current_datetime = datetime.now()

def format_datetime_ru(dt):
    months = {
        1: 'января', 
        2: 'февраля', 
        3: 'марта', 
        4: 'апреля',
        5: 'мая', 
        6: 'июня', 
        7: 'июля', 
        8: 'августа',
        9: 'сентября', 
        10: 'октября', 
        11: 'ноября', 
        12: 'декабря'
    }
    
    formatted = f"Сегодня {dt.day} {months[dt.month]} {dt.year} года, время: {dt:%H:%M}"
    
    return formatted

print(format_datetime_ru(current_datetime))