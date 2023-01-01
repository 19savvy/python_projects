import random
while True:
    try:
        secret_number = random.randint(1,10)
        guess = int(input("enter a number between 1 and 10: "))
    except ValueError:
        print("enter a number")  
        continue 
    else:
        break
guesses = 1   

while guess != secret_number:
    if guess > 10:
        print("the number you entered is greater than 10")
    if guess < 1:
        print("the number you entered is less than 1")
    if guess < secret_number:
        print("the number you have entered is less try a higher number")        
    elif guess > secret_number:
        print("the number you input is high, try a lesser number")
    guess = int(input("enter a number between 1 and 10: "))
    guesses += 1
    
     
if guess == secret_number:
    print("Correct, you got the answer right in {} tries.".format(guesses))