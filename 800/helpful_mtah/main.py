import re

s = input()

numbers = sorted(re.findall(r'\d+', s))
s = re.sub(r'\d+', lambda x : numbers.pop(0), s)

print(s)
