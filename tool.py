# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import numpy
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import os

def extract_info(inf_name, category_title, category_array, x_title, y_title):
    '''
    This function is used to extract information from log file and show them through graph.
    Note: The input log file must adhere to a certain format, for example:
    log2width = 5  realbits =   350  estbits =   330  diff_ratio = 0.05714
    log2width = 4  realbits =   126  estbits =    96  diff_ratio = 0.23810
    log2width = 3  realbits =    50  estbits =    35  diff_ratio = 0.30000
    Then category_title is log2width, category_array = [5, 4, 3], x_title = 'realbits', y_title = 'estbits'
    '''
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

            try: # in case cat_value don't exist in predefined array
                cat_value = (int)(line[cat_pos:].split()[2])
                cat_idx   = category_array.index(cat_value)
            except Exception, e:
                print "Found a category value %d which don't exist in category_array"%cat_value
                line = inf.readline()
                continue

            x_value   = (int)(line[x_pos:].split()[2])
            y_value   = (int)(line[y_pos:].split()[2])
            x_array[cat_idx].append(x_value)
            y_array[cat_idx].append(y_value)
        line = inf.readline()

    return x_array, y_array

def plot_arrays(x_array, y_array, category_title, category_array, x_title, y_title, out_img):
    font_set = FontProperties(fname=r"c:\windows\fonts\calibri.ttf", size=15)
    category_f0 = plt.figure(0, figsize=(20, 10))
    for cat_value in category_array:
        cat_idx = category_array.index(cat_value)
        ax      = plt.subplot(2, 2, cat_idx + 1)
        plt.xlabel(x_title, fontproperties=font_set, fontsize = 14)
        plt.ylabel(y_title, fontproperties=font_set, fontsize = 14)
        plt.xticks(fontsize=12)
        plt.yticks(fontsize=12)

        plt.title(category_title + " = %s"%cat_value, fontproperties=font_set, fontsize = 12)
        plt.scatter(x_array[cat_idx], y_array[cat_idx], c='red', marker='+')
        plt.grid(True)
    plt.subplots_adjust(left=0.123, right=0.9, bottom=0.1, top=0.9, wspace=0.2, hspace=0.2)
    #plt.show()
    plt.savefig(out_img, format='pdf', dpi=150)

def CheckFile(FileName):
    if not os.path.exists(FileName):
        return 0
    return 1