file = open('millisecond2-1.txt')

solution = 0 
for line in file:
    data = map(int, (line.split()))
    
    for x in data:
        for y in data:
            if x % y == 0:
                if x != y:
                    #print x, y
                    solution = solution + (x / y)
                    
print solution

    
    
