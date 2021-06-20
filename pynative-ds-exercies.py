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

def reverse_sliced_chunks():
    list1 = [11, 45, 8, 23, 14, 12, 78, 45, 89]

    def slice_it(arr):
        if len(arr) <= 3:
            print(arr)
            return

        res = arr[:3]
        res.reverse()
        print(res)
        slice_it(arr[3:])

    slice_it(list1)

def count_elements():
    list1 = [11, 45, 8, 11, 23, 45, 23, 45, 89]

    res = dict.fromkeys(list1, 0)

    for x in res.keys():
        c = list1.count(x)
        res[x] = c

    print(res)
    

def list_to_set():
    list1 = [2, 3, 4, 5, 6, 7, 8]
    list2 = [4, 9, 16, 25, 36, 49, 64]

    its = zip(list1, list2)
    print(tuple(its))

def set_intersection():
    set1 = {65, 42, 78, 83, 23, 57, 29}
    set2 = {67, 73, 43, 48, 83, 57, 29}

    set3 = set1.intersection(set2)

    print('Intersection result: ', end=' ')
    print(set3)

    set4 = set1.difference(set2)
    print('Difference: ', end=' ')
    print(set4)

def subset_superset():
    set1 = {27, 43, 34}
    set2 = {34, 93, 22, 27, 43, 53, 48}

    subset = {}

    if set1.issubset(set2):
        print('set1 is subset of set2');
        set1.clear()
        print('set1 = ' + str(set1))
        print('set2 = ' + str(set2))
    elif set2.issubset(set1):
        print('set2 is subset of set1');
        set2.clear()
        print('set2 = ' + str(set2))
        print('set1 = ' + str(set1))

def pop_from_list():
    list1 = [47, 64, 69, 37, 76, 83, 95, 97]
    dict1 = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}

    vals = dict1.values()

    for x in list1:
        if x not in vals:
            list1.remove(x)
    
    print(list1)

def non_duplicate_list():
    dict1 = {'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53, 'july':54, 'Aug':44, 'Sept':54}
    res = []
    
    for x in dict1.values():
        if x not in res:
            res.append(x)
    
    print(res)

def tuple_min_max():
    list1 = [87, 45, 41, 65, 94, 41, 99, 94]
    t1 = tuple(set(list1))

    print('Unique List: ' + str(t1))
    list1.sort()

    print('Min: ' + str(list1[0]))
    print('Max: ' + str(list1[len(list1)-1]))

# Problems map is a dictionary mapping the serial number with its solver function.

problems = {
    '1': merge_lists,
    '2': remove_and_add,
    '3': reverse_sliced_chunks,
    '4': count_elements,
    '5': list_to_set,
    '6': set_intersection,
    '7': subset_superset,
    '8': pop_from_list,
    '9': non_duplicate_list,
    '10': tuple_min_max
}

# main() is the root function from where the other functions are called
# depending on problem number provided in selection

def main():
    global problems
    option = input('Selection: ')

    problems[option]()

main() # Run the root function.