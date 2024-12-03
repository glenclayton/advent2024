import re



def extract_tuple(row, c):
    regex = r"^(\d+),(\d+)$"
    idx = row.index('mul(',c)
    idy = row.index(')',idx+4)
    ts = row[idx+4:idy]
    matches = re.finditer(regex,ts,re.MULTILINE)
    


def extract_mul(row):
    c = 0
    return []


