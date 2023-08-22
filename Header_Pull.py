import pandas as pd
import re
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from lmfit import minimize, fit_report, Parameters

filename = "D19_8K_12.0T.txt"

NUM_HEADERS = 1

df = pd.read_csv(filename, sep="\t", encoding='latin')


print(f"\n df={df}")

def parseTemp(df:str):
    temp = float(re.findall('[0-9]*\.*[0-9]*(?=K)',filename)[0])
    return temp

temp = parseTemp(filename)


print("11. regex Expressions:")
print(f"temp: {temp}")

#tape_width = float(re.findall('(?u)[]'), df))

import csv 

def extract_headers(filename: str):
    """this method grabs the headers of the file and put them all in one string of text separated by commas
    Args:
        filename: [string] the string path of the file
    Returns:
        header_text: [string] the headers as a string
    """
    with open(filename, "r", encoding="utf8", errors="ignore",) as f:
        fr = csv.reader(f, delimiter="\t")  
        print(f"4. fr:{fr}")
    
        datalist = [str(datarow) for i, datarow in enumerate(fr) if i < NUM_HEADERS] # i is the counter used with enumerate
        print(f"datalist:{datalist}")
        header_text = ",".join(datalist)
        print(f"text:{header_text}")  

        return header_text

headers = extract_headers(filename) 


import os
current_directory = os.getcwd()
header_text = extract_headers(current_directory+"\\"+filename) 
print(f"header_text:{header_text}")

tape_width = re.findall('(?<=width \(m\): )[0-9]+\.*[0-9]*' ,header_text)
print(f"tape width: {tape_width} um")

tape_thickness = re.findall('(?<=thickness \(m\): )[0-9]+\.*[0-9]*' ,header_text)
print(f"tape thickness: {tape_thickness} um")

tape_length = re.findall('(?<=length \(m\): )[0-9]+\.*[0-9]*' ,header_text)
print(f"tape length: {tape_length} m")

initial_current = re.findall('(?<=Initial current \[A\]: )[0-9]+\.*[0-9]*' ,header_text)
print(f"initial_current: {initial_current} A")

starting_current = re.findall('(?<=Starting current \(order/n\): )[0-9]+\.*[0-9]*' ,header_text)
print(f"starting_current: {starting_current} A")

current_limit = re.findall('(?<=Current limit \[A\]: )[0-9]+\.*[0-9]*' ,header_text)
print(f"current_limit: {current_limit} A")

voltage_limit = re.findall('(?<=Voltage limit \[V\]: )[0-9]+\.*[0-9]*' ,header_text)
print(f"voltage_limit: {voltage_limit} uV")

lower_v_for_v_fit = re.findall('(?<=Lower V for fit \[V\]: )[0-9]+\.*[0-9]*' ,header_text)
print(f"lower_v_for_v_fit: {lower_v_for_v_fit} uV")

upper_v_for_v_fit = re.findall('(?<=Upper V for fit \[V\]: )[0-9]+\.*[0-9]*' ,header_text)
print(f"upper_v_for_v_fit: {upper_v_for_v_fit} uV")

expected_n_value = re.findall('(?<=Expected n value: )[0-9]+\.*[0-9]*' ,header_text)
print(f"expected_n_value: {expected_n_value}")

e_field_crit = re.findall('(?<=Elec. field criteria \[V/cm\]: )[0-9]+\.*[0-9]*' ,header_text)
print(f"e_field_crit: {e_field_crit} uV/cm")