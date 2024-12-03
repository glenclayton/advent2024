import re



def extract_tuple(row, c):
    regex = r"^(\d+),(\d+)$"
    idx = row.find('mul(',c)
    idy = row.find(')',idx+4)
    if idx<0 or idy<0 :
        return (0,0)
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


