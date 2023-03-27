def printTasks(tasks): 
    print("\nHere is the list:")
    for i in tasks: print("       - ", i)
    print()

tasks = []
printTasks(tasks)
task = input('What do you want to add:\n')

while task.lower() != 'nothing':
    tasks.append(task)
    printTasks(tasks)
    task = input('What do you want to add:\n')

printTasks(tasks)
print('Goodbye')