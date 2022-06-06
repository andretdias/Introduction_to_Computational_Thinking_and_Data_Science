import random

#EXERCISE 3.1
def deterministicNumber():
    '''
    Deterministically generates and returns an even number between 9 and 21
    '''
    return 10


#EXERCISE 3.2
import random
def stochasticNumber():
    '''
    Stochastically generates and returns a uniformly distributed even number between 9 and 21
    '''
    a = -1
    while a%2 != 0:
        a = random.randint(10,21)
    return a

print(stochasticNumber())
print(stochasticNumber())
print(stochasticNumber())
print(stochasticNumber())
print(stochasticNumber())
print(stochasticNumber())
print(stochasticNumber())
print(stochasticNumber())
print(stochasticNumber())
print(stochasticNumber())
print(stochasticNumber())
print(stochasticNumber())
print(stochasticNumber())
print(stochasticNumber())
print(stochasticNumber())
print(stochasticNumber())