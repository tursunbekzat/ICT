h = int(input("Height of the pyramid: "))
ch = input("Character: ")

for i in range(h):
    if i == 0: 
        print(' ' * (h-1), ch, sep='')
    elif i == 1: 
        print(' ' * (h - i - 2), '/ \\')
    elif i == h - 1: 
        print('/', '_'*(h*2-3), '\\', sep='')
    else: 
        print(' ' * (h - i - 2), '/', ' ' * (i * 2 - 3), '\\')