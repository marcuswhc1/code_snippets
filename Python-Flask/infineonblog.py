from flask import Flask, redirect, url_for, render_template, flash
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

# Secret key to keep our site secure
app.config['SECRET_KEY'] = '1q2w3e4r'

@app.route('/')
@app.route('/piechart')
def piechart():
    return render_template("piechart.html")

@app.route('/graph')
def graph():
    return render_template("graph.html")


@app.route('/register', methods =['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
    	# This message will flash when the user registers successfully.
    	flash(f'Account created for {form.username.data}!', 'success') 
    	# After validating correctly, we will get redirected to the piechart page
    	return redirect(url_for('piechart'))
    return render_template("register.html", title = 'Register', form=form)

@app.route('/login', methods = ['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
    	# This message will flash when the user registers successfully.
    	flash(f'Welcome back {form.email.data}!', 'success') 
    	# After validating correctly, we will get redirected to the piechart page
    	return redirect(url_for('piechart'))
    return render_template("login.html", title = 'Login', form=form)


if __name__ == '__main__':
	app.run(debug=True)
