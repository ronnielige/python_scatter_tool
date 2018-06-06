__author__ = 'lr9371'
'''
This script is used to extract information from log file and show them with graph.
Note: The log File must adhere to a certain format as follows:
log2width = 5  realbits =   350  estbits =   330  diff_ratio = 0.05714
log2width = 4  realbits =   126  estbits =    96  diff_ratio = 0.23810
log2width = 3  realbits =    50  estbits =    35  diff_ratio = 0.30000
'''

from tool import *
import sys

# set title names and category values by user
category_title = "log2width"
category_array = [5,  4,  3,  2]
x_title        = "realbits"
y_title        = "estbits"

def showhelp():
    print "Usage:"
    print "    python  %s  input.log"%__file__

if __name__ == "__main__":
    if len(sys.argv) < 2:
        showhelp()
        exit()
    inf_name = sys.argv[1]

    x_array, y_array = extract_info(inf_name, category_array, category_title, x_title, y_title)
    plot_arrays(x_array, y_array, category_array, category_title, x_title, y_title)
