file = open('millisecond4-1.txt')

solution = 0 
valid = True


for line in file:
    valid = True
    data = line.split()
    
    for i in range(len(data)):
        data[i] = "".join(sorted(data[i]))
        
    for item in data:
        if data.count(item) >= 2:
             valid = False
    if valid == True:
        solution = solution + 1

print solution

    
    
        