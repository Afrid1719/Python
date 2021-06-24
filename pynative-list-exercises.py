def rev_list():
    list1 = [100, 200, 300, 400, 500]
    list1.reverse()

    print('Output: ' + str(list1))

def concat_list_index():
    list1 = ["M", "na", "i", "Ke"]
    list2 = ["y", "me", "s", "lly"]

    def concat_list(a, b):
        return a + b

    res = map(concat_list, list1, list2)
    res = list(res)

    print('Output: ' + str(res))

def square_items():
    list1 = [1, 2, 3, 4, 5, 6, 7]
    list1 = [i*i for i in list1]

    print('Output: ' + str(list1))

def concat_list_in_patt1():
    list1 = ["Hello ", "take "]
    list2 = ["Dear", "Sir"]
    res = []

    for x in list1:
        [res.append(x + y) for y in list2]
    
    print('Output: ' + str(res))

def iterate_simultaneously():
    list1 = [10, 20, 30, 40]
    list2 = [100, 200, 300, 400]

    for x,y in zip(list1,list2[::-1]):
        print(str(x) + ' ' + str(y))

def remove_empty_str():
    list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
    
    while list1.count("") is not 0:
        list1.remove("")
    print(list1)

def add_item_inside():
    list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
    list1[2][2].append(7000)
    print(list1)

def extend_in_between():
    list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
    ext = ["h", "i", "j"]

    list1[2][1][2].extend(ext)

    print('Output: ' + str(list1))

def replace_first_match():
    list1 = [5, 10, 15, 20, 25, 50, 20]
    pos = list1.index(20)
    list1.pop(pos)
    list1.insert(pos, 200)

    print('Output: ' + str(list1))

def remove_all_matches():
    list1 = [5, 20, 15, 20, 25, 50, 20]
    
    while list1.count(20) > 0:
        list1.remove(20)

    print('Output: ' + str(list1))

# Problems map is a dictionary mapping the serial number with its solver function.

problems = {
    '1': rev_list,
    '2': concat_list_index,
    '3': square_items,
    '4': concat_list_in_patt1,
    '5': iterate_simultaneously,
    '6': remove_empty_str,
    '7': add_item_inside,
    '8': extend_in_between,
    '9': replace_first_match,
    '10': remove_all_matches
}

# main() is the root function from where the other functions are called
# depending on problem number provided in selection

def main():
    global problems
    option = input('Selection: ')

    problems[option]()

main() # Run the root function.