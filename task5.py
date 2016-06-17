def is_3_5_div(x):
    if not (type(x) ==int or type(x) == float):
        return False
    return \
        x % 2 == 0 and \
        x % 3 == 0

assert is_3_5_div(6)
assert is_3_5_div(12)
assert not is_3_5_div(2)
assert not is_3_5_div(3)
assert not is_3_5_div(4)
assert not is_3_5_div(9)
assert not is_3_5_div('42')
assert not is_3_5_div(3.5)
assert not is_3_5_div(2.3)

print("All tests passed successfully")
