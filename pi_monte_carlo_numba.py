# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 15:47:27 2022

Script for estimating pi using monte carlo simulation
"""
from time import perf_counter
import math
import numpy as np
import matplotlib.pyplot as plt
from numba import jit
@jit(nopython=True)
def pi_estimate(counts):

    inside_count = 0
    inside_x = []
    inside_y = []
    outside_x = []
    outside_y = []

    for _ in range(counts):

        x = np.random.uniform(-1,1)
        y = np.random.uniform(-1,1)
        radius = np.sqrt(x**2+y**2)

        if radius < 1:
        #true for if inside circle
            inside_x.append(x)
            
            inside_y.append(y)
            inside_count += 1

        else:
            outside_x.append(x)
            outside_y.append(y)

    #pi is the area of a circle with a radius of 1
    pi_estimatation = 4 * inside_count / counts
    #assert (inside_count+outside_count == counts)
    return pi_estimatation, inside_x, inside_y, outside_x, outside_y

def find_radius(x, y):
    return np.sqrt(x**2+y**2)

def generate_random_number(low, high):

    return np.random.uniform(low, high)

def plot_circle(inside_x, inside_y, outside_x, outside_y):

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

    plt.figure(figsize=(5, 5))
    plt.plot(counts_array, pi_array)
    plt.title('Pi Estimate vs Number of Counts')
    plt.xlabel('Number of Counts')
    plt.ylabel('Pi Estimate')
    plt.axhline(y=math.pi, color='r')
    plt.show()

    return None

def main():

    number_counts = 10000
    pi, inside_x, inside_y, outside_x, outside_y = pi_estimate(number_counts)
    print("The estimate of pi for ", number_counts, " counts is ", pi)
    plot_circle(inside_x, inside_y, outside_x, outside_y)

    #start the counter for checking runtime for varying the number of counts
    time_start = perf_counter()
    number_counts_array = np.arange(1, 10000, 100)
    pi_estimates = pi_varying_counts(number_counts_array)
    time_end = perf_counter()

    plot_counts_pi(number_counts_array, pi_estimates)
    print("Total runtime to find all Pi Estimates is  {0:0.5f} seconds".format(
        time_end-time_start))

    return 1

if __name__ == '__main__':
    main()
