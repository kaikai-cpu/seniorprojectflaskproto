from flask import Blueprint, render_template,redirect,url_for

main = Blueprint('main', __name__)

##route for index
@main.route('/')
def index():
    return render_template('index.html')

##student profile
@main.route('/studentprofile')
def studentprofile():
    return render_template('studentprofile.html')

##Staff profile
@main.route('/staffprofile')
def staffprofile():
    return render_template('staffprofile.html')

@main.route('/logout')
def logout():
    return redirect(url_for('main.index'))