import os
import tkinter
import tkinter.messagebox
from time import time

from datetime import  datetime
import tkinter as tk
from tkinter.filedialog import askdirectory
import glob
global root
def request_location():

    root.withdraw()
    path = askdirectory(title='Select Folder')  # shows dialog box and return the path
    if "/" in path:
        path += "/"
    elif "\\" in path:
        path += "\\"

    root.update()
    root.withdraw()
    return  path
if __name__ == '__main__':
    root = tk.Tk()
    print("Hello world")
    brands="Acura AlfaRomeo Audi BMW Buick Cadillac Chevrolet Chrysler Dodge FIAT Ford Genesis GMC Honda Hyundai INFINITI Jaguar Jeep Kia LandRover Lexus Lincoln Maserati Mazda Mercedes-Benz Mercury MINI Mitsubishi Nissan Pontiac Porsche Ram Scion smart Subaru Suzuki Tesla Toyota Volkswagen Volvo"
    brands = brands.lower()
    brand_list = brands.split(" ")

    location = request_location()

    date = datetime.now().strftime("%d-%b-%Y")

    time1 = time()


    tkinter.messagebox.showinfo(title="Program has finished running", message="The result will be in " + location +"\n The program took: %s seconds " % str(time()-time1) )
    root.update()
    root.destroy()

