"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
  if number_of_primes<1:
    raise ValueError("ValueError exception thrown")
  else:
    list = [2]
    numToTest=2
    while len(list)!=number_of_primes:
      numToTest+=1
  
      isPrime=True
  
      if numToTest%2:
        for i in range (3,(numToTest+1)//2,2):
          if numToTest%i==0: 
            isPrime=False
            break
        
        if isPrime:
          list.append(numToTest)
  
    return list
  
  
  	
  


