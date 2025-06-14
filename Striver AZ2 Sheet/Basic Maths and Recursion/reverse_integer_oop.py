import sys
import os
import math

class IntegerReverser:
    INT_MIN = -2**31
    INT_MAX = 2**31 - 1

    def __init__(self, input_file, output_file):
        base_path = os.path.dirname(__file__)
        self.input_path = os.path.join(base_path, input_file)
        self.output_path = os.path.join(base_path, output_file)

    def read_input(self):
        with open(self.input_path, 'r') as file:
            return int(file.read().strip())

    def write_output(self, result):
        with open(self.output_path, 'w') as file:
            file.write(str(result))

    def is_within_32bit_signed_int_range(self, n):
        return self.INT_MIN <= n <= self.INT_MAX

    def reverse_integer(self, n):
        neg = n < 0
        n = abs(n)
        rev = 0

        while n != 0:
            n, rem = divmod(n, 10)
            rev = rev * 10 + rem

        if neg:
            rev = -rev

        if not self.is_within_32bit_signed_int_range(rev):
            return 0

        return rev

    def reverse_integer_less_lines(self, n):
        # List Indexing with Bolean
        # if negetive then [1,-1][1] which is the 2nd value in list i.e -1
        sign=[1,-1][n<0]
        rev,x=0,abs(n)

        while x:
            # divmod will do // and % and store in a tuple
            x,mod=divmod(x,10)
            rev=rev*10 +mod
            if rev> 2**31-1:
                return 0
        return sign*rev



    def process(self):
        n = self.read_input()
        result = self.reverse_integer_less_lines(n)
        self.write_output(result)

if __name__ == "__main__":
    reverser = IntegerReverser('../input.txt', '../output.txt')
    reverser.process()