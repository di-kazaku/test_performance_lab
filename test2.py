"""
				Task2
	Напишите программу, которая рассчитывает положение точки относительно окружности.
Координаты центра окружности и его радиус считываются из файла1.
Пример:
1 1
5
	Координаты точек считываются из файла2.
Пример:
0 0
1 6
6 6
	Файлы передаются программе в качестве аргументов. Файл с координатами и радиусом окружности - 1 аргумент,
файл с координатами точек - 2 аргумент.
Координаты в диапазоне float. Количество точек от 1 до 100.
Вывод каждого положения точки заканчивается символом новой строки.
	Соответствия ответов:
0 - точка лежит на окружности
1 - точка внутри
2 - точка снаружи
"""

def point_position(file1, file2):
    points = []
    with open(file1, 'r') as file_1:
        radius_centr = file_1.read().split('\n')
    with open(file2, 'r') as file_2:
        while True:
            line = file_2.readline().strip()
            if line:
                points.append(line.split('\n'))
            if not line:
                break

    points = [[float(i) for i in j[0].split(' ')] for j in points]
    centr_radius = [[float(i) for i in j.split(' ')] for j in radius_centr]
    radius = centr_radius[1][0]
    centr_x = centr_radius[0][0]
    centr_y = centr_radius[0][1]

    for point in points:
        x = point[0]
        y = point[1]
        result = ((x - centr_x) ** 2 + (y - centr_y) ** 2) ** 0.5
        if result < radius:
            return 1  # точка лежит внутри
        elif result > radius:
            return 2  # точка лежит снаружи
        elif result == radius:
            return 0  # точка лежит на окружности



if __name__ == "__main__":
    print(point_position('file1.txt', 'file2.txt'))
