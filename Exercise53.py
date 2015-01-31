__author__ = 'charles'

prompt_type_error = 'Please enter a valid integer\n'
prompt_a = 'Value of a?\n'
prompt_b = 'Value of b?\n'
prompt_c = 'Value of c?\n'
prompt_n = 'Value of n?\n'

a = raw_input(prompt_a)
while type(a) is not int:
    try:
        a = int(a)
    except:
        a = raw_input(prompt_type_error)


b = raw_input(prompt_b)

while type(b) is not int:
    try:
        b = int(b)
    except:
        b = raw_input(prompt_type_error)

c = raw_input(prompt_c)

while type(c) is not int:
    try:
        c = int(c)
    except:
        c = raw_input(prompt_type_error)


n = raw_input(prompt_n)

while type(n) is not int:
    try:
        n = int(n)
    except:
        n = raw_input(prompt_type_error)



def fermat_test(a, b, c, n):
    left = a**n + b**n
    right = c**n

    if left == right:
        print 'You broke Fermat\'s theorem ... or n is less than two'
    else:
        print 'The rules of Math still apply'


fermat_test(a, b, c, n)
