import random
def genEven():
    '''
    Returns a random even number x, where 0 <= x < 100
    '''
    a = -1
    while a%2 != 0:
        a = random.randint(0,99)
    return a

print(genEven())
print(genEven())
print(genEven())
print(genEven())
print(genEven())
print(genEven())
print(genEven())