"""
					Task1
	Круговой массив - массив из элементов, в котором по достижению конца массива следующим
элементом будет снова первый. Mассив задается числом n, то есть представляет собой числа от 1 до n.
	Напишите программу, которая выводит путь, по которому,
двигаясь интервалом длины m по заданному массиву, концом будет являться первый элемент.
Началом одного интервала является конец предыдущего.
Путь - массив из начальных элементов полученных интервалов.
	Пример 1: n = 4, m = 3
	Решение: Круговой массив: 1234.
	При длине обхода 3 получаем интервалы: 123, 341. Полученный путь: 13.
"""

from sys import argv
a, b = int(argv[1]), int(argv[2])


def task1(n, m):
	if m == 1:
		return 1

	# Формирование кругового массива
	circular_array = ''
	my_list = [i for _ in range(n * 5) for i in range(1, n + 1)]
	for k in my_list[0:len(my_list):m - 1]:
		circular_array += str(k)

	# Возврат пути без повторений
	ind = 0
	for i in range(1, len(circular_array)):
		x = circular_array[0:i]
		if ind < circular_array.find(x, 1):
			ind = circular_array.find(x, 1)
	return circular_array[0:ind]


print(task1(a, b))
