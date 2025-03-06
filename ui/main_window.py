import tkinter as tk
from tkinter import filedialog as fd
import sys
import os
from services.generation_sensor import SensorGenerator

sys.path.append("C:/Users/Главный пользователь/PycharmProjects/SmartMix_Builder/.venv")

# Путь к проекту
project_filename = ""

# Путь к таблицe сигналов
signal_table_filename = ""

# Путь к network_variables
network_variables_filename = ""

class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("SmartMix builder")
        self.root.geometry("700x450")

        # Кнопка выбора проекта
        tk.Button(text='Выберите проект',
                  command=self.select_project_callback).pack(fill=tk.X)

        # Кнопка выбора таблицы сигналов
        tk.Button(text='Выберите таблицу сигналов',
                  command=self.select_network_variables_callback).pack(fill=tk.X)

        # Кнопки
        button = tk.Button(
            self.root,
            text="Сгенерирровать",
            font=("Arial", 14, "bold"),  # Изменяем шрифт
            bg="#4CAF50",  # Цвет фона
            fg="white",  # Цвет текста
            activebackground="#45a049",  # Цвет при нажатии
            activeforeground="white",  # Цвет текста при нажатии
            relief=tk.RAISED,  # Стиль границы
            borderwidth=5,  # Толщина границы
            command=self.generation_click_button
        )

        # Размещение кнопки
        button.pack(pady=50)

    # Генерация проекта
    def generation_click_button(self):
        s = SensorGenerator()

    # Обработчик нажатия на выбор проекта
    def select_project_callback(self):
        global project_filename
        name = fd.askopenfilename()
        project_filename = name

    # Обработчик нажатия для выбора таблицы сигналов
    def select_network_variables_callback(self):
        global network_variables_filename
        name = fd.askopenfilename()
        network_variables_filename = name

    def run(self):
        self.root.mainloop()