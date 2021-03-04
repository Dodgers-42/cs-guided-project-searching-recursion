# Function Call Stack
#
def foo():
    print("function 1")
    return 

def bar():
    print("function 2")
    return

def baz():
    foo()
    bar()
    return


#2
def foo(a):
    return a * a

def bar():
    print("function 2")
    return

def baz():
    new_value = foo(10)
    return new_value
    
print(bar())

# Fibonacci sequence
# 0, 1,1,2,3,5,8,13

#Return the Nth fibonacci number 
def fib(n):
    if n <= 1:
        return n

    return fib(n-1) + fib(n-2)



print(fib(0)) # return 0
print(fib(1)) # return 1
print(fib(2))

# Or...

def fib(n):
    if n <= 1:
        return n

    else:
        n_minus_1 = fib(n-1)
        n_minus_2 = fib(n-2)
        return n_minus_1 + n_minus_2


print(fib(2)) # return 1
