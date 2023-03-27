word = input("Hello! ")
i = 0
while word != 'Hello':
    i+=1
    if i <= 3:   word = input("You have to say hello to me!")
    elif i < 7:  word = input("I said hello, do you have something to say to me?")
    else:        word = input("I SAID HELLO, ANSWER HELLO!")
print("Thank you, how are you?")
    