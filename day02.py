def is_safe(row):
    diffs = []
    for i in range(len(row)-1):
        a = row[i]
        b = row[i+1]
        diffs.append(b-a)
    max_diff = max(diffs)
    min_diff = min(diffs)
    rv = False
    if ((max_diff<4) and (min_diff>0)) or ((min_diff>-4) and max_diff<0):
        rv = True
    return rv

def tolerate_is_safe(row):
    for i in range(len(row)):
        newrow=row.copy()
        del newrow[i]
        rv = is_safe(newrow)
        if rv:
            return rv
    return False



def readfile():
    text_file = open("day02_input.txt", "r")
    lines = text_file.readlines()
    rows = []
    for line in lines:
        rows.append(list(map(int,line.split())))
    return rows

def list_safe_count(rows):
    safe = 0
    for row in rows:
        if is_safe(row):
            safe=safe+1
    return safe

def list_tolerate_safe_count(rows):
    safe = 0
    for row in rows:
        if tolerate_is_safe(row):
            safe=safe+1
    return safe

rows = readfile()
safes = list_safe_count(rows)
print(f"Number of safe rows = {safes}")

tolerate_safes = list_tolerate_safe_count(rows)
print(f"Number of safe rows(tolerant) = {tolerate_safes}")


    
