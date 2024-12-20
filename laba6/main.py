"""Задание состоит из двух частей.
1 часть – написать программу в соответствии со своим вариантом задания. Написать 2 варианта формирования
 (алгоритмический и с помощью функций Питона), сравнив по времени их выполнение.
2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение
 на характеристики объектов (которое будет сокращать количество переборов) и целевую функцию для нахождения
 оптимального  решения."""

"""Группу из 20 рабочих нужно разделить на 3 бригады,
причем в первую бригаду должны входить 3 человека, во вторую — 5 и в третью — 12. 
Вывести все возможные варианты"""

from itertools import combinations
import time


def manual_partition(group):
    results = []
    n = len(group)

    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                first_team = [group[i], group[j], group[k]]
                remaining1 = [x for x in group if x not in first_team]

                for l1 in range(len(remaining1) - 4):
                    for l2 in range(l1 + 1, len(remaining1) - 3):
                        for l3 in range(l2 + 1, len(remaining1) - 2):
                            for l4 in range(l3 + 1, len(remaining1) - 1):
                                for l5 in range(l4 + 1, len(remaining1)):
                                    second_team = [
                                        remaining1[l1], remaining1[l2], remaining1[l3],
                                        remaining1[l4], remaining1[l5]
                                    ]
                                    third_team = [x for x in remaining1 if x not in second_team]
                                    results.append((first_team, second_team, third_team))
    return results


def pythonic_partition(group):
    results = []
    for first_team in combinations(group, 3):
        remaining1 = [x for x in group if x not in first_team]
        for second_team in combinations(remaining1, 5):
            third_team = [x for x in remaining1 if x not in second_team]
            results.append((list(first_team), list(second_team), third_team))
    return results


def objective_function(first_team, second_team, third_team):
    max_sum = max(sum(first_team), sum(second_team), sum(third_team))
    min_sum = min(sum(first_team), sum(second_team), sum(third_team))
    difference = max_sum - min_sum
    return difference


def pythonic_partition_with_constraints(group, max_first_team_sum):
    results = []
    optimal_result = None
    optimal_difference = float('inf')

    for first_team in combinations(group, 3):
        if sum(first_team) > max_first_team_sum:
            continue

        remaining1 = [x for x in group if x not in first_team]
        for second_team in combinations(remaining1, 5):
            third_team = [x for x in remaining1 if x not in second_team]

            current_difference = objective_function(first_team, second_team, third_team)
            results.append((list(first_team), list(second_team), third_team))

            if current_difference < optimal_difference:
                optimal_difference = current_difference
                optimal_result = (list(first_team), list(second_team), third_team)

    return results, optimal_result


def main():
    group = list(range(1, 21))
    max_first_team_sum = 30  # Установите порог для суммы первой бригады

    print("=== Часть 1: Алгоритмическое решение ===")
    start_time = time.time()
    manual_results = manual_partition(group)
    end_time = time.time()
    print(f"Найдено {len(manual_results)} вариантов.")
    print(f"Время выполнения: {end_time - start_time:.2f} секунд.\n")

    print("=== Часть 1: Решение с использованием Python ===")
    start_time = time.time()
    pythonic_results = pythonic_partition(group)
    end_time = time.time()
    print(f"Найдено {len(pythonic_results)} вариантов.")
    print(f"Время выполнения: {end_time - start_time:.2f} секунд.\n")

    print("=== Часть 2: Усложнённое решение с ограничениями ===")
    start_time = time.time()
    constrained_results, optimal_result = pythonic_partition_with_constraints(group, max_first_team_sum)
    end_time = time.time()
    print(f"Найдено {len(constrained_results)} вариантов с ограничением.")
    print(f"Время выполнения: {end_time - start_time:.2f} секунд.\n")

    if optimal_result is None:
        print("Не удалось найти разбиение, удовлетворяющее ограничениям.")
    else:
        print("=== Оптимальное разбиение ===")
        print(f"Первая бригада: {optimal_result[0]}")
        print(f"Вторая бригада: {optimal_result[1]}")
        print(f"Третья бригада: {optimal_result[2]}")
        print(f"Оптимальная разница: {objective_function(optimal_result[0], optimal_result[1], optimal_result[2])}")


if __name__ == "__main__":
    main()





