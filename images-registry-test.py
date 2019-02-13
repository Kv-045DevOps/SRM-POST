import sys
import os
import requests
import json

def main():
    check_image()


def check_image():
   tmp = requests.get("http://" + sys.argv[1] + "/v2/" + sys.argv[3] + "/tags/list")
   req = tmp.json()
   print(req)
   if req["name"] == sys.argv[2] and sys.argv[3] in req["tags"]:
       return 0
   else:
       raise Exception("Image with tag " + sys.argv[3] + " does not exist in Docker Registry with IP: " + sys.argv[1])
       return 1


if __name__=='__main__':
    main()
