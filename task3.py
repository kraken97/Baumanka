def test_mean_func(f):
    # Mean of no el-s is undefined
    assert f([]) is None
    # Mean of 2 elements (42+2)/2 = 22
    assert f([42, 2]) == 22
    # Mean of many elements
    assert f([1,2,3,4,5,6,7,8]) == 4.5
    # Mean of list of one el-t is this el-t
    for x in range(500, 600):
        assert f([x]) == x
    # Test with floating-point numbers
    assert f([3.2,3.23]) == 3.215
    assert f([3.5,4.5]) == 4
    #Test with objects of wrong type
    assert f([3.5,"42"]) == None
    assert f(["42"]) == None

def my_mean(l):
    if len(l) == 0:
        return None
    else:
        res = None
        try:
            res =sum(l) / len(l)
        except TypeError:
            res = None

        return res

test_mean_func(my_mean)