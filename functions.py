def isEvenWithoutReturn(i):
    print("without return")
    i % 2 == 0

def isEven(i):
    return i % 2 == 0

def isEvenWithReturn(i):
    print("with return")
    remainder = i % 2
    return remainder == 0


def bisectional(target, low, high, epsilon = 0.01):
    while abs(high - low) > epsilon:
        mid = (high + low) /2
        if mid > high:
            high = mid
        else:
            low = mid
    return (high + low) /2

s = 'dictation'
def char_counts(s):
    vowels = 'aeiou'
    (c, v) = (0,0)
    if len(s) == 0:
        return None
    for letter in s:
        if letter in vowels:
            v += 1
        else:
            c +=1
    return (v, c)
print(char_counts(s))
    
def mean(*args):
    total = sum(args)
    length = len(args)
    return total/length
print(f"the mean is {mean(4,5,6,2,9,0,10,22,21,34)}")

L = [1,2,3,4,5,6,7,8,9,10]
def sum_and_product(L):
    sumElements = sum(L)
    products = 1
    for e in L:
        products *= e
    return (sumElements, products)
print(f"The sum and products are: {sum_and_product(L)}")
