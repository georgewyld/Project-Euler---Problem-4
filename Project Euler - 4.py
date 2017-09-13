"""A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers."""
import time
def is_palindromic(x):
    x=str(x)
    y=x[::-1]
    if x==y:
        return True
    else: return False
factors=[]
palindromic=[]
start=time.time()
while True:
    for num in range(1,999*999):
        if is_palindromic(num):
            palindromic.append(num)
    palindromic=palindromic[::-1]
    while True:       
        for i in range(1,palindromic[0]+1): 
            if palindromic[0]%i==0:
                factors.append(i)       
        while len(factors)>2:
            factors.pop()
            factors.pop(0)
        factors=list(map(str,factors))       
        if len(factors[0])!=3:
            palindromic.pop(0)
            factors.clear()
            continue
        elif len(factors[1])!=3:
                 palindromic.pop(0)
                 factors.clear()
                 continue
        else:break
    break
elapsed=(time.time() -start)
print('Required answer:',factors[0],'x',factors[1],'=',palindromic[0])
print(elapsed)
