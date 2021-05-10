import random
from datetime import datetime

time_start = datetime.now()

l = [random.randrange(100, 999) for i in range(100000000)]

squared = [x**2 for x in l]
sqrt = [x**0.5 for x in l]
mul = [x * y for x, y in zip(squared, sqrt)]
div = [x / y for x, y in zip(squared, sqrt)]
int_div = [x // y for x, y in zip(squared, sqrt)]

time_end = datetime.now()
print(f'TOTAL TIME = {(time_end - time_start).seconds} seconds')
