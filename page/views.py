from flask import Blueprint, render_template, flash
views=Blueprint('views', __name__)

@views.route('/')
def home():
    flash('welcome', category='start')
    return render_template("home.html")
