def isPrime(n):
    for i in range(2, n):
        if n % i == 0: 
            print(n // i, i)
            return False
    return True

n = int(input())
if(isPrime(n)): print("It is prime number")
