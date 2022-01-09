from tkinter import *

import matplotlib.pyplot as plt
import numpy as np
root = Tk()
root.title("Sample2")
root.geometry("1080x900")


def naive(p, t):
    ocurrences = []
    for i in range(len(t)-len(p)+1):
        match = True
        for j in range(len(p)):
            if not t[i+j] == p[j]:
                match = False
                break
        if match:
            ocurrences.append(i)
    return ocurrences

def readgenome(filename):
    genome = ""
    with open(filename, "r") as f:
        for line in f:
            if not line[0] == ">":
                genome += line.rstrip()
    return genome


def findGCcontentbypos(reads):
    gc = [0] * 100
    totals = [0] *100
    for read in reads:
        for i in range(len(read)):
            if read[i]=="G" or read[i]=="C":
                gc[i]+= 1
            totals[i]+= 1
    for i in range(len(gc)):
        if totals[i]>0:
            gc[i] /= float(totals[i])
    return gc


def clicked1():
    my_label2 = Label(my_frame, text=naive(p.get(), readgenome(t.get())))
    my_label2.pack(padx = 10, pady = 30)
def clicked2():
    my_label2 = Label(root, text=findGCcontentbypos(readgenome(t.get())))
    my_label2.pack()

def clicked3():
    gc = findGCcontentbypos(readgenome(t.get()))
    my_label2 = Label(root, text="GC distribution graph")
    plt.plot(range(len(gc)), gc)
    plt.show()
    my_label2.pack()


my_label = Label(root, text = "Enter the PATTERN and the fasta file name in the dir", font = ("Ariel", "10"))
my_label.pack()

p = Entry(root)
p.pack()
t = Entry(root, width = "50" )
t.pack()
scrollbar = Scrollbar(root, orient = HORIZONTAL)
scrollbar.pack()


my_button1 = Button(root, text = "Get seq hits", command = clicked1)
my_button1.pack()
my_button2 = Button(root, text = "Get GC content", command = clicked2)
my_button2.pack()
my_button3 = Button(root, text = "Plot GC dist graph", command = clicked3)
my_button3.pack()

my_frame = Frame(root, width = 200, height = 200, bd= 1, bg ="Blue")
my_frame.pack()


root.mainloop()