input = 289326
x = 0
y = 0

x_direction = 1
y_direction = -1

start = 1
step = 1
found = False

while found == False:
    for i in range(1, step + 1):
        if input == start:
            found = True
            break
        else:
            start = start + 1
            x = x + (1 * x_direction)
    x_direction = x_direction * -1
    
    for i in range(1, step + 1):
        if input == start:
            found = True
            break
        else:
            start = start + 1
            y = y + (1 * y_direction)
    y_direction = y_direction * -1
    
    step = step + 1

solution = abs(x) + abs(y)

print solution

    

        
    