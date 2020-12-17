import matplotlib.pyplot as plt
import numpy as np

def create_histogram(x, title, x_label):
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
    plt.figure()
    plt.boxplot(x, vert=False)
    plt.yticks([])
    plt.title("Box and Whisker Plot for " + label)
    plt.xlabel(label)
    plt.show()
    plt.close()