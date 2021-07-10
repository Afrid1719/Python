def rev_tuple():
    tuple1 = (10, 20, 30, 40, 50, 60, 70)
    list1 = list(tuple1)
    list1.reverse()

    print(tuple(list1))

def access_item():
    tuple1 = ('Orange', [10,20,30], (5,15, 25))
    val = tuple1[1][1]

    print('Output: ' + str(val))

def single_item_tuple():
    tuple1 = (10,)

    print('Output: ' + str(tuple1))

def unpack_tuple():
    tuple1 = (10, 20, 30, 40)
    a, b, c, d = tuple1

    print(a)
    print(b)
    print(c)
    print(d)

def swap_tuples():
    tuple1 = (11, 22)
    tuple2 = (99, 88)

    tuple1, tuple2 = tuple2, tuple1
    print('Output :')
    print(tuple1)
    print(tuple2)

def copy_into_tuple():
    tuple1 = (11, 22, 33, 44, 55, 66)
    *x, a, b, c = tuple1
    
    print('Output :' + str((a, b)))

    # print(tuple1[3:-1])

def modify_list_in_tuple():
    tuple1 = (11, [22, 33], 44, 55)
    list1 = list(tuple1)
    list1[1][0] = 222
    tuple1 = tuple(list1)

    print('Output :' + str(tuple1))

def sort_tuple_of_tuples():
    tuple1 = (('a', 23), ('b', 37), ('c', 11), ('d', 29))
    list1 = list(tuple1)

    sortFunc = lambda x: x[1]
    list1.sort(key = sortFunc)
    print(tuple(list1))

def count_occurences():
    tuple1 = (50, 10, 60,  70, 50)
    t = tuple1.count(50)

    print(t)

def are_all_same_items():
    tuple1 = (45, 45, 45, 45)

    print(tuple1.count(tuple1[0]) == len(tuple1))

# Problems map is a dictionary mapping the serial number with its solver function.

problems = {
    '1': rev_tuple,
    '2': access_item,
    '3': single_item_tuple,
    '4': unpack_tuple,
    '5': swap_tuples,
    '6': copy_into_tuple,
    '7': modify_list_in_tuple,
    '8': sort_tuple_of_tuples,
    '9': count_occurences,
    '10': are_all_same_items
}

# main() is the root function from where the other functions are called
# depending on problem number provided in selection

def main():
    global problems
    option = input('Selection: ')

    problems[option]()

main() # Run the root function.