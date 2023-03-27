def diverders(div1, div2, numb):
    if div1 == 0 or div2 == 0:
        return False
    elif numb % div1 == 0 and numb % div2 == 0:
        return True
    return False

div1, div2, numb = int(input()), int(input()), int(input())
ans = diverders(div1, div2, numb)
print(ans)