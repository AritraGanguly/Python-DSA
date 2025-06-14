import sys
import os
import math

base_path = os.path.dirname(__file__)
sys.stdin = open(os.path.join(base_path, '../input.txt'), 'r')
sys.stdout = open(os.path.join(base_path, '../output.txt'), 'w')

n=int(input())
neg=False
if (n<0):
    neg=True
    n=abs(n)

min=-2**31
max=2**31-1
if n!=0:
    digits=int(math.log10(n)+1)

# 123, 321
rev=0
while n!=0:
    rem=n%10
    rev=rev+rem*(10**(digits-1))
    digits=digits-1
    n=n//10
if rev<min or rev>max:
    print(0)
else:
    if neg:
        print(-1*rev)
    else:
        print(rev)