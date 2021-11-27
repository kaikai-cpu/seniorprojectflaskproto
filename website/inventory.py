from flask import Blueprint, render_template,redirect,url_for

inventory = Blueprint('inventory', __name__)

##route for login
@inventory.route('/add')
def add():
    return render_template('add.html')

#Post Login
#@auth.route('/add', methods=['POST'])
#def add_post():




