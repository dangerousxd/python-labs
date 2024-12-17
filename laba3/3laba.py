"""Написать программу, которая читая символы из бесконечной последовательности (эмулируется конечным файлом)
, распознает, преобразует и выводит на экран объекты по определенному правилу. Объекты разделены пробелами.
 Преобразование делать по возможности через словарь. Для упрощения под выводом числа прописью подразумевается
 последовательный вывод всех цифр числа. Регулярные выражения использовать нельзя."""

"""Целые четные числа, начинающиеся с 9. Для каждого числа повторяющиеся цифры вывести прописью."""


def number_to_words(digit):
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
        digit_count[digit] = digit_count.get(digit, 0) + 1
    return digit_count

def process_number(num):

    digit_count = get_digit_counts(num)
    words_representation = []

    for digit in str(num):
        count = digit_count[digit]
        if count > 1:
            words_representation.append(number_to_words(digit))
        else:
            words_representation.append(digit)
            digit_count[digit] = 0

    return ''.join(words_representation)

def process_numbers(input_data):

    results = []
    numbers = input_data.split()
    for num_str in numbers:
        if num_str.isdigit():
            num = int(num_str)
            if num % 2 == 0 and str(num).startswith('9'):
                words_representation = process_number(num)
                results.append(f"{num}: {words_representation}")
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
