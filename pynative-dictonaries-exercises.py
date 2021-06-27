def dict_from_list():
    keys = ['Ten', 'Twenty', 'Thirty']
    values = [10, 20, 30]

    dict1 = dict(zip(keys, values))
    print('Output: ' + str(dict1))

def merge_dicts():
    dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
    dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
    
    # Python 3.5+
    dict3 = {**dict1, **dict2}
    print('Output: ' + str(dict3))

    # Older versions
    # dict1.update(dict2)
    # print('Output :' + str(dict1))

def access_key_from_nested():
    sampleDict = { 
        "class":{ 
            "student":{ 
                "name":"Mike",
                "marks":{ 
                    "physics":70,
                    "history":80
                }
            }
        }
    }

    print('Output: ' + str(sampleDict['class']['student']['marks']['history']))

def dict_with_default_values():
    employees = ['Kelly', 'Emma', 'John']
    defaults = {"designation": 'Application Developer', "salary": 8000}

    res = dict.fromkeys(employees, defaults)

    print('Output: ' + str(res))

def dict_from_keys():
    dict1 = {
        "name": "Kelly",
        "age":25,
        "salary": 8000,
        "city": "New york"  
    }

    keys = ["name", "salary"]

    res = {
        keys[0]: dict1[keys[0]],
        keys[1]: dict1[keys[1]]
    }

    print('Output: ' + str(res))

def remove_keys():
    dict1 = {
        "name": "Kelly",
        "age":25,
        "salary": 8000,
        "city": "New york"  
    }
    keysToRemove = ["name", "salary"]

    for x in  keysToRemove:
        dict1.pop(x)

    print('Output: ' + str(dict1))

def value_exists():
    dict1 = {'a': 100, 'b': 200, 'c': 300}
    vals = list(dict1.values())

    if vals.count(200) > 0 :
        print('True')
    else:
        print('False')

def rename_key():
    dict1 = {
        "name": "Kelly",
        "age":25,
        "salary": 8000,
        "city": "New york"
    }

    dict1['location'] = dict1.pop('city')
    print(dict1)

def key_of_min_val():
    dict1 = {
        'Physics': 82,
        'Math': 65,
        'history': 75
    }

    print(min(dict1, key = dict1.get))

def change_nested_val():
    dict1 = {
        'emp1': {'name': 'Jhon', 'salary': 7500},
        'emp2': {'name': 'Emma', 'salary': 8000},
        'emp3': {'name': 'Brad', 'salary': 6500}
    }

    dict1['emp3']['salary'] = 8500
    print(dict1)
# Problems map is a dictionary mapping the serial number with its solver function.

problems = {
    '1': dict_from_list,
    '2': merge_dicts,
    '3': access_key_from_nested,
    '4': dict_with_default_values,
    '5': dict_from_keys,
    '6': remove_keys,
    '7': value_exists,
    '8': rename_key,
    '9': key_of_min_val,
    '10': change_nested_val
}

# main() is the root function from where the other functions are called
# depending on problem number provided in selection

def main():
    global problems
    option = input('Selection: ')

    problems[option]()

main() # Run the root function.