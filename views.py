from flask import Blueprint, render_template, request,jsonify,redirect,url_for
import datetime

views = Blueprint(__name__,"views")

@views.route('/')
def hello():
    return render_template('index.html', utc_dt=datetime.datetime.utcnow())

@views.route('/about/')
def about():
    return render_template('about.html')

@views.route('/comments/')
def comments():
    comments = ['This is the first comment.',
                'This is the second comment.',
                'This is the third comment.',
                'This is the fourth comment.'
                ]

    return render_template('comments.html', comments=comments)

@views.route('/prueba/')
def prueba():
    return render_template('indexp.html')

@views.route('/prueba1/')
def prueba1():
    return render_template('indexp1.html')