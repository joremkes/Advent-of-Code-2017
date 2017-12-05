## 1. read the amount of steps from the current value of the list
## 2. increase the current value of the list with one
## 3. jump with the amount of steps from the current value of the list

#input = [0, 3, 0, 1, -3]
input = []
file = open('millisecond5-1.txt')
for line in file:
    input.append(int(line))

step = 0
position = 0
max_position = len(input)
found = False

while found == False:
    offset = input[position]
    input[position] = input[position] + 1
    position = position + offset
    #print step, position
    #print input
    step = step + 1
    if position >= max_position:
        found = True
        solution = step

print solution



     