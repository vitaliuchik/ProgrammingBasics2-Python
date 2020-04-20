from flask import Flask, render_template, request,redirect
import json

app = Flask(__name__)

students = {"students":[]}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=["POST"])
def register():
    if not request.form.get("name") or not request.form.get("domain"):
        return render_template("failure.html")
    data = {"student" : {"name": request.form.get("name"),
                        "domain": request.form.get("domain")}}
    students["students"].append(data)
    with open("registrants.json", "w", encoding="utf-8") as json_file:    
        json.dump(students, json_file, ensure_ascii=False)
        
    return render_template("success.html")


