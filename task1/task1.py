import sys

array = []
range_sum = 0
with open(sys.argv[1], "r") as file:  # ��������� ������ �� �����(�������� � ������� ��������� � ��������� ������)
    for line in file.readlines():
        array.append(int(line.strip()))  # �������� ������ �� ����� � ������ array ��� ���������� ������
array.sort()  # ��������������� ������

print(f"��������������� ������:\n{array}")
# ������ ��������
average = round(sum(array) / len(array), 2)
print("������� �������� �������:", average)
# ������ ����� 90-�� ����������.
percentil_range = round(90 / 100 * len(array))
print("90-�� ����������: ", array[percentil_range - 1])
# ������ �����
for i in array:
    if (i > average and i <= array[percentil_range - 1]) or (i > array[percentil_range - 1] and i <= average):
        range_sum += i
print("����� ����� ����� ������� � 90-�� �����������:", range_sum)
