input_file = open("input.in")
line = input_file.readline()

arr = []

for i in line.split(","):
    arr.append(int(i))

i = 0

arr[1] = 12
arr[2] = 2

while i < (len(arr) - 1):
    operation = arr[i]
    i = i + 1
    first_operand = arr[arr[i]]
    i = i + 1
    second_operand = arr[arr[i]]
    i = i + 1
    position = arr[i]
    if operation == 99:
        break
    elif operation == 1:
        arr[position] = first_operand + second_operand
    elif operation == 2:
        arr[position] = first_operand * second_operand
    i = i + 1

print(arr[0])
