def mutliplication():
    n1 = int(input('Number 1: '))
    n2 = int(input('Number 2: '))
    print('Output: ' + str(n1*n2))


def print_formatted():
    print('My', 'name', 'is', 'Jarvis', sep='**')

# Problems map is a dictionary mapping the serial number with its solver function.

problems = {
    '1': mutliplication,
    '2': print_formatted
}

# main() is the root function from where the other functions are called
# depending on problem number provided in selection

def main():
    global problems
    option = input('Selection: ')

    problems[option]()

main() # Run the root function.