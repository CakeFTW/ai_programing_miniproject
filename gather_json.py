import os
import sys
import pandas
import json

try:
    open("keypoints.data")
    print("important----output file allready exists, adding data at the end of that one")
except FileNotFoundError:
    print("-creating output file")

output_file = open("keypoints.data",'a')
totals = []
paths = []
has_arg = 0

if(len(sys.argv)> 1):
    paths = os.listdir(sys.argv[1])
    has_arg = 1
else:
    paths = ["participant351_000000000000_keypoints.json","participant351_000000000001_keypoints.json"]

folder = "test_data"
if has_arg:
    folder = sys.argv[1]

print("found a total of : ", len(paths)," files")
for path in paths:
    f = open(folder+ "//" + path, 'r')
    datastore = json.load(f)["people"][0]["pose_keypoints_2d"]
    totals.append(datastore)

json.dump(totals,output_file)
output_file.close()

# list_of_files = os.listdir("test_data")

# data = pandas.read_json("test_data//participant351_000000000000_keypoints.json").get("people")
# data1 = pandas.read_json("test_data//participant351_000000000001_keypoints.json").get("people")
# data = data.append(data1)
# print(type(data))
# # print(data['people'][0]['pose_keypoints_2d'])

# print(data[0]["pose_keypoints_2d"])
# # for paths in list_of_files:
# #     data = data.append(pandas.read_csv("test_data//" + paths))


