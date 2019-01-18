import os
import sys

with open(sys.argv[1], 'r') as file:

    data = file.read()
    tmp = sys.argv[2] + ":" + sys.argv[3]
    data = data.replace("100.71.71.71:5000/post-service:2.1", tmp)
    print(data)
         

with open(sys.argv[1], 'w') as file:
    file.write( data )
