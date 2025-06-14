import sys
import os
import math

base_path = os.path.dirname(__file__)
sys.stdin = open(os.path.join(base_path, '../input.txt'), 'r')
sys.stdout = open(os.path.join(base_path, '../output.txt'), 'w')

n=int(input())
print(n)