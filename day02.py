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
    


