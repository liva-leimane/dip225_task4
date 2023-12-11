import csv
import hashlib
import time

import pandas
import selenium
from openpyxl import Workbook, load_workbook
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# import time
# import hashlib
# import pandas as pd
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By

service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)

url = "https://emn178.github.io/online-tools/crc32.html"
driver.get(url)
time.sleep(2)
# def get_crc32_hash(name):
#     return hashlib.crc32(name.encode())
# def find_salary_by_code(info_list, code):
#     for x in range(len(info_list)):
#         r = info_list[x][0]
#         if r == code:
#             return info_list[x][1]
#     return None

# name=[]
# with open("people.csv", "r") as file:
#     next(file)
#     for line in file:
#         row = line.rstrip().split(",")[1]
#         name.append(row)

# salary_info_list = fails.values.tolist()

# for i in range(len(name)):
#     find = driver.find_element(By.ID, "input")
#     find.send_keys(name[i])

#     find = driver.find_element(By.ID, "output")
#     izvada = find.get_attribute("value")

#     crc32_code = get_crc32_hash(izvada)
#     salary = find_salary_by_code(salary_info_list, crc32_code)

#     if salary is not None:
#         print(f"Darbinieks: {name[i]}, Alga: {salary}")

#     time.sleep(2)
#     find.clear()

# input()

name=[]
i=0
# program read information from people.csv file and put all data in name list.
with open("people.csv", "r") as file:
    next(file)
    for line in file:
        row=line.rstrip().split(",")[1]
        name.append(row)
        
find = driver.find_element(By.ID, "input")
i=i+1
find.send_keys(name[i])

find= driver.find_element(By.ID, "output")
izvada= find.get_attribute("value")


fails = pandas.read_excel("salary.xlsx")
info_list = fails.values.tolist()

ch=False
for x in range(len(info_list)):
    r=info_list[x][1]
    if r==izvada:
        kodejums=str(info_list[x][0])
        ch=True
        break
# kodejums=[]
# with open("salary.xlsx","r") as f:
#     next(f)
#     for line in f:
#         if ch==True:
#             if row[1]==kodejums:
#                 kodejums.append(int(row[1]))

if ch:
    kodejums_list = []
    with open("salary.xlsx", "r") as f:
        next(f)
        for line in f:
            if row[1] == kodejums:
                kodejums_list.append(int(row[1]))

# with open("salary.xlsx", "r") as f:
#     next(f)
#     i=i+1
#     for row in range (sheet.nrows):
#         kodejums.append(sheet.cell(row, i))
#         if(izvada==kodejums):
#             kodejums=kodejums.replace(izvada)

input()
