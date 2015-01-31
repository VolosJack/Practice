__author__ = 'charles'


def the_return(x, y):
    if x > y:
        return 1
    if x == y:
        return 0
    if x < y:
        return -1

print the_return(raw_input('x='), raw_input('y='))