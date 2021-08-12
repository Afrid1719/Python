import json
from json import JSONEncoder

def convert_dict_to_json():
    data = {"key1": "value1", "key2": "value2"}
    json_data = json.dumps(data)
    print(json_data)

def access_json_key():
    json_data = """{"key1": "value1", "key2": "value2"}"""
    data = json.loads(json_data)
    print(data['key2'])

def pretty_print_json():
    data = {"key1": "value1", "key2": "value2"}
    json_data = json.dumps(data, indent=2, separators=(',', ' = '))
    print(json_data)

def sort_json_keys_and_write_to_file():
    data = {"id" : 1, "name" : "value2", "age" : 29}
    print('Start writing json data to file')
    with open('test_json.json', 'w') as out_file:
        json.dump(data, out_file, indent=4, sort_keys=True)
    print('Done writing json data to file')

def print_nested_value():
    json_data = """{ 
        "company":{ 
            "employee":{ 
                "name":"emma",
                "payble":{ 
                    "salary":7000,
                    "bonus":800
                }
            }
        }
    }"""
    data = json.loads(json_data)
    print(data['company']['employee']['payble']['salary'])

class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price

class VehicleEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

def VehicleDecoder(obj):
    return Vehicle(obj['name'], obj['engine'], obj['price'])

def object_to_json():
    vehicle = Vehicle("Toyota Rav4", "2.5L", 32000)
    json_data = json.dumps(vehicle, indent=4, cls=VehicleEncoder)
    print(json_data)

def json_to_object():
    json_data = '{ "name": "Toyota Rav4", "engine": "2.5L", "price": 32000 }'
    data = json.loads(json_data, object_hook=VehicleDecoder)
    print('Type of decoded object: ' + str(type(data)))
    print('Vehicle object:')
    print(data.name, data.engine, data.price)

def validate_json():
    InvalidJsonData = """{ "company":{ "employee":{ "name":"emma", "payble":{ "salary":7000 "bonus":800} } } }"""
    try:
        json.loads(InvalidJsonData)
        print('Valid json data')
    except ValueError:
        print('Invalid JSON data')

def parse_json():
    json_data = """[ 
        { 
            "id":1,
            "name":"name1",
            "color":[ 
                "red",
                "green"
            ]
        },
        { 
            "id":2,
            "name":"name2",
            "color":[ 
                "pink",
                "yellow"
            ]
        }
    ]"""
    
    try:
        data = json.loads(json_data)
    except Exception as e:
        print(e)
    
    dataList = [item['name'] for item in data]
    print(dataList)

# Problems map is a dictionary mapping the serial number with its solver function.

problems = {
    '1': convert_dict_to_json,
    '2': access_json_key,
    '3': pretty_print_json,
    '4': sort_json_keys_and_write_to_file,
    '5': print_nested_value,
    '6': object_to_json,
    '7': json_to_object,
    '8': validate_json,
    '9': parse_json
}

# main() is the root function from where the other functions are called
# depending on problem number provided in selection

def main():
    global problems
    option = input('Selection: ')

    problems[option]()

main() # Run the root function.