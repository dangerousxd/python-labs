"""Задание состоит из двух частей.
1 часть – написать программу в соответствии со своим вариантом задания. Написать 2 варианта формирования
 (алгоритмический и с помощью функций Питона), сравнив по времени их выполнение.
2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение
 на характеристики объектов (которое будет сокращать количество переборов) и целевую функцию для нахождения
 оптимального  решения."""

"""
Две бригады, в первую 3 человека, во вторую 4, всего 7 .
Вывести все возможные варианты"""

from itertools import combinations
import timeit


def manual_partition(group):
    results = []
    n = len(group)

    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                first_team = [group[i], group[j], group[k]]
                remaining1 = [x for x in group if x not in first_team]

                for l1 in range(len(remaining1)):
                    for l2 in range(l1 + 1, len(remaining1)):
                        for l3 in range(l2 + 1, len(remaining1)):
                            second_team = [
                                remaining1[l1], remaining1[l2], remaining1[l3], remaining1[3]
                            ]
                            results.append((first_team, second_team))
    return results


def pythonic_partition(group):
    results = []
    for first_team in combinations(group, 3):
        remaining1 = [x for x in group if x not in first_team]
        for second_team in combinations(remaining1, 4):
            results.append((list(first_team), list(second_team)))
    return results


def objective_function(first_team, second_team):
    return abs(sum(first_team) - sum(second_team))


def pythonic_partition_with_constraints(group, max_first_team_sum):
    results = []
    optimal_result = None
    optimal_difference = float('inf')

    for first_team in combinations(group, 3):
        if sum(first_team) > max_first_team_sum:
            continue

        remaining1 = [x for x in group if x not in first_team]
        for second_team in combinations(remaining1, 4):
            current_difference = objective_function(first_team, second_team)
            results.append((list(first_team), list(second_team)))

            if current_difference < optimal_difference:
                optimal_difference = current_difference
                optimal_result = (list(first_team), list(second_team))

    return results, optimal_result


def main():
    group = list(range(1, 8))
    max_first_team_sum = 10

    print("=== Часть 1: Алгоритмическое решение ===")
    manual_time = timeit.timeit(lambda: manual_partition(group), number=1)
    manual_results = manual_partition(group)
    print(f"Найдено {len(manual_results)} вариантов.")
    print(f"Время выполнения: {manual_time:.2f} секунд.\n")

    print("=== Все варианты разбиения (алгоритмическое решение) ===")
    for i, (first_team, second_team) in enumerate(manual_results):
        print(f"Вариант {i + 1}: Первая бригада: {first_team}, Вторая бригада: {second_team}")

    print("\n=== Часть 1: Решение с использованием Python ===")
    pythonic_time = timeit.timeit(lambda: pythonic_partition(group), number=1)
    pythonic_results = pythonic_partition(group)
    print(f"Найдено {len(pythonic_results)} вариантов.")
    print(f"Время выполнения: {pythonic_time:.2f} секунд.\n")

    print("=== Все варианты разбиения (Python) ===")
    for i, (first_team, second_team) in enumerate(pythonic_results):
        print(f"Вариант {i + 1}: Первая бригада: {first_team}, Вторая бригада: {second_team}")

    print("\n=== Часть 2: Усложнённое решение с ограничениями ===")
    constrained_results, optimal_result = pythonic_partition_with_constraints(group, max_first_team_sum)
    print(f"Найдено {len(constrained_results)} вариантов с ограничением.\n")

    if optimal_result is None:
        print("Не удалось найти разбиение, удовлетворяющее ограничениям.")
    else:
        print("=== Оптимальное разбиение ===")
        print(f"Первая бригада: {optimal_result[0]}")
        print(f"Вторая бригада: {optimal_result[1]}")
        print(f"Разница сумм: {objective_function(optimal_result[0], optimal_result[1])}\n")


if __name__ == "__main__":
    main()





