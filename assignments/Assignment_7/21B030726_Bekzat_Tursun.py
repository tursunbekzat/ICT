def show_dict(): 
    print("here is dictionary:")
    for key in key_value: print('        -', key, ':', key_value[key])

def add(key, value): key_value[key] = value

def delete(key):
    if len(key_value) == 0:    print("dictionary is empty!")
    elif key not in key_value: print("key is not found!")
    else:                 key_value.pop(key)

key_value = {}
while True:
    case = input("what do you want to do: add/delete/exit?\n")
    if case == 'add':   add(input("enter the key:\n"), input("enter the value:\n"))
    elif case == 'delete': delete(input("enter the key:\n"))
    elif case == 'exit': break
    else: 
        print("try again!")
        continue
    show_dict()
        