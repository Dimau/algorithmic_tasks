# Uses python3
import sys

input_str = sys.stdin.read()
tokens = input_str.split()
a = int(tokens[0])
b = int(tokens[1])
print(a + b)
