#1. for memory optimization
#2. generating values according to us.
#3. use yield keyword
#4. Maintain state(maintain stack frame) fo function

def generateValues(n):
    for i in range(1,n+1):
        yield i

res = generateValues(11)

print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
