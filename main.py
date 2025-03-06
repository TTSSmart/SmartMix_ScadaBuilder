import pandas as pd
from openpyxl import load_workbook
from openpyxl.worksheet.print_settings import PRINT_AREA_RE


#Чтение данных
file_name = 'Таблица сигналов Alfa (2).xlsm'
sql_script = 'INSERT INTO `sensors` (`line_num`, `description`, `isAlarm`, `isInvert`, `pos_x`, `pos_y`, `network_var`) VALUES'

df = pd.read_excel(file_name, skiprows=1, sheet_name='DI SCADA')
print(df.columns)

if 'Название сигнала' in df.columns and 'SENSOR_ST' in df.columns:
    # Фильтрация строк, где SENSOR_ST заполнен и является числом
    filtered_df = df[df['SENSOR_ST'].notna() & pd.to_numeric(df['SENSOR_ST'], errors='coerce').notna()]

    # Создание словаря с соответствием "Название сигнала" -> "SENSOR_ST"
    signal_dict = filtered_df.set_index('Название сигнала')['SENSOR_ST'].to_dict()
    items = list(signal_dict.items())

    # Вывод результата
    print("Словарь соответствия 'Название сигнала' -> 'SENSOR_ST':")
    for i, (signal_name, sensor_value) in enumerate(items):
        if i == len(items) - 1:  # Проверяем, является ли это последним элементом
            sql_script += '\n' + f"(1, '{signal_name}', 1, 1, 400, 400, '{sensor_value}');"
        else:
            sql_script += '\n' + f"(1, '{signal_name}', 1, 1, 400, 400, '{sensor_value}'),"

    print(sql_script)
else:
    print("Один или оба столбца ('Название сигнала', 'SENSOR_ST') не найдены в файле.")