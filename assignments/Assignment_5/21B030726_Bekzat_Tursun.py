def diverders(div1, div2, numb):
    if div1 * div2  == 0:return False
    return numb % div1 == 0 and numb % div2 == 0
print(diverders(int(input()), int(input()), int(input())))