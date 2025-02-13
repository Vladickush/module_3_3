#  Распаковка позиционных параметров
def print_params(a=1, b='строка', c=True):
    print(a, b, c)
    return

#  1.Функция с параметрами по умолчанию:
print_params(b=25)
print_params(c=[1, 2, 3])

#  2.Распаковка параметров:
values_list = [12, 'students', False]
print_params(*values_list)
values_dict = {'a': 'Vlad', 'b': 'Urban', 'c': 2024}
print_params(**values_dict)

#  3.Распаковка + отдельные параметры:
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)