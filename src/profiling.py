############################################################################
# @file profiling.py
# @brief Calculator math library for IVS 2025
# @date 15.4.2025
# @author: Filip Figúr <xfigurf00>
#
# Profiling for math_library.py - calculating standard deviation
# (https://en.wikipedia.org/wiki/Standard_deviation), (https://cs.wikipedia.org/wiki/Směrodatná_odchylka)
# How to run the program: python3 profiling.py < <file.txt>
############################################################################
import sys
from math_library import add, sub, multiply, divide, power, n_root

def data_extractor(data):
    for line in sys.stdin:
        line = line.strip()
        if line:
            parts = line.split()
            for part in parts:
                num = int(part)
                data.append(num)  
    return data

def calculate_average(data,count):
    total = 0
    for num in data:
        total = add(total,num)
    average = (total/count)
    return average

def formula_core(data,average):
    total = 0
    avg_power = power(average,2)
    for num in data:
        num_power = power(num,2)
        part_sub = sub(num_power,avg_power)
        total = add(total,part_sub)
    return total

def finito(core,count):
    fraction = divide(1,count-1)
    under_square_root = multiply(fraction,core)
    result = n_root(under_square_root,2)
    return result

def main():
    data = [] # storing each number value
    data_extractor(data)
    count = len(data) # number of lines = how many numbers are there (N)
    #print(f"data = {data}")
    #print(f"count = {count}")
    average = calculate_average(data,count)
    #print(f"average = {average}")
    core = formula_core(data,average)
    #print(f"Core = {core}")
    standard_deviation = finito(core,count)
    print(f"standard deviation = {standard_deviation}")
    
if __name__ == "__main__":
    import cProfile
    cProfile.run("main()")
