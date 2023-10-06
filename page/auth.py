from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask import Flask
from flask_socketio import SocketIO
auth=Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        flash('Logged in successfully!', category='success')
        return render_template("home3.html")

    return render_template("login.html")

@auth.route('/logout')
def logout():
    return redirect(url_for('views.home'))

@auth.route('/consultant')
def consultant():
    return render_template("consultant.html")

@auth.route('/ho')
def ho():
    return render_template("home2.html")

@auth.route('/aud')
def aud():
    return render_template("aud.html")

@auth.route('/mood')
def mood():
    return render_template("mood.html")

@auth.route('/story')
def story():
    return render_template("story.html")

@auth.route('/dis')
def dis():
    return render_template("dis.html")

@auth.route('/community')
def index():
    return render_template('community.html')






@auth.route('/sign-up', methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        if len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            flash('Account created!', category='success')
            return redirect(url_for('auth.login'))

    return render_template("sign_up.html")



@auth.route('/video')
def video():
    return render_template("youtube.html")

@auth.route('/vid1')
def vid1():
    return '''<iframe src="https://www.youtube.com/embed/J6mDkcqU_ZE?si=a9w9k6TsmLsxFnqe" width="853" height="480" frameborder="0" allowfullscreen></iframe>'''

@auth.route('/vid2')
def vid2():
    return '''<iframe src="https://www.youtube.com/embed/gB6WLkSrtJk?si=QMHNCN94JMKEzDxu" width="853" height="480" frameborder="0" allowfullscreen></iframe>'''


