def left_side_triangle():
    for i in range(9):
        if i < 5:
            for j in range(i+1):
                print('*',end=' ')
            print('\n')
        else:
            for j in range(i,9):
                print('*',end=' ')
            print('\n')


def pyramid_1():
    rows = 9
    k = 2 * rows - 2
    for i in range(0, rows):
        for left in range(0,k):
            print(end=' ')

        k -= 2

        for middle in range(0,i+1):
            print(i+1, end=' ')
        print('')
        


# Problems map is a dictionary mapping the serial number with its solver function.

problems = {
    '1': left_side_triangle,
    '2': pyramid_1
}

# main() is the root function from where the other functions are called
# depending on problem number provided in selection

def main():
    global problems
    option = input('Selection: ')

    problems[option]()

main() # Run the root function.