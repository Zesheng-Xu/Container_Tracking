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
from selenium import webdriver
from urllib.request import urlopen,Request
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def request_location():

    root.withdraw()
    path = askopenfilename(title='Select Excel File')  # shows dialog box and return the path

    root.update()
    root.withdraw()
    return  path

def check_container(container_ID):
    url = "http://www.shippingline.org/track/?type=bill&container="+container_ID+"&line=&track=Track+container"
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read().decode("utf-8")
    print(url)
    print(webpage)

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

        if indexes[i] == 'Container NO':
            container_index = i
        elif indexes[i] == 'Actual ETD':
            ETD_ind = i
        elif indexes[i] == 'Actual ETA':
            ETA_ind = i
    print(container_index,ETD_ind,ETA_ind)
    matrix = containers.to_numpy()

    driver = webdriver.Chrome("chromedriver.exe")
    driver.get("http://www.shippingline.org")
    # first search page
    search_ele = driver.find_element_by_xpath("//*[@id=\"id_seacrh\"]")
    search_confirm_ele = driver.find_element_by_xpath("//*[@id=\"id_search_submit\"]")
    search_ele.send_keys(matrix[container_index][0])
    search_confirm_ele.click()
    # wait for the page to load


    # second search confirm page
    search_ele = driver.find_element_by_xpath("//*[@id=\"idTAUnitNo\"]")
    search_ele.send_keys(matrix[container_index][0])
    search_confirm_ele = driver.find_element_by_xpath("//*[@id=\"idBtnUnitEnqSubmit\"]")
    search_confirm_ele.click()
    # print(containers[['Container NO','Actual ETD','Actual ETA']])

    tkinter.messagebox.showinfo(title="Program has finished running", message="The result will be in " + location +"\n The program took: %s seconds " % str(time()-time1) )
    root.update()
    root.destroy()

