from ast import *
import os

path = "input-code/"
dir_list = os.listdir(path)
 
print("Analyzing files in '", path, "' :")


for file in dir_list:
    print(" ==== " + file + " ==== ")
    fileContent = open(path+file).read()
    tree = parse(fileContent)
    print(tree.body)