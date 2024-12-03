import re



def extract_tuple(row, c):
    regex = r"^(\d+),(\d+)$"
    idx = row.index('mul(',c)
    idy = row.index(')',idx+4)
    ts = row[idx+4:idy]
    thematch = re.match(regex,ts)
    if thematch != None:
        a = thematch.group(1)
        b = thematch.group(2)
        return (int(a),int(b))
    return (0,0)
    


def extract_mul(row):
    c = 0
    return []


