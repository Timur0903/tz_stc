import openpyxl as op


filename_2024 = 'перечень 2024 ТЗ Якушев Т.Н. python.xlsx'
wb_2024 = op.load_workbook(filename_2024)
sheet_2024 = wb_2024.active


filename_4_1 = '4-1.xlsx'
wb_4_1 = op.load_workbook(filename_4_1)
sheet_4_1 = wb_4_1.active


values_left = []
values_right = []


for i in range(1, 391):
    value_2024 = sheet_2024['A' + str(i)].value

    for j in range(1, 7489):
        value_4_1 = sheet_4_1['A' + str(j)].value

        if value_2024 == value_4_1:
            values_left.append(value_2024)
            values_right.append(value_4_1)


print("Совпадающие значения из первого файла:", values_left)
print("Совпадающие значения из второго файла:", values_right)
print("Количество совпадений", len(values_left))

