"""Требуется для своего варианта второй части л.р. №6 (усложненной программы) разработать реализацию
с использованием графического интерфейса. Допускается использовать любую графическую библиотеку питона.
Рекомендуется использовать внутреннюю библиотеку питона  tkinter."""

import tkinter as tk
from tkinter import scrolledtext
import itertools


def calculate_groups():
    try:
        num_workers = int(entry_workers.get())
        if num_workers < 20:
            raise ValueError("Количество рабочих должно быть >= 20")

        workers = list(range(1, num_workers + 1))

        output_text.delete(1.0, tk.END)
        best_solution_text.delete(1.0, tk.END)

        min_diff = float("inf")
        best_solution = None
        all_solutions = []

        for group1 in itertools.combinations(workers, 3):
            if 1 not in group1:
                continue
            remaining1 = set(workers) - set(group1)
            for group2 in itertools.combinations(remaining1, 5):
                group3 = tuple(remaining1 - set(group2))

                sum_group1 = sum(group1)
                sum_group2 = sum(group2)
                diff = abs(sum_group1 - sum_group2)

                if diff < min_diff:
                    min_diff = diff
                    best_solution = (group1, group2, group3)

                all_solutions.append((group1, group2, group3))

        for solution in all_solutions:
            output_text.insert(
                tk.END,
                f"Группа 1: {solution[0]}, Группа 2: {solution[1]}, Группа 3: {solution[2]}\n",
            )

        if best_solution:
            best_solution_text.insert(
                tk.END,
                f"Лучшая конфигурация:\n"
                f"Группа 1: {best_solution[0]}, сумма: {sum(best_solution[0])}\n"
                f"Группа 2: {best_solution[1]}, сумма: {sum(best_solution[1])}\n"
                f"Группа 3: {best_solution[2]}, сумма: {sum(best_solution[2])}\n"
                f"Минимальная разница: {min_diff}\n",
            )

    except ValueError as e:
        output_text.insert(tk.END, f"Ошибка: {e}\n")


root = tk.Tk()
root.title("Разделение рабочих на группы")

frame_input = tk.Frame(root)
frame_input.pack(pady=10)
label_workers = tk.Label(frame_input, text="Количество рабочих:")
label_workers.pack(side=tk.LEFT, padx=5)
entry_workers = tk.Entry(frame_input)
entry_workers.pack(side=tk.LEFT)

button_calculate = tk.Button(root, text="Рассчитать", command=calculate_groups)
button_calculate.pack(pady=10)

output_label = tk.Label(root, text="Все решения:")
output_label.pack()
output_text = scrolledtext.ScrolledText(root, width=80, height=15)
output_text.pack(pady=5)

best_solution_label = tk.Label(root, text="Лучшее решение:")
best_solution_label.pack()
best_solution_text = tk.Text(root, width=80, height=5)
best_solution_text.pack(pady=5)

root.mainloop()
