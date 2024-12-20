"""Требуется написать ООП с графическим интерфейсом в соответствии со своим вариантом.
Должны быть реализованы минимум один класс, три атрибута, четыре метода (функции).
Ввод данных из файла с контролем правильности ввода.
Базы данных не использовать. При необходимости сохранять информацию в файлах, разделяя значения запятыми (CSV файлы) или пробелами.
Для GUI и визуализации использовать библиотеку tkinter."""

"""Объекты – бронь на гостиничный номер
Функции:	сегментация полного списка брони по срокам проживания
визуализация предыдущей функции в форме круговой диаграммы
сегментация полного списка брони по типам номеров
визуализация предыдущей функции в форме круговой диаграммы"""


import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import csv
from collections import Counter
import matplotlib.pyplot as plt


class HotelBooking:
    def __init__(self):
        self.bookings = []
        self.file_path = None
        self.segmented_data = {}

    def load_from_file(self, file_path):
        self.bookings = []
        self.file_path = file_path

        try:
            with open(file_path, newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if "duration" not in row or "room_type" not in row:
                        raise ValueError("Неверный формат файла. Требуются поля 'duration' и 'room_type'.")
                    row['duration'] = int(row['duration'])
                    self.bookings.append(row)
            messagebox.showinfo("Успех", f"Файл '{file_path}' успешно загружен!")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось загрузить файл: {e}")

    def segment_by_duration(self):
        durations = [b['duration'] for b in self.bookings]
        self.segmented_data = Counter(durations)
        return self.segmented_data

    def segment_by_room_type(self):
        room_types = [b['room_type'] for b in self.bookings]
        self.segmented_data = Counter(room_types)
        return self.segmented_data

    def plot_pie_chart(self, data, title):

        labels = data.keys()
        sizes = data.values()

        plt.figure(figsize=(6, 6))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.title(title)
        plt.show()

class BookingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Сегментация бронирований")
        self.center_window(400, 300)
        self.booking_manager = HotelBooking()

        self.load_button = ttk.Button(root, text="Загрузить файл", command=self.load_file)
        self.load_button.pack(pady=10)

        self.segment_duration_button = ttk.Button(root, text="Сегментация по срокам", command=self.segment_by_duration)
        self.segment_duration_button.pack(pady=5)

        self.segment_room_button = ttk.Button(root, text="Сегментация по типам номеров",
                                              command=self.segment_by_room_type)
        self.segment_room_button.pack(pady=5)

    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            self.booking_manager.load_from_file(file_path)

    def segment_by_duration(self):
        data = self.booking_manager.segment_by_duration()
        self.booking_manager.plot_pie_chart(data, "Сегментация по срокам проживания")

    def segment_by_room_type(self):
        data = self.booking_manager.segment_by_room_type()
        self.booking_manager.plot_pie_chart(data, "Сегментация по типам номеров")

    def center_window(self, width, height):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")

if __name__ == "__main__":
    root = tk.Tk()
    app = BookingApp(root)
    root.mainloop()
