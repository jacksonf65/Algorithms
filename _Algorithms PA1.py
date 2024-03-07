# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 15:15:15 2024

@author: JRFRIZZELL
"""

#PA1

import random
from tabulate import tabulate
from time import time

# def problem_1():
#     origin_count = 0
#     for i in range(100):
#         particle = 0
#         for j in range(20):
#             particle += random.choice([-1,1])
#             if particle == 0:
#                 origin_count += 1
#                 break
#     return origin_count 

# def problem_2a():
#     origin_count = 0
#     for i in range(100):
#         particle = [0,0]
#         current_dimension = -1
#         for j in range(20):
#             current_dimension = random.choice([0,1])
#             particle[current_dimension] += random.choice([-1,1])
#             if particle[0] == 0 and particle[1] == 0:
#                 origin_count += 1
#                 break
#     return origin_count
   
# def problem_2b():
#     origin_count = 0
#     for i in range(100):
#         particle = [0,0,0]
#         current_dimension = -1
#         for j in range(20):
#             current_dimension = random.choice([0,1,2])
#             particle[current_dimension] += random.choice([-1,1])
#             if particle[0] == 0 and particle[1] == 0 and particle[2] == 0:
#                 origin_count += 1
#                 break
#     return origin_count

# def problem_3a():
#     for i in range(1,7):
#         origin_count = 0
#         for i in range(100):
#             particle = 0
#             for k in range(2 * 10 ** i):
#                 particle += random.choice([-1,1])
#                 if particle == 0:
#                     origin_count += 1
#                     break
#         print(origin_count)
        
# def problem_3b():
#     for i in range(1,7):
#         origin_count = 0
#         for j in range(100):
#             particle = [0,0]
#             for k in range(2 * 10 ** i):
#                 current_dimension = random.choice([0,1])
#                 particle[current_dimension] += random.choice([-1,1])
#                 if particle[0] == 0 and particle[1] == 0:
#                     origin_count += 1
#                     break
#         print(origin_count)
        
# def problem_3c():
#     for i in range(1,7):
#         origin_count = 0
#         for j in range(100):
#             particle = [0,0,0]
#             for k in range(2 * 10 ** i):
#                 current_dimension = random.choice([0,1,2])
#                 particle[current_dimension] += random.choice([-1,1])
#                 if particle[0] == 0 and particle[1] == 0 and particle[2] == 0:
#                     origin_count += 1
#                     break
#         print(origin_count)
        
def n1():
    counts = []
    for i in range(1,7):
        origin_count = 0
        for i in range(100):
            particle = 0
            for k in range(2 * 10 ** i):
                particle += random.choice([-1,1])
                if particle == 0:
                    origin_count += 1
                    break
        counts.append(str(origin_count) + " %")
    return counts
    
def n2():
    counts = []
    for i in range(1,7):
        origin_count = 0
        for j in range(100):
            particle = [0,0]
            for k in range(2 * 10 ** i):
                current_dimension = random.choice([0,1])
                particle[current_dimension] += random.choice([-1,1])
                if particle[0] == 0 and particle[1] == 0:
                    origin_count += 1
                    break
        counts.append(str(origin_count) + " %")
    return counts
        
def n3():
    counts = []
    times = []
    for i in range(1,7):
        start_time = time()
        origin_count = 0
        for j in range(100):
            particle = [0,0,0]
            for k in range(2 * 10 ** i):
                current_dimension = random.choice([0,1,2])
                particle[current_dimension] += random.choice([-1,1])
                if particle[0] == 0 and particle[1] == 0 and particle[2] == 0:
                    origin_count += 1
                    break
        end_time = time()
        counts.append(str(origin_count) + " %")
        times.append(round(end_time - start_time, 4))
    return counts, times

def percent_table(r1, r2, r3):
    data = [["1D", r1[0], r1[1], r1[2], r1[3], r1[4], r1[5]],
            ["2D", r2[0], r2[1], r2[2], r2[3], r2[4], r2[5]],
            ["3D", r3[0], r3[1], r3[2], r3[3], r3[4], r3[5]]]
    headers = ["Number of steps: ", "20", "200", "2,000",
               "20,000", "200,000", "2,000,000"]
    table = tabulate(data, headers)
    return table

def time_table(r):
    
    data = [["3D", r[0], r[1], r[2], r[3], r[4], r[5]]]
    headers = ["Number of steps: ", "20", "200", "2,000",
               "20,000", "200,000", "2,000,000"]
    table = tabulate(data, headers)
    return table

def main():
    
    results1 = n1()
    results2 = n2()
    results3 = n3()[0]
    results4 = n3()[1]
    
    print("Percentages of time particle returned to origin:")
    print(percent_table(results1, results2, results3))
    
    print("\nRun time (seconds):")
    print(time_table(results4))
    
main()
            