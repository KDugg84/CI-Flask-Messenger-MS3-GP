from flask import render_template, url_for, flash, redirect
from flaskmessenger.forms import RegistrationForm, LoginForm
from flaskmessenger import app, db

# dummy date to iterate through using jinja for loop.
posts = [
    {
        'author': 'John Doe',
        'title': 'Message 1',
        'content': 'First post content',
        'date_posted': 'November 27th, 2023'
    },
    {
        'author': 'Jane Doe',
        'title': 'Message 2',
        'content': 'Second post content',
        'date_posted': 'November 27th, 2023'
    }
]


@app.route("/")
def base():
    return render_template('base.html')


@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    # conditional to validate a successful registration
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template("login.html", title='Login', form=form)