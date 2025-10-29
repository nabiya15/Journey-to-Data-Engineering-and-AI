import re

print(sum(int(num) for num in re.findall('[0-9]+', open('actualData.txt').read())))