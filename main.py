from flask import Flask
from utils import *

app = Flask(__name__)
candidates_list = get_candidates()


@app.route("/")
def main_page():
    text = ""
    for candidate in candidates_list:
        text += "<p>Имя кандидата - " + candidate["name"] + "</p>"
        text += "<p>Позиция кандидата: " + candidate["position"] + "</p>"
        text += "<p>Навыки: " + candidate["skills"] + "</p>"
    return f"<center>{text}</center>"


@app.route("/candidates/<name>")
def get_candidates(name):
    for candidate in candidates_list:
        if name.title().strip() == candidate["name"]:
            # picture = get_images(candidate['picture'])
            return f'<img scr="{candidate["picture"]}"/>' \
                   f"<center><p>Имя кандидата - {candidate['name']}</p>" \
                   f"<p>Позиция кандидата: {candidate['position']}</p>" \
                   f"<p>Навыки: {candidate['skills']}</p>"
    return f"<center><p>Такого кандидата нет</p>"


@app.route("/skills/<skill>")
def get_skills(skill):
    text = ""
    for candidate in candidates_list:
        if skill.lower().strip() in candidate["skills"].lower().split(", "):
            text += f"<center><p>Имя кандидата - {candidate['name']}</p>" \
                    f"<p>Позиция кандидата: {candidate['position']}</p>" \
                    f"<p>Навыки: {candidate['skills']}</p>"
    if len(text) != 0:
        return text
    else:
        return f"<center><p>Кандидата с таким умением нет</p>"


if __name__ == "__main__":
    app.run()

