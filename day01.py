def distance(a,b):
    a = sorted(a)
    b = sorted(b)
    sum = 0
    for i,j in zip(a,b):
        sum = sum + abs(i-j)
    return sum

def readfile():
    text_file = open("day01_input.txt", "r")
    lines = text_file.readlines()
    a = []
    b = []
    for line in lines:
        sl = line.split()
        a.append(int(sl[0]))
        b.append(int(sl[1]))
    return a,b

first,second = readfile()
print(first)
dis = distance(first,second)
print(f"The distance is {dis}")

        
