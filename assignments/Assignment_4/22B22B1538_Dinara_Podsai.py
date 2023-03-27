def show(tasks): 
    for i in tasks: print("       - ", i)
    print()

print("Here is the list:")
list_of_tasks = []
show(list_of_tasks)
task = input('What do you want to add:\n')

while task.lower() != 'nothing':
    list_of_tasks.append(task)
    print("\nHere is the list:")
    show(list_of_tasks)
    task = input('What do you want to add:\n')

print("\nHere is the list:")
show(list_of_tasks)
print('Goodbye')