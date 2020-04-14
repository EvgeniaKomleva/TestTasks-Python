import sys

array = []
range_sum = 0
with open(sys.argv[1], "r") as file:  
    for line in file.readlines():
        array.append(int(line.strip())) 
array.sort() 

print(f"Отсортированный массив:\n{array}")

average = round(sum(array) / len(array), 2)
print("Среднее значение массива:", average)

percentil_range = round(90 / 100 * len(array))
print("90-ый пертицентиль: ", array[percentil_range - 1])

for i in array:
    if (i > average and i <= array[percentil_range - 1]) or (i > array[percentil_range - 1] and i <= average):
        range_sum += i
print("Сумма чисел между средним и 90-ым перцентилем:", range_sum)
