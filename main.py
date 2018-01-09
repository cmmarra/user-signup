from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def display_create_account_form():
    return render_template('main.html')

@app.route("/", methods=['POST'])
def create_account_complete():

    username = request.form['username']
    password = request.form['password']
    confirm_password = request.form['confirm_password']
    email = request.form['email']

    username_error = ""
    password_error = ""
    confirm_password_error = ""
    email_error = ""

    #USERNAME VALIDATION
    if not empty(username):
        username_error = "username required"
        password = ''
        confirm_password = ''
        password_error = "password required"
    elif not char_length(username):
        username_error = "username must be between 3 and 20 characters"
        password = ''
        confirm_password = ''
        password_error = "please re-enter password"
        confirm_password_error = "please re-enter password"
    else:
        if " " in username:
            username_error = "username must not contain spaces"
            password = ''
            confirm_password = ''
            password_error = "please re-enter password"
            confirm_password_error = "please re-enter password"

    #PASSWORD VALIDATION
    if not empty(password):
        password_error = "password required"
        password = ''
        confirm_password = ''
    elif not char_length(password):
        password_error = "password must be between 3 and 20 characters"
        password = ''
        confirm_password = ''
        confirm_password_error = "please re-enter password"
    else:
        if " " in password:
            password_error = "password must not contain spaces"
            password = ''
            confirm_password = ''
            confirm_password_error = "please re-enter password"

    #CONFIRM PASSWORD VALIDATION
    if confirm_password != password:
        confirm_password_error = "passwords must match"
        password = ''
        confirm_password = ''
        password_error = 'passwords must match'
            
    #EMAIL VALIDATION
    if empty(email):
        if not char_length(email):
            email_error = "email must be between 3 and 20 characters"
            password = ''
            confirm_password = ''
            password_error = "please re-enter password"
            confirm_password_error = "please re-enter password"
        elif not email_at_symbol(email):
            email_error = "email must contain the @ symbol"
            password = ''
            confirm_password = ''
            password_error = "please re-enter password"
            confirm_password_error = "please re-enter password"
        elif not email_at_symbol_more_than_one(email):
            email_error = "email must contain only one @ symbol"
            password = ''
            confirm_password = ''
            password_error = "please re-enter password"
            confirm_password_error = "please re-enter password"
        elif not email_period(email):
            email_error = "email must contain ."
            password = ''
            confirm_password = ''
            password_error = "please re-enter password"
            confirm_password_error = "please re-enter password"
        elif not email_period_more_than_one(email):
            email_error = "email must contain only one ."
            password = ''
            confirm_password = ''
            password_error = "please re-enter password"
            confirm_password_error = "please re-enter password"
        else:
            if " " in email:
                email_error = "email must not contain spaces"
                password = ''
                confirm_password = ''
                password_error = "please re-enter password"
                confirm_password_error = "please re-enter password"

    if not username_error and not password_error and not confirm_password_error and not email_error:
        username = username
        return redirect('/hello?username={0}'.format(username))
    else:
        return render_template('main.html', username_error=username_error, username=username, password_error=password_error, password=password, confirm_password_error=confirm_password_error, confirm_password=confirm_password, email_error=email_error, email=email)

@app.route("/hello")
def valid_signup():
    username = request.args.get('username')
    return render_template('hello.html', username=username)

#FUNCTIONS FOR VALIDATIONS
def empty(x):
    if x:
        return True
    else:
        return False

def char_length(x):
    if len(x) > 2 and len(x) < 21:
        return True
    else:
        return False

def email_at_symbol(x):
    if x.count('@') >= 1:
        return True
    else:
        return False

def email_at_symbol_more_than_one(x):
    if x.count('@') <= 1:
        return True
    else:
        return False

def email_period(x):
    if x.count('.') >= 1:
        return True
    else:
        return False

def email_period_more_than_one(x):
    if x.count('.') <= 1:
        return True
    else:
        return False

app.run()