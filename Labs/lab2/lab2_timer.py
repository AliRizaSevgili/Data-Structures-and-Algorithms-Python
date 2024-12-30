#
#   Author: Catherine Leung
#   This timer file performs a timing of the functions provided in lab2.py
#

import time
import random
from lab2 import partb_one, partb_two, partb_three

AMOUNT_OF_DATA = 1000

# generate a list of unique random numbers (AMOUNT_OF_DATA unique values)
my_list = random.sample(range(1, AMOUNT_OF_DATA*10), AMOUNT_OF_DATA)
my_list2 = my_list.copy()
my_list3 = my_list.copy()

total_time = 0

# generate an odd number as the target
target = random.randint(1,AMOUNT_OF_DATA*10-1)
if target % 2 == 0:
    target += 1  


start_time = time.perf_counter()
result = partb_one(my_list, target)
end_time = time.perf_counter()
total_time = (end_time-start_time)
print(f"time for partb_one()= {total_time}")


start_time = time.perf_counter()
result = partb_two(my_list, target)
end_time = time.perf_counter()
total_time = (end_time-start_time)
print(f"time for partb_two()= {total_time}")

start_time = time.perf_counter()
result = partb_three(my_list, target)
end_time = time.perf_counter()
total_time = (end_time-start_time)
print(f"time for partb_three()= {total_time}")

