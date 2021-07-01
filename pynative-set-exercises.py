def add_list_to_set():
    set1 = {"Yellow", "Orange", "Black"}
    list1 = ["Blue", "Green", "Red"]

    set1.update(list1)

    print('Output: ' + str(set1))

def set_of_identical_items():
    set1 = {10, 20, 30, 40, 50}
    set2 = {30, 40, 50, 60, 70}
    
    #set3 = {x for x in set1 if x in set2}
    #print('Output: ' + str(set3))

    print(set1.intersection(set2))

def remove_duplicates():
    set1 = {10, 20, 30, 40, 50}
    set2 = {30, 40, 50, 60, 70}
    set3 = set1.union(set2)

    print('Output: ' + str(set3))

def update_different_set():
    set1 = {10, 20, 30}
    set2 = {20, 40, 50}
    set1.difference_update(set2)

    print('Output: ' + str(set1))

def remove_subset():
    set1 = {10, 20, 30, 40, 50}
    set1.difference_update({10, 20, 30})

    print('Output: ' + str(set1))

def remove_non_identical():
    set1 = {10, 20, 30, 40, 50}
    set2 = {30, 40, 50, 60, 70}
    set1.symmetric_difference_update(set2)

    print('Output: ' + str(set1))

def check_and_display_common_items():
    set1 = {10, 20, 30, 40, 50}
    set2 = {60, 70, 80, 90, 10}

    if not set1.isdisjoint(set2):
        print('Common items in two sets are:')
    else:
        print('There are no common items in the two sets.')
    
    set3 = set1.intersection(set2)
    print(set3)

def same_as_6():
    print('Same as Problem 6.')

def remove_different_items():
    set1 = {10, 20, 30, 40, 50}
    set2 = {30, 40, 50, 60, 70}

    set1.intersection_update(set2)

    print('Output: ' + str(set1))

# Problems map is a dictionary mapping the serial number with its solver function.

problems = {
    '1': add_list_to_set,
    '2': set_of_identical_items,
    '3': remove_duplicates,
    '4': update_different_set,
    '5': remove_subset,
    '6': remove_non_identical,
    '7': check_and_display_common_items,
    '8': same_as_6,
    '9': remove_different_items
}

# main() is the root function from where the other functions are called
# depending on problem number provided in selection

def main():
    global problems
    option = input('Selection: ')

    problems[option]()

main() # Run the root function.