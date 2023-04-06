f = open('text.txt', 'r')
num1 = int(f.readline())
num2 = int(f.readline())
num3 = int(f.readline())
f.close()

result = num1 * num2 - num3

with open('text.txt', 'a') as f:
    f.write('\n'+str(result))