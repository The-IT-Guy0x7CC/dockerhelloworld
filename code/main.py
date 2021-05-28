""" This module is supposed to start the flask environment """
import os
import pickle
import json

from flask import Flask, render_template, request, redirect, url_for, session
from training import Training



app = Flask(__name__, static_url_path='/static/')
app.secret_key = os.urandom(16)
pickle_path = "db.pickle"

@app.route("/")
def home():
    """ DocString """
    return render_template("home.html.j2", trainings=load_training_object())


@app.route("/search")
def search():
    """ DocString """
    return render_template("search.html.j2")


@app.route("/results")
def results():
    """ DocString """
    filtered = list(map(Training.from_json, json.loads(session["filtered"])))
    return render_template("home.html.j2", trainings=filtered, results='true')


@app.route("/api/training/search", methods=['POST'])
def search_training():
    """ DocString """
    name = str(request.form.get('name'))
    instructor = str(request.form.get('instructor'))
    duration = str(request.form.get('duration'))
    content = str(request.form.get('content'))
    filtered = list()
    for training in load_training_object():
        if name in training.name and instructor in training.instructor \
            and duration in training.duration and content in training.content:
            filtered.append(training)
    session['filtered'] = json.dumps(filtered, default=lambda training: training.to_json())
    return redirect(url_for("results"))


@app.route("/add")
def add_training():
    """ DocString """
    return render_template("add.html.j2")


@app.route('/api/training/save', methods=['POST'])
def save_training():
    """ DocString """
    name = str(request.form.get('name'))
    instructor = str(request.form.get('instructor'))
    duration = str(request.form.get('duration'))
    content = str(request.form.get('content'))
    save_training_object(content, duration, name, instructor)
    return redirect(url_for("home"))


def save_training_object(content, duration, name, instructor):
    """ DocString """
    trn = Training(name, instructor, duration, content)
    # load the list of trainings
    if os.path.isfile(pickle_path):
        with open(pickle_path, "rb") as pickle_file:
            list_of_trainings = pickle.load(pickle_file)
    else:
        list_of_trainings = list()
    # add the new training and save
    list_of_trainings.append(trn)
    with open(pickle_path, "wb") as pickle_file:
        pickle.dump(list_of_trainings, pickle_file)


def load_training_object():
    """ DocString """
    # load the list of trainings
    if os.path.isfile(pickle_path):
        with open(pickle_path, "rb") as pickle_file:
            return pickle.load(pickle_file)
    else:
        return list()
        #raise FileNotFoundError("Couldn't load training, because file wasn't found")


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
