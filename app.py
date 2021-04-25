from flask import Flask, render_template
import data

app = Flask(__name__)


@app.route('/')
def index():
    output = render_template("index.html", data=data)
    return output


@app.route('/departures/<departure>/')
def departures(departure):
    tours = {}
    for key, value in data.tours.items():
        if value["departure"] == departure:
           tours[key] = value
    output = render_template("departure.html", departure=data.departures[departure], data=data, tours=tours)
    return output


@app.route('/tours/<id>/')
def tour(id):
    if int(id) in data.tours.keys():
        tour = data.tours[int(id)]
        output = render_template("tour.html", data=data, departures=data.departures, tour=tour, departure=data.departures[tour["departure"]])
    else:
        output = render_template("index.html", data=data)
    return output


@app.route('/data/')
def all_tours():
    output = "<h1>Все туры: </h1>"
    for key in data.tours.keys():
        output += '<p>{0}: <a href="/data/tours/{1}/">{2} {3} {4} *</a></p>'.format(data.tours[key]["country"], key, data.tours[key]["title"], data.tours[key]["price"], data.tours[key]["stars"])
    return output


@app.route('/data/departures/<departure>/')
def depature_tours(departure):
    output = "<h1>Туры {0}</h1>".format(data.departures[departure])
    for key in data.tours.keys():
        if data.tours[key]["departure"] == departure:
            output += '<p>{0}: <a href="/data/tours/{1}/">{2} {3} {4} *</a></p>'.format(data.tours[key]["country"], key, data.tours[key]["title"], data.tours[key]["price"], data.tours[key]["stars"])
    return output


@app.route('/data/tours/<id>/')
def data_tour(id):
    key = int(id)
    output = "<h1>{0}: {1} {5} *</h1><p>{2} ночей</p><p>Стоимость: {3} Р</p><p>{4}</p>".format(data.tours[key]["country"], data.tours[key]["title"], data.tours[key]["nights"], data.tours[key]["price"], data.tours[key]["description"], data.tours[key]["stars"])
    return output


app.run('127.0.0.1', 8000, debug=True)  # запустим сервер на 8000 порту!
