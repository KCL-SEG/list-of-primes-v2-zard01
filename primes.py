"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def isPrime(numToTest):
    primeFlag=True
    if numToTest%2:
        for i in range (3,(numToTest+1)//2,2):
            if numToTest%i==0:
                primeFlag=False
                break
    return primeFlag

def primes(number_of_primes):
    if number_of_primes<1:
        raise ValueError("ValueError exception thrown")
    else:
        list = [2]
        numToTest=2
        while len(list)!=number_of_primes:
            numToTest+=1
            if isPrime(numToTest):
                list.append(numToTest)
    return list
