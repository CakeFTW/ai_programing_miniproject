import os
import sys
import pandas
import json

try:
    open("keypoints.data")
except FileNotFoundError:
    print("keypoints.data not found")

output_file = open("keypoints.data",'r')

data = json.load(output_file)
print(len(data))