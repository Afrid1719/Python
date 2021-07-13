import datetime

def current_datetime():
    d = datetime.datetime.now()
    print(d)
    print(d.time())
    print(d.strftime('%A, %d %B %Y, %I:%M:%S %p'))

def str_to_datetime():
    date_str = 'Feb 25 2020 4:20PM'
    d = datetime.datetime.strptime(date_str, '%b %d %Y %I:%M%p')
    print(d)

def subtract_a_week():
    print()

# Problems map is a dictionary mapping the serial number with its solver function.

problems = {
    '1': current_datetime,
    '2': str_to_datetime,
    '3': subtract_a_week
}

# main() is the root function from where the other functions are called
# depending on problem number provided in selection

def main():
    global problems
    option = input('Selection: ')

    problems[option]()

main() # Run the root function.