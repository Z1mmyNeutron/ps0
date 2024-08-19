def FizzBuzz(n):
    fizzbuzz = []
    for i in range(1, n+ 1):
        if i % 3 == 0 and i % 5 == 0:
            fizzbuzz.append("FizzBuzz")
        elif  i % 3 == 0:
            fizzbuzz.append("Fizz")
        elif i % 5 == 0:
            fizzbuzz.append("Buzz")
        else:
            fizzbuzz.append(str(i))
    return fizzbuzz


m = FizzBuzz(15)
print(f"fizzbuzz: {m}")

def fib(n):
    if n == 0: return 0
    if n == 1: return 1
    return fib(n-1) + fib(n-2)

print(f"Fibbanocci: {fib(5)}")

def is_palindrome(s):
    def to_chars(s):
        s = s.lower()
        letters = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                letters = letters + c
        return letters
    
    def is_pal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and is_pal(s[1:-1])
    return is_pal(to_chars(s))
print(f"is palindrome: {is_palindrome('racecar')}")
    
