# Solution for the first day of advent of code

inFile = open("input.in", "r")
outFile = open("output.out", "w")

line = inFile.readline()

sum = 0


def compute(argument):
    global sum
    argument = argument / 3
    argument = argument // 1
    argument = int(argument)
    argument = argument - 2
    if argument > 0:
        sum = sum + argument
    return argument


while line != '':
    for i in line.split():
        answer = int(i)
# In order to solve the first half of the problem, comment the "while" below.
    while answer > 0:
        answer = compute(answer)
    line = inFile.readline()

    
outFile.write(str(sum))
