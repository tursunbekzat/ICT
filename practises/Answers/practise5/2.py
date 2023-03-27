start, end, step = int(input()), int(input()), int(input())
for i in range(start, end, step):
    if(i < end - step): print(i, end="-")
    else: print(i)
        