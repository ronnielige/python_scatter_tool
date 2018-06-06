__author__ = 'lr9371'
'''
This script is used to extract information from log file and show them with graph.
Note: The log File must adhere to a certain format as follows:
log2width = 5  realbits =   350  estbits =   330  diff_ratio = 0.05714
log2width = 4  realbits =   126  estbits =    96  diff_ratio = 0.23810
log2width = 3  realbits =    50  estbits =    35  diff_ratio = 0.30000
'''

import numpy
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import sys

# set title names and category values by user
category_title = "log2width"
category_array = [5,  4,  3,  2]
x_title        = "realbits"
y_title        = "estbits"

def showhelp():
    print "Usage:"
    print "    python  %s  input.log"%__file__

def extract_info(inf_name, category_array):
    x_array = []
    y_array = []
    for cat_value in category_array: # init x_array and y_array
        x_array.append([])
        y_array.append([])

    inf      = open(inf_name, 'r')
    line     = inf.readline()
    while line:
        cat_pos = line.find(category_title)
        if cat_pos >= 0:
            x_pos = line.find(x_title)
            y_pos = line.find(y_title)
            if x_pos < 0 or y_pos < 0:
                print "Encounter an abnormal line: %s, can't find %s or %s"%(line[:-1], x_title, y_title)
                line = inf.readline()
                continue
            cat_value = (int)(line[cat_pos:].split()[2])
            cat_idx   = category_array.index(cat_value)
            x_value   = (int)(line[x_pos:].split()[2])
            y_value   = (int)(line[y_pos:].split()[2])
            x_array[cat_idx].append(x_value)
            y_array[cat_idx].append(y_value)
        line = inf.readline()

    return x_array, y_array

def plot_arrays(x_array, y_array, category_array):
    font_set = FontProperties(fname=r"c:\windows\fonts\calibri.ttf", size=15)
    category_f0 = plt.figure(0)
    for cat_value in category_array:
        cat_idx = category_array.index(cat_value)
        ax      = plt.subplot(2, 2, cat_idx + 1)
        plt.xlabel(x_title, fontproperties=font_set, fontsize = 14)
        plt.ylabel(y_title, fontproperties=font_set, fontsize = 14)
        plt.title(category_title + " = %s"%cat_value, fontproperties=font_set, fontsize = 14)
        plt.scatter(x_array[cat_idx], y_array[cat_idx], c='red', marker='+')
        plt.grid(True)
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        showhelp()
    inf_name = sys.argv[1]

    x_array, y_array = extract_info(inf_name, category_array)
    plot_arrays(x_array, y_array, category_array)
