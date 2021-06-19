def merge_lists():
    list1 = [3, 6, 9, 12, 15, 18, 21]
    list2 = [4, 8, 12, 16, 20, 24, 28]
    
    list1 = [list1[i] for i in range(len(list1)) if i % 2 != 0]
    list2 = [list2[i] for i in range(len(list2)) if i % 2 == 0]

    list1.extend(list2)
    
    print(list1)

def remove_and_add():
    list1 = [54, 44, 27, 79, 91, 41]
    ex = list1.pop(4)
    
    print('List after removing element at index 4 -->', end=' ')
    print(list1)

    list1.insert(2, ex)
    print('List after inserting element at index 2 -->', end=' ')
    print(list1)

    list1.append(ex)
    print('List after inserting element at the end of the list -->', end=' ')
    print(list1)

# Problems map is a dictionary mapping the serial number with its solver function.

problems = {
    '1': merge_lists,
    '2': remove_and_add
}

# main() is the root function from where the other functions are called
# depending on problem number provided in selection

def main():
    global problems
    option = input('Selection: ')

    problems[option]()

main() # Run the root function.