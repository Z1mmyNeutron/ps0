def find_extreme_divisors(n1, n2):
    min_val, max_val = None, None
    for i in range(2, min(n1,n2)+1):
        if n1%i == 0 and n2%i == 0:
            if min_val == None:
                min_val = i
            max_val = i
    return min_val, max_val

min_divisor, max_divisor = find_extreme_divisors(100,200)
print(min_divisor, max_divisor)

t1 = (1,2,3,4,5,6,7,8,9,10)
def find_mean(t1):
    summed = 0
    for elm in t1:
        summed += elm
    return summed / len(t1)

def better_find_mean(t1):
    total_sum = sum(t1)
    count = len(t1)
    return total_sum / count
print(better_find_mean(t1))

l = [1,2,3]
l.append(l)
print(l is l[-1])

non_primes = [x for x in range(2, 101) if any(x % y == 0 for y in range(2, int(x**0.5) + 1))]
print(non_primes)

for i in map(lambda x: x**2, [2,6,4]):
    print(i)

l1 = [1,2]
l2 = [2,3]
def f(l1, l2):
    return sum(x**y for x, y in zip(l1,l2))
print(f(l1,l2))


d = {'x': 11, 'b': 12, 'a': 5, 'c' :22}
def minKey(d):
    min_key = min(d.keys())
    return d[min_key]
print(minKey(d))
# Example definition of Don_Quixote (book dictionary)
Don_Quixote = {
    1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j',
    11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't',
    21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z', 27: ' ', 28: '.', 29: ',', 30: '!',
    31: 'A', 32: 'B', 33: 'C', 34: 'D', 35: 'E', 36: 'F', 37: 'G', 38: 'H', 39: 'I', 40: 'J',
    41: 'K', 42: 'L', 43: 'M', 44: 'N', 45: 'O', 46: 'P', 47: 'Q', 48: 'R', 49: 'S', 50: 'T',
    51: 'U', 52: 'V', 53: 'W', 54: 'X', 55: 'Y', 56: 'Z', 57: '-', 58: ';', 59: '?', 60: ':',
    61: '(', 62: ')', 63: '[', 64: ']', 65: '{', 66: '}', 67: '+', 68: '-', 69: '*', 70: '/',
    71: '@', 72: '#', 73: '$', 74: '%', 75: '^', 76: '&', 77: '_', 78: '=', 79: '|', 80: '~'
}

# Define the gen_decode_keys lambda function
gen_decode_keys = lambda book, cipher_text: {s: book[int(s)] for s in cipher_text.split('*')}

# Example cipher text
cipher_text = '22*13*33*137*59*11*23*11*1*57*6*13*1*2*6*57*2*6*1*22*13*33*137*59*11*23*11*1*57*6*173*7*11'

# Call the function and print the result
decoded_keys = gen_decode_keys(Don_Quixote, cipher_text)
print(decoded_keys)
