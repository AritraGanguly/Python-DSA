import os
import math

class MathOperations:
    def __init__(self, input_file, output_file):
        base_path = os.path.dirname(__file__)
        self.input_path = os.path.join(base_path, input_file)
        self.output_path = os.path.join(base_path, output_file)

    def read_input(self):
        with open(self.input_path, 'r') as file:
            return [int(x) for x in file.read().strip().split()]

    def write_output(self, result):
        with open(self.output_path, 'w') as file:
            file.write(str(result))

    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def lcm(self, a, b):
        return abs(a * b) // self.gcd(a, b)

    def process(self):
        # Read input
        numbers = self.read_input()
        if len(numbers) != 2:
            raise ValueError("Input file must contain exactly two integers")

        a, b = numbers

        # Calculate GCD and LCM
        gcd_result = self.gcd(a, b)
        lcm_result = self.lcm(a, b)

        # Write output
        self.write_output(f"GCD: {gcd_result}, LCM: {lcm_result}")

if __name__ == "__main__":
    math_operations = MathOperations('../input.txt', '../output.txt')
    math_operations.process()