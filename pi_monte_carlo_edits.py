# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 15:47:27 2022

Script for estimating pi using monte carlo simulation
"""
import numpy as np
import matplotlib.pyplot as plt
import math
from time import perf_counter

def pi_estimate(counts):
    
    inside_count = 0
    inside_x = np.array([])
    inside_y = np.array([])
    outside_x = np.array([])
    outside_y = np.array([])
    
    for i in range(counts):
        
        x = np.random.uniform(-1, 1)
        y = np.random.uniform(-1, 1)
        radius = np.sqrt(x**2 + y**2)
        
        if (radius<1):
        #true for if inside circle 
            inside_x = np.append(inside_x, x)
            inside_y = np.append(inside_y, y)
            inside_count += 1

        elif (radius>1):
            outside_x = np.append(outside_x, x)
            outside_y = np.append(outside_y, y)

    #pi is the area of a circle with a radius of 1
    pi_estimatation = 4 * inside_count / counts
    return pi_estimatation, inside_x, inside_y, outside_x, outside_y

def plot_circle(counts):

    pi, inside_x, inside_y, outside_x, outside_y = pi_estimate(counts)
    print("The estimate of pi for ", counts, " counts is ", pi)
    plt.figure(figsize=(5, 5))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.scatter(inside_x, inside_y)
    plt.scatter(outside_x, outside_y)
    plt.Circle((0, 0), 0.5, color='r')
    plt.title("Accepted or rejected points for a circle of radius 1")
    plt.show()
    
    return None

def pi_varying_counts(counts_array):
    
    pi_array = np.array([])

    for counts in counts_array:
        
        estimate_values = pi_estimate(counts)
        pi_array = np.append(pi_array, estimate_values[0])
        
    return pi_array

def plot_counts_pi(counts_array, pi_array):
    
    plt.figure(figsize=(5,5))
    plt.plot(counts_array, pi_array)
    plt.title('Pi Estimate vs Number of Counts')
    plt.xlabel('Number of Counts')
    plt.ylabel('Pi Estimate')
    plt.axhline(y=math.pi, color='r')
    plt.show()
    
    return None

number_counts = 10000
plot_circle(number_counts)

#start the counter for checking runtime for varying the number of counts
time_start = perf_counter()
number_counts_array = np.arange(1, 10000, 100)
pi_estimates = pi_varying_counts(number_counts_array)
time_end = perf_counter()

plot_counts_pi(number_counts_array, pi_estimates)
print("Total runtime to find all Pi Estimates is  {0:0.5f} seconds".format(
        time_end-time_start))