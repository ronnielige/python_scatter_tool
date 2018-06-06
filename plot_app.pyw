# coding=gbk
from   Tkinter import *
import tkFont
from   tkFileDialog import *
import ttk
import codecs
from tool import *

button_relief = 'solid'   # button looks
text_relief   = 'solid'
lt_ipady      = 8         # ipady for Label and Text
wid_sticky    = W+E+N+S
msg_key_idx   = 0
msg_value_idx = 1

class APPPlotTool():
    def openSourceFileDialog(self):
        org_file_dir = os.path.dirname(self.t_source.get('0.0', END)[0:-1])
        options = {}
        options['initialdir'] = org_file_dir
        src_path = askopenfilename(**options)
        if src_path != "":
            self.t_source.delete('0.0', END)        # clear contents first
            self.t_source.insert('0.0', src_path)

    def openOutputFileDialog(self):
        org_file_dir = os.path.dirname(self.t_output.get('0.0', END)[0:-1])
        options = {}
        options['initialdir'] = org_file_dir
        file_path = asksaveasfilename(initialfile="plot.pdf", defaultextension=".pdf")
        if file_path != "":
            self.t_output.delete('0.0', END)        # clear contents first
            self.t_output.insert('0.0', file_path)

    def checkHistory(self):  # fill texts with history values if exists
        if CheckFile(".history"):
            f_history   = open(".history", "r")
            source_file = f_history.readline()[8:-1]
            output_file = f_history.readline()[8:-1]
            categ_title = f_history.readline()[8:-1]
            categ_value = f_history.readline()[8:-1]
            x_title     = f_history.readline()[8:-1]
            y_title     = f_history.readline()[8:-1]
            self.t_source.insert('0.0', source_file)
            self.t_output.insert('0.0', output_file)
            self.t_cat_title.insert('0.0', categ_title)
            self.t_cat_array.insert('0.0', categ_value)
            self.t_x_title.insert('0.0', x_title)
            self.t_y_title.insert('0.0', y_title)
        else:
            self.t_source.insert('0.0', r"D:/input.log")
            self.t_output.insert('0.0', r"D:/output.img")
            self.t_cat_title.insert('0.0', "log2width")
            self.t_cat_array.insert('0.0', "5 4 3 2")
            self.t_x_title.insert('0.0', "realbits")
            self.t_y_title.insert('0.0', "estbits")

    def saveHistory(self):
        f_history = codecs.open(".history", 'w', 'utf-8')   # write 中文内容
        f_history.write(u"Source: %s\n"%self.t_source.get('0.0', END)[0:-1])
        f_history.write(u"Output: %s\n"%self.t_output.get('0.0', END)[0:-1])
        f_history.write(u"cattit: %s\n"%self.t_cat_title.get('0.0', END)[0:-1])
        f_history.write(u"catval: %s\n"%self.t_cat_array.get('0.0', END)[0:-1])
        f_history.write(u"xtitle: %s\n"%self.t_x_title.get('0.0', END)[0:-1])
        f_history.write(u"ytitle: %s\n"%self.t_y_title.get('0.0', END)[0:-1])
        f_history.close()

    def __init__(self, master):
        self.font = tkFont.Font(family="Courier", size=9)

        ##### Define Main Frames
        self.OpenFileFrame = LabelFrame(master, text=u"选择文件", padx = 5, pady = 5)
        self.OpenFileFrame.grid(row = 0, column = 0, columnspan = 2, sticky = W+E+N+S, padx = 5, pady = 5)
        self.OptionsFrame = LabelFrame(master, text="Options", padx = 5, pady = 5)
        self.OptionsFrame.grid(row = 1, column = 0, sticky = W+E+N+S, padx = 5, pady = 5)
        self.OperationsFrame = LabelFrame(master, padx = 0, pady = 5)
        self.OperationsFrame.grid(row = 2, column = 0, sticky = W+E+N+S, padx = 5, pady = 5)

        ##### Define widgets within OpenFileFrame
        self.l_source  = Label (self.OpenFileFrame, text=u'source file', fg='red')
        self.l_output  = Label (self.OpenFileFrame, text=u'output file', fg='blue')
        self.t_source  = Text  (self.OpenFileFrame, height = 1, width = 45, relief = text_relief, fg='red', font=self.font)
        self.t_output  = Text  (self.OpenFileFrame, height = 1, width = 45, relief = text_relief, fg='blue', font=self.font)
        self.b_source  = Button(self.OpenFileFrame, text=u'Open   ', relief=button_relief, command=lambda: self.openSourceFileDialog())
        self.b_output  = Button(self.OpenFileFrame, text=u'Save As', relief=button_relief, command=lambda: self.openOutputFileDialog())

        ##### Define widgets within OptionsFrame
        self.l_cat_title = Label(self.OptionsFrame, text=u'category title', fg='blue')
        self.t_cat_title = Text (self.OptionsFrame, height = 1, width = 15, relief = text_relief, fg='blue', font=self.font)
        self.l_cat_array = Label(self.OptionsFrame, text=u'category values', fg='blue')
        self.t_cat_array = Text (self.OptionsFrame, height = 1, width = 15, relief = text_relief, fg='blue', font=self.font)
        self.l_x_title   = Label(self.OptionsFrame, text=u'x title       ', fg='blue')
        self.t_x_title   = Text (self.OptionsFrame, height = 1, width = 15, relief = text_relief, fg='blue', font=self.font)
        self.l_y_title   = Label(self.OptionsFrame, text=u'y title       ', fg='blue')
        self.t_y_title   = Text (self.OptionsFrame, height = 1, width = 15, relief = text_relief, fg='blue', font=self.font)

        ##### Place widgets within OpenFileFrame
        self.l_source.grid (row = 0, column = 0, padx = 5, pady = 5, sticky = wid_sticky, ipady = lt_ipady)
        self.t_source.grid (row = 0, column = 1, padx = 5, pady = 5, sticky = wid_sticky, ipady = lt_ipady)
        self.b_source.grid (row = 0, column = 2, padx = 5, pady = 5, ipady = 1)
        self.l_output.grid (row = 1, column = 0, padx = 5, pady = 5, sticky = wid_sticky, ipady = lt_ipady)
        self.t_output.grid (row = 1, column = 1, padx = 5, pady = 5, sticky = wid_sticky, ipady = lt_ipady)
        self.b_output.grid (row = 1, column = 2, padx = 5, pady = 5, ipady = 1)

        ##### Place widgets within OptionFrame
        self.l_cat_title.grid(row = 0, column = 1, padx = 2, pady = 3)
        self.t_cat_title.grid(row = 0, column = 2, padx = 15, pady = 3)
        self.l_cat_array.grid(row = 0, column = 3, padx = 2, pady = 3)
        self.t_cat_array.grid(row = 0, column = 4, padx = 5, pady = 3)
        self.l_x_title.grid(row = 1, column = 1, padx = 2, pady = 3)
        self.t_x_title.grid(row = 1, column = 2, padx = 15, pady = 3)
        self.l_y_title.grid(row = 1, column = 3, padx = 2, pady = 3)
        self.t_y_title.grid(row = 1, column = 4, padx = 5, pady = 3)

        ##### Place widgets within OperationsFrame
        self.progressbar = ttk.Progressbar(self.OperationsFrame, orient=HORIZONTAL, length = 380, mode='determinate')
        self.progressbar.grid(row = 0, column = 1, columnspan = 2, ipady = lt_ipady, sticky = W+E+N+S, padx = 4, pady = 5)
        self.progress = 0
        self.b_Collect = Button(self.OperationsFrame, relief=button_relief, bg='green', text = u'Start Plot', width = 10, command=self.StartPlotThread)
        self.b_Collect.grid (row = 0, column = 0, ipady = 1, padx = 2, pady = 3)
        self.checkHistory()

    def StartPlotThread(self):
        source_file = self.t_source.get('0.0', END)[0:-1]
        output_file = self.t_output.get('0.0', END)[0:-1]
        self.saveHistory()
        category_title = self.t_cat_title.get('0.0', END)[0:-1]
        category_text  = self.t_cat_array.get('0.0', END)[0:-1]
        category_array = []
        for item in category_text.split():
            if len(category_array) >= 4:
                print "category values should be no more than 4"
                continue
            category_array.append((int)(item))

        x_title = self.t_x_title.get('0.0', END)[0:-1]
        y_title = self.t_y_title.get('0.0', END)[0:-1]

        x_array, y_array = extract_info(source_file, category_title, category_array, x_title, y_title)
        plot_arrays(x_array, y_array, category_title, category_array, x_title, y_title, output_file)
        self.progressbar['value'] = 100.0


if __name__ == "__main__":
    root = Tk()
    root.title(u'python plot tool')
    root.resizable(0, 0) # can't resize
    root.rowconfigure   (0, weight=1)
    root.columnconfigure(0, weight=1)
    APPPlotTool(root)
    root.mainloop()