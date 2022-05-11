from flask import Flask
import requests

candidat_list = requests.get("https://jsonkeeper.com/b/S7FV")
candidat_list = candidat_list.json()

app = Flask(__name__)


@app.route("/")
def page_index():
    lt = ''
    for i in candidat_list:
        lt += f"<br><b>Имя кандидата - {i['name']}</b></br><br>Позиция кандидата - {i['position']}</br><br>Навыки - {i['skills']}</br><br></br>"
    return lt


@app.route("/candidates/<int:num_can>")
def candidat(num_can):
    lt = ''
    for i in candidat_list:
        if num_can == int(i['id']):
            lt = f"<br><img src = {i['picture']}></br><br><b>Имя кандидата - {i['name']}</b></br><br>Позиция кандидата - {i['position']}</br><br>Навыки - {i['skills']}</br><br></br>"
    return lt


@app.route("/skills/<skill>")
def page_skills(skill):
    lt = ''
    for i in candidat_list:
        if skill in i['skills'].lower().split(', '):
            lt += f"<br><b>Имя кандидата - {i['name']}</b></br><br>Позиция кандидата - {i['position']}</br><br>Навыки - {i['skills']}</br><br></br>"
    return lt


app.run()
