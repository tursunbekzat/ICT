def add(key, value):
    dict[key] = value

def delete(key):
    if len(dict) == 0 or key not in dict:
        print("Dictionary is empty or key is not found!")
        return
    dict.pop(key)

def show():
    print("here is dictionary:")
    for x in dict:
        print('        -', x, ':', dict[x])

dict = {}
while True:
    operation = input("What do you want to do: add/delete/exit?\n")
    if operation == 'add':   add(input("Enter the key:\n"), input("Enter the value:\n"))
    elif operation == 'delete': delete(input("Enter the key:\n"))
    else: break
    show()
        