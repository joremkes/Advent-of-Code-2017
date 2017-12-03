file = open('millisecond2-1.txt')

solution = 0 
for line in file:
    data = map(int, (line.split()))
    data.sort()
    solution = solution + (data[-1] - data[0])

print solution

    
    
