from day02 import is_safe

def test_is_safe():
    row1 = [7,6,4,2,1]
    assert is_safe(row1) == True
    row2 = [1,2,7,8,9]
    assert is_safe(row2) == False
    row3 = [9,7,6,2,1]
    assert is_safe(row3) == False
    row4 = [1,3,2,4,5]
    assert is_safe(row4) == False
    row5 = [8,6,4,4,1]
    assert is_safe(row5) == False
    row6 = [1,3,6,7,9]
    assert is_safe(row6) == True