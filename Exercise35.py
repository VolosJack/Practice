'''
Exercise 3-5

Draw:
+ - - - - + - - - - +
|        |          |
|        |          |
|        |          |
|        |          |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +


'''


'''
 Print the horizontal rows
'''


base_box = '+ - - - - +'
base_row = '|         |'
additional_column = ' - - - - +'
additional_row = '         |'

'''
 Print the vertical columns 4 times
'''


def one_box():
    print base_box
    for i in range(4):
        print base_row
    print base_box

'''
 Concatenate it all together
'''


def four_square():
    print base_box + additional_column
    for i in range(4):
        print base_row + additional_row
    print base_box + additional_column
    for i in range(4):
        print base_row + additional_row
    print base_box + additional_column


def sixteen_square():
    print base_box + additional_column + additional_column + additional_column
    for i in range(4):
        print base_row + additional_row + additional_row + additional_row
    print base_box + additional_column + additional_column + additional_column
    for i in range(4):
        print base_row + additional_row + additional_row + additional_row
    print base_box + additional_column + additional_column + additional_column
    for i in range(4):
        print base_row + additional_row + additional_row + additional_row
    print base_box + additional_column + additional_column + additional_column
    for i in range(4):
        print base_row + additional_row + additional_row + additional_row
    print base_box + additional_column + additional_column + additional_column


four_square()

sixteen_square()