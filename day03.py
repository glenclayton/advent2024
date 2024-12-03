import re



def extract_tuple(row, c):
    regex = r"^(\d+),(\d+)$"
    idx = row.find('mul(',c)
    idy = row.find(')',idx+4)
    if idx<0 or idy<0:
        return None,-1
    ts = row[idx+4:idy]
    thematch = re.match(regex,ts)
    if thematch != None:
        a = thematch.group(1)
        b = thematch.group(2)
        return (int(a),int(b)),idy
    return (0,0),idx+4
    


def extract_mul(row):
    c = 0
    i = 0
    while True:
        t,i = extract_tuple(row,i)
        if t == None:
            break
        c = c+t[0]*t[1]
        print(f"{t} found, next pos {i}")
    return c
    
def readfile():
    text_file = open("day03_input.txt", "r")
    rows = text_file.readlines()
    return rows

rows = readfile()
print(len(rows))
row = ''.join(rows)
print(row)
val = extract_mul(row)
print(f"Value is {val}")




