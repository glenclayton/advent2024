from day01 import distance
def test_distance():
    a = [3,4,2,1,3,3]
    b = [4,3,5,3,9,3]
    dist = distance(a,b)
    assert dist == 11
    