from day03 import extract_mul

def test_extract_mul():
    data = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'
    rv = extract_mul(data)
    assert len(rv) == 4
    assert rv[0] == (2,4)
    assert rv[1] == (5,5)
    assert rv[2] == (11,8)
    assert rv[3] == (8,5)


