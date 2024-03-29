from flask import render_template, url_for, flash, redirect, request, abort
from flaskmessenger.forms import RegistrationForm, LoginForm, NewPost
from flaskmessenger import app, db, bcrypt
from flaskmessenger.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required


@app.route("/")
def base():
    return render_template('base.html')


@app.route("/home")
def home():
    posts = Post.query.all()
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    # conditional to stop user going back to register/login page via the navbar from home page
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    # conditional to validate a successful registration
    if form.validate_on_submit():
        # variable to hash a password generated by the bcrypt class
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        # creates a new user of the User model to be stored on the database
        user = User(username=form.username.data, email=form.email.data, password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        # 'alert-message' css class to help validate a successful registration 
        flash(f'Your account has now been created! You are now logged in', 'alert-message')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    # conditional to stop user going back to register/login page via the navbar from home page
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    # conditional to validate successful login
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            # ternary conditional 
            next_pg = request.args.get('next')
            return redirect(next_pg) if next_pg else redirect(url_for('home'))
        else:
            # 'warning' css class to highlight an unsuccessful login attempt 
            flash('Login Unsuccessful! Please check email and password', 'warning')  
    return render_template("login.html", title='Login', form=form)


@app.route("/logout")
def logout():
    # logout route based on the logout_user class imported from login_user extension
    logout_user()
    return redirect(url_for('home'))


@app.route("/account")
# login required decorator added to route from the imported login_user extension
@login_required
def account():
    # variable to add the default 'profile.png' image file when a user creates an account   
    profile_image = url_for('static', filename='img/' + current_user.profile_image)
    return render_template('account.html', title='Account', profile_image=profile_image)


@app.route("/new/post", methods=['GET', 'POST'])
@login_required
def new_post():
    # instance of NewPost class from forms.py
    form = NewPost()
    if form.validate_on_submit():
        # variable to populate the date to the NewPost class based on existing db
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been sent!', 'alert-message')
        return redirect(url_for('home'))
    return render_template('new_post.html', title='New Posts',legend='New Post!', form=form)


@app.route("/posts/<int:post_id>")
def posts(post_id):
    # variable to query a user's existing post 
    post = Post.query.get(post_id)
    return render_template('posts.html', title=post.title, post=post)


@app.route("/posts/<int:post_id>/edit", methods=['GET', 'POST'])
@login_required
def edit_posts(post_id):
    post = Post.query.get(post_id)
    if post.author != current_user:
        abort(403)
    form = NewPost()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated!', 'alert-message')
        return redirect(url_for('posts', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('new_post.html', title='Update Posts', legend='Update Post!', form=form)


@app.route("/posts/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_posts(post_id):
    post = Post.query.get(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'alert-message')
    return redirect(url_for('home'))               