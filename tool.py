import numpy
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

def extract_info(inf_name, category_array, category_title, x_title, y_title):
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

def plot_arrays(x_array, y_array, category_array, category_title, x_title, y_title):
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