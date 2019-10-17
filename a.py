import random


def fibonacci(x):
    print"the first %s fibonacci sequential numbers are:"%(str(x))
    first=1
    second=0
    sum=0
    number=0
    while number<x:
        sum=first + second
        second=first
        first=sum
        number+=1
        print str(first)

def prime(x):
    print"Prime numbers between 2 and",x,"are:"
    for num in range(2,x + 1):
       # prime numbers are greater than 1
       if num > 1:
           for i in range(2,num):
               if (num % i) == 0:
                   break
           else:
               print(num)

fibonacci(x=random.randrange(80))
print"\n \n \n \n \n"
prime(x=random.randrange(80))
