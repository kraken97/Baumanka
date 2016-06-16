from math import sqrt

def sq_mean(seq):
    t_sum = 0
    for el in seq:
        t_sum += el * el
    return sqrt(t_sum / len(seq))

test_seq = [1,2,3,4,5]
print("Root mean square of %s is %f" % (test_seq,sq_mean(test_seq)))
