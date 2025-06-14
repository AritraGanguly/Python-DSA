import sys
import os
import math

base_path = os.path.dirname(__file__)
sys.stdin = open(os.path.join(base_path, '../input.txt'), 'r')
sys.stdout = open(os.path.join(base_path, '../output.txt'), 'w')


n = int(input())
print(math.log10(n))

log=math.log10(n)

# +1 is to handle the case when n is log of 10 like 100, 1000 which gives log100=2 but the no of digits are 3.
print(f"count of digits in {n} is {int(log)+1}")