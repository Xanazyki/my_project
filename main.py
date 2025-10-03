import random
from collections import Counter

numbers = [random.randint(1, 10) for _ in range(20)]
unique_numbers = list(set(numbers))
print(f"1. Исходный список: {numbers}")
print(f"   Уникальные значения: {unique_numbers}")

print("\n" + "="*50 + "\n")

frequency_dict = {}
for num in numbers:
    frequency_dict[num] = frequency_dict.get(num, 0) + 1
unique_dict = {num: count for num, count in frequency_dict.items() if count == 1}
print(f"Уникальные элементы: {unique_dict}")

print("\n" + "="*50 + "\n")

words = ["перпендикулярность", "Дом", "Ведьма", "Семья", "Курица", "Питон", "Телефон"]
long_words = {word for word in words if len(word) > 5}
print(f"3. Список слов: {words}")
print(f"   Слова длиннее 5 символов: {long_words}")

print("\n" + "="*50 + "\n")

sentence = input("4. Введите предложение: ").lower()
word_count = {}
for word in sentence.split():
    word_count[word] = word_count.get(word, 0) + 1
print(f"   Количество вхождений слов: {word_count}")

print("\n" + "="*50 + "\n")

numbers_with_duplicates = [1, 1, 1, 2, 3, 4, 4, 4, 6]
unique_list = list(set(numbers_with_duplicates))
print(f"5. Исходный список: {numbers_with_duplicates}")
print(f"   Без дубликатов: {unique_list}")

print("\n" + "="*50 + "\n")

products = {"яблоко": 60, "арбуз": 90, "мандарин": 40, "помела": 150}
most_expensive = max(products, key=products.get)
print(f"6. Товары и цены: {products}")
print(f"   Самый дорогой товар: '{most_expensive}' за {products[most_expensive]} руб.")

print("\n" + "="*50 + "\n")

names = ["Анна", "Михаил", "Мария", "Михаил", "Сергей", "Анна", "Михаил", "Сергей"]
name_count = Counter(names)
repeated_names = [name for name, count in name_count.items() if count > 1]
most_common = name_count.most_common(1)[0]

print(f"7. Список имён: {names}")
print(f"   Имена, встречающиеся более 1 раза: {repeated_names}")
print(f"   Самое частое имя: '{most_common[0]}' ({most_common[1]} раз)")

print("\n" + "="*50 + "\n")

text = input("8. Введите строку: ")
first_occurrence = {}
for index, char in enumerate(text):
    if char not in first_occurrence:
        first_occurrence[char] = index
print(f"   Первые вхождения символов: {first_occurrence}")
