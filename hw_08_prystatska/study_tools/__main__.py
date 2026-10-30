from study_tools.calculations import mean
from study_tools.formatting import format_report

print("Запуск пакету study_tools")
val = mean(5, 5, 5)
print(format_report("Тест модуля через __main__", val))
