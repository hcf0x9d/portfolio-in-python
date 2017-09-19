#!/usr/bin/python3
from flask import Flask, render_template, request, jsonify
from flask import redirect, url_for, flash, make_response
from flask import session as login_session
from flask_navigation import Navigation

app = Flask(__name__)
# TODO: [DEPLOY TASKS] Make the secret key different for deployment
app.config['SECRET_KEY'] = '00923681-4fa6-49e3-b727-9113ac78450e'

nav = Navigation(app)

nav.Bar('top', [
    nav.Item('Home', 'home_controller'),
    nav.Item('Resume', 'resume_controller'),
    nav.Item('Work', 'work_controller'),
])


# TODO: [VIEWS] Home
@app.route('/')
def home_controller():
    return render_template('home.html')


# TODO: [VIEWS] Resume
@app.route('/resume')
def resume_controller():
    return render_template('resume.html')


# TODO: [VIEWS] Work Examples
@app.route('/work')
def work_controller():
    return render_template('work.html')


# TODO: [VIEWS] Management Portal
@app.route('/manage')
def login():
    return 'LOGIN TO THE MANAGER!'


if __name__ == '__main__':
    # TODO: [DEPLOY TASKS] Make debug=False before deployment
    app.run(host='0.0.0.0', port=5000, debug=True)
