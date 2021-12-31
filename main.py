import os
import tkinter
import tkinter.messagebox
from time import time
import numpy as np
from datetime import  datetime
import tkinter as tk
from tkinter.filedialog import askopenfilename
global root
import pandas as pd
def request_location():

    root.withdraw()
    path = askopenfilename(title='Select Excel File')  # shows dialog box and return the path

    root.update()
    root.withdraw()
    return  path
if __name__ == '__main__':
    root = tk.Tk()
    print("Hello world")


    location = request_location()

    date = datetime.now().strftime("%d-%b-%Y")

    time1 = time()
    containers = pd.read_excel(location,index_col=0,)
    container_index = 0
    ETA_ind = 0
    ETD_ind = 0
    indexes = list(containers.columns)
    for i in range(0,len(indexes)):
        print(indexes[i], i)
        if indexes[i] == 'Container NO':
            container_index = i
        elif indexes[i] == 'Actual ETD':
            ETD_ind = i
        elif indexes[i] == 'Actual ETA':
            ETA_ind = i
    print(container_index,ETD_ind,ETA_ind)
    matrix = containers.to_numpy()
    print(matrix)
    # print(containers[['Container NO','Actual ETD','Actual ETA']])

    tkinter.messagebox.showinfo(title="Program has finished running", message="The result will be in " + location +"\n The program took: %s seconds " % str(time()-time1) )
    root.update()
    root.destroy()

