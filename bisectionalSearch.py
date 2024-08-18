low = 0
high = 100
epsilon = .01
guess = (high + low) / 2.0
numGuesses = 0

answer = float(input("Enter a number: "))
while abs(guess - answer) >= epsilon:
    if guess < answer:
        low = guess
    else: 
        high = guess
    guess = (high + low)/2.0
    numGuesses += 1
print(guess, numGuesses, answer)