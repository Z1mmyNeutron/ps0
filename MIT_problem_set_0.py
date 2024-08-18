low = 0
high = 100
epsilon = .01
num_guesses = 0
guess = (high + low) / 2.0

answer = float(input("Enter a number: "))
while abs(guess - answer) >= epsilon:
    if guess < answer:
        low = guess
    else:
        high = guess
    guess = (high + low) / 2.0
    num_guesses += 1
print(num_guesses, guess, answer)
