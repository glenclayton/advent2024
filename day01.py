def distance(a,b):
    a = sorted(a)
    b = sorted(b)
    sum = 0
    for i,j in zip(a,b):
        sum = sum + abs(i-j)
    return sum


        
