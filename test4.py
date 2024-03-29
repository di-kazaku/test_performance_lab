"""
					Task4
	Дан массив целых чисел nums. Напишите программу, выводящую минимальное количество ходов, 
требуемых для приведения всех элементов к одному числу. За один ход можно уменьшить или 
увеличить число массива на 1.
"""



from sys import argv


nums = []
with open(f'{argv[1]}', 'r', encoding='utf-8') as f:
	for line in f:
		nums.append(int(line.strip('\n')))

n = 0
while len(set(nums)) not in (0, 1):
	for i in range(len(nums)):
		if nums[i] < round(sum(nums) / len(nums)):
			nums[i] += 1
			n += 1
		elif nums[i] > round(sum(nums) / len(nums)):
			nums[i] -= 1
			n += 1
print(n)
