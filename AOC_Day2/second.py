input_file = open("input.in")
line = input_file.readline()

default_arr = []

for i in line.split(","):
    default_arr.append(int(i))


for noun in range(100):
    for verb in range(100):

        arr = default_arr.copy()

        i = 0
        arr[1] = noun
        arr[2] = verb

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

        if arr[0] == 19690720:
            print(100 * arr[1] + arr[2])
            break



