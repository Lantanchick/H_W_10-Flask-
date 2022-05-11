from flask import Flask
import requests

candidat_list = requests.get("https://jsonkeeper.com/b/S7FV")
candidat_list = candidat_list.json()

app = Flask(__name__)


@app.route("/")
def page_index():
    lt = ''
    for i in candidat_list:
        lt += f"--({i['name']},{i['position']},{i['skills']})--"
    return lt


@app.route("/candidates/<int:num_can>")
def candidat_name(num_can):
    return candidat_list[num_can - 1]["name"]


@app.route("/skills/<skill>")
def page_skills(skill):
    lt = ''
    for i in candidat_list:
        if skill in i["skills"]:
            lt += f"--({i['name']},{i['position']},{i['skills']})--"
    return lt


app.run()
