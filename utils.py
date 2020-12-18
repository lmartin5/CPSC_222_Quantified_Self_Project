'''
Programmer: Luke Martin
Class: CPSC 222-01, Fall 2020
Quantified Self Project utils file
9/27/2020

Description: This file contains the functions used in my Technical Report.
It includes the two main visualization functions.
'''

import matplotlib.pyplot as plt
import numpy as np

def create_histogram(x, title, x_label):
    '''
    Creates a histogram with the mean displayed, used in CPSC 222 Project
    Paramter x: the data to be charted
    Parameter title: the title of the histogram
    Parameter x_label: the x-label of the histogram
    Returns: the histogram is plotted and shown in the notebook
    '''
    x_mean = np.mean(x)
    plt.figure()
    # return tuple of plt.hist in matplotlib documentation
    hist_values = plt.hist(x, bins=15, color="#add8e6", edgecolor="black")
    plt.plot([x_mean, x_mean], [0, hist_values[0].max()], ls="dashed", color="black", lw=3, label="Mean: %.2f" %(x_mean))
    plt.title(title)
    plt.ylabel("Frequency")
    plt.xlabel(x_label)
    plt.legend()
    plt.show()
    plt.close()

def create_box_plot(x, label):
    '''
    Creates a box and whisker plot, used in CPSC 222 Project
    Paramter x: the data to be charted
    Parameter label: the label of the data that will be used on x-label and title
    Returns: the box and whisker plot is plotted and shown in the notebook
    '''
    plt.figure()
    plt.boxplot(x, vert=False) # makes the plot horizontal
    plt.yticks([]) # removes y ticks on side
    plt.title("Box Plot for " + label)
    plt.xlabel(label)
    plt.show()
    plt.close()