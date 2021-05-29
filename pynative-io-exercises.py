def mutliplication():
    n1 = int(input('Number 1: '))
    n2 = int(input('Number 2: '))
    print('Output: ' + str(n1*n2))


def print_formatted():
    print('My', 'name', 'is', 'Jarvis', sep='**')

def dec_to_octal():
    inp = int(input('Input: '))
    print('Output: ' + str(oct(inp))[2:])

def disp_float():
    inp = float(input('Input: '))
    print('Output: {:.2f}'.format(inp))

def accept_floats():
    list1 = []
    for i in range(5):
        inp = float(input('Input: '))
        list1.append(inp)
    
    print(list1)


def file_reading():
    f =  open('test.txt', 'r')
    i = 0
    for l in f:
        i += 1
        if i == 5:
            continue
        print(l)

    f.close()

def accept_only_three():
    inp = input('Input :').split(' ')
    print('Output :')
    for i in range(3):
        print(inp[i])

def string_format():
    total_money = 1000
    quantity = 3
    price = 450
    print('I have {money} dollars so I can buy {quantity} football for {price:.2f} dollars.'.format(money=total_money, quantity=quantity, price=price))


def check_empty_file():
    f = open('test.txt', 'r')
    try:
        data = f.read()
        if (len(data) > 0):
            print('File not empty')
        else:
            print('File is empty')
    except:
        print('File Not found')
    finally: 
        f.close()


# Problems map is a dictionary mapping the serial number with its solver function.

problems = {
    '1': mutliplication,
    '2': print_formatted,
    '3': dec_to_octal,
    '4': disp_float,
    '5': accept_floats,
    '6': file_reading,
    '7': accept_only_three,
    '8': string_format,
    '9': check_empty_file
}

# main() is the root function from where the other functions are called
# depending on problem number provided in selection

def main():
    global problems
    option = input('Selection: ')

    problems[option]()

main() # Run the root function.