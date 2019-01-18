import os
import sys

with open(sys.argv[1], 'r') as file:
    str_tmp = "ghostgoose"
    data = file.read()
    tmp = sys.argv[2] + ":" + sys.argv[3]
    data = data.replace("ghostgoose33/get-python:v1", tmp)
    print(data)
         

with open(sys.argv[1], 'w') as file:
    file.write( data )
