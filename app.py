from flask import Flask, render_template, url_for, redirect, request, session
from database import add_offer, add_user, get_all_users, query_by_username, query_by_password, check_login
app = Flask(__name__)

@app.route('/', methods=(['GET' , 'POST']))
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
    	name = request.form['name']
    	password = request.form['password']

    	if check_login(name, password):
    		return redirect('home.html')
    	else:
    		print("incorrect username or password")



@app.route('/')
def home():
    return render_template('home.html')






if __name__ == '__main__':
    app.run(debug=True)
