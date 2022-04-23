f1 = 1
f2 = 1

n = input("Input number: ")
n = int(n)

i = 0
while i < n - 2:
    fib = f1 + f2
    f1 = f2
    f2 = fib
    i += 1
    
print(f2)


f1 = 1
f2 = 1
n = input("Input number: ")
n = int(n) - 2

i = 0
while i < n:
    f1, f2 = f2, f1 + f2
    print(f2)
    n -= 1