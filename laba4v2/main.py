"""Написать программу, которая читая символы из файла, распознает, преобразует и выводит на экран объекты по определенному правилу.
 Объекты разделены пробелами. Распознавание и преобразование делать по возможности через регулярные выражения.
  Для упрощения под выводом числа прописью подразумевается последовательный вывод всех цифр числа."""

"""Целые четные числа, начинающиеся с 9. Для каждого числа повторяющиеся цифры вывести прописью."""
import re

def number_to_words(digit):
    """Функция преобразует цифру в слово."""
    words_dict = {
        '0': 'ноль',
        '1': 'один',
        '2': 'два',
        '3': 'три',
        '4': 'четыре',
        '5': 'пять',
        '6': 'шесть',
        '7': 'семь',
        '8': 'восемь',
        '9': 'девять'
    }
    return words_dict.get(digit, '')

def get_digit_counts(number):
    digit_count = {}
    for digit in str(number):
        if digit.isdigit():
            digit_count[digit] = digit_count.get(digit, 0) + 1
    return digit_count

def process_numbers(input_data):
    results = []

    pattern = re.compile(r'-?9\d*[02468]')

    numbers = input_data.split()

    for num_str in numbers:
        if pattern.fullmatch(num_str):
            digit_count = get_digit_counts(num_str)
            words_representation = []

            for digit in num_str:
                if digit == '-':
                    words_representation.append('-')
                elif digit_count[digit] > 1:
                    words_representation.append(number_to_words(digit))
                else:
                    words_representation.append(digit)

            results.append(f"{num_str}: {''.join(words_representation)}")

    return results

try:
    with open('file', 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                results = process_numbers(line)
                for result in results:
                    print(result)
except FileNotFoundError:
    print("Файл не найден.")
except Exception as e:
    print(f"Ошибка при чтении файла: {e}")
