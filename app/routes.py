from app import app
import flask
from flask import Flask, jsonify, request
from requests import post
import json
import os

link = str(os.getenv("DB_URL"))

@app.route('/posting', methods=['POST'])
def posting():

    def send_json1(sendjson1):
        # department send function
        sendjson1 = post("http://" + link + ":5002/set_department", json=sendjson1, headers={"Content-type": "application/json"})
        print(sendjson1.text)
    def send_json2(sendjson2):
        # Team send function
        sendjson2 = post("http://" + link + ":5002/set_team", json=sendjson2, headers={"Content-type": "application/json"})
        print(sendjson2.text)
    def send_json3(sendjson3):
        # Employee send function
        sendjson3 = post("http://" + link + ":5002/set_employee", json=sendjson3, headers={"Content-type": "application/json"})
        print(sendjson3.text)

    def json_count(little_json):
        # Check null in json function
        len_keys = len(little_json)
        len_value = 0
        for item in little_json:
            n = little_json[item]
            if n == None:
                len_value = 0
            else:
                len_value += 1

        if len_value == len_keys:
            return True
        else:
            return False

    datajson = request.data
    data = json.loads(datajson)
    msg = "Successfully sent"

    for i in data:
        if i == "department":
            Department = data["department"]
            if Department is None:
                pass
            else:
                if json_count(Department) is True:
                    send_json1(Department)
                else:
                    msg = "Fill in all the fields"

        elif i == "team":
            Team = data["team"]
            if Team is None:
                pass
            else:
                if json_count(Team) is True:
                    send_json2(Team)
                else:
                    msg = "Fill in all the fields"

        elif i == "employee":
            Employee = data["employee"]
            if Employee is None:
                pass
            else:
                if json_count(Employee) is True:
                    send_json3(Employee)
                else:
                    msg = "Fill in all the fields"
        else:
            pass

    return jsonify(msg)
