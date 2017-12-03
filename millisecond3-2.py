import numpy

input = 289326
#input = 1000
size = 21 ## use ODD number
x = (size / 2) 
y = x

x_direction = 1
y_direction = -1

start = 1
step = 1
found = False

## X and Y are reversed!! To resemble descrption and example drawing
a = numpy.zeros((size, size), int)  

a[y, x] = 1

while found == False:
    for i in range(1, step + 1):
        if found == True:
            break
        x = x + (1 * x_direction)
        value = a[y+1, x+1] + a[y, x+1] + a[y-1, x+1] + a[y-1, x] + a[y-1, x-1] + a[y, x-1] + a[y+1, x-1] + a[y+1, x]
        a[y, x] = value
        if value > input:
            found = True
            solution = value
    x_direction = x_direction * -1
    
    for i in range(1, step + 1):
        if found == True:
            break
        #start = start + 1
        y = y + (1 * y_direction)
        value = a[y+1, x+1] + a[y, x+1] + a[y-1, x+1] + a[y-1, x] + a[y-1, x-1] + a[y, x-1] + a[y+1, x-1] + a[y+1, x]
        a[y, x] = value
        if value > input:
        	found = True
        	solution = value
    y_direction = y_direction * -1
    
    step = step + 1

print solution

