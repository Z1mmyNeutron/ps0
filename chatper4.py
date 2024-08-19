def mult(*args):
    if len(args) == 1:
        return args[0]
    else:
        return args[0] * args[1]

print(mult(4,5))
print(mult(3))

def mean(*args):
    tot = 0
    for a in args:
        tot += a
    return tot/len(args)

print(mean(7,6,5,24,5))

def scoping(x):
    y = 1
    x = x + y
    print('x=', x)
    return x
x = 3
y = 2
z = scoping(x)
print('z =', z)
print('x =', x)
print('y =', y)


def create_eval_ans():
    power = input("Enter a positive integer: ")
    return lambda ans: ans**int(power)


def bisection_solve(x, eval_ans, epsilon, low, high):
    ans = (high + low) / 2
    while(eval_ans(ans) - x ) >= epsilon:
        if eval_ans(ans) < x:
            low = ans
        else:
            high = ans
        ans = (high + low)/2
    return ans

def log(x, base, epsilon):
    def find_log_bounds(x, base):
        upper_bound = 0
        while base**upper_bound < x:
            upper_bound += 1
        return upper_bound -1, upper_bound
    low, high = find_log_bounds(x, base)
    return bisection_solve(x, lambda ans: base**ans, epsilon, low, high)

low = 1
high = 1000

divide = lambda x, y: None if y == 0 else x/y
print(divide(2,3))
print(divide(5,0))

eval_ans = create_eval_ans()
print(f"bisection solve: {bisection_solve(99, eval_ans, .01, low, high)}")
print(f"log: {log(99, 2, .01)}")





