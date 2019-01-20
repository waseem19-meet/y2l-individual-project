from flask import Flask, render_template, url_for, redirect, request, session
from database import add_offer, get_all_offers, add_user, get_all_users, query_by_username, query_by_password
app = Flask(__name__)
app.secret_key ="yalla"


@app.route('/')
def home():
	if session.get('display_login') == True:
		session['display_login'] = False
		return render_template('home.html', logged_in=True)
	else:
		return render_template('home.html', logged_in=False)




@app.route('/add_offer', methods=['GET', 'POST'])
def add_offers_route():
  if 'logged_in' in session:
    if session['logged_in']==True:  
      if request.method == 'GET':
        return render_template('post.html')
      if request.method=="POST":
        print ('Received POST request for adding an article!')
        subject = request.form['subject']
        content = request.form['offer_content']
        user_id=session['user_id']
        # image=request.form['image']
        add_offer(subject, content,user_id)
        return render_template('read.html')
    else:
      return redirect(url_for('login_route'))            
  else:
    return redirect(url_for('login_route'))






@app.route('/login', methods=(['GET' , 'POST']))
def login_route():
	if 'logged_in' in session and session['logged_in']==True:
		return redirect (url_for('home'))
	if request.method == 'POST':
		print('hey')
		user=query_by_username(request.form['name'])

		if user==None:
			return redirect (url_for('signup_route'))
		else:
			if request.form['password']==user.password:
				session['logged_in'] = True
				session['user_id']=user.id
				session['display_login'] = True
				return redirect(url_for('home'))
			return render_template('login.html')

	else:
		return render_template('login.html') 



	# if request.method == 'GET':
	#     return render_template('login.html')
	# else:
	# 	name = request.form['name']
	# 	password = request.form['password']

	# 	if check_login(name, password):
	# 		return redirect('home.html')
	# 	else:
	# 		print("incorrect username or password")



@app.route('/offers')
def offers_page():
  offers=get_all_offers()
  offers.reverse()

  return render_template('read.html', offers = offers)



@app.route('/signup', methods=['GET', 'POST'])
def signup_route():
	if request.method == 'GET':
		return render_template('signUp.html')
	else:
		print ('Received POST request for sign up!')
		status = request.form['status']
		name = request.form['name']
		email = request.form['email']
		password= request.form['password']
		phone = request.form['phone']

		g=query_by_username(name)

		if g!=None:
			print ('we already have a user with that name')
		else:   
			add_user(status, name, email, password,phone)
			session['display_login'] = True
	return redirect(url_for('home'))


@app.route('/logout')
def logout_route():
	if 'user_id' in session:
		del session['user_id']
		session['logged_in']=False
	return redirect(url_for('home'))
	print('logged out')

# @app.route('/nav')
# def navi():
# 	return render_template('read.html')
	


  


if __name__ == '__main__':
	app.run(debug=True)
