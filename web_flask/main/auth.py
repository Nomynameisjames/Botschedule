from flask import render_template, flash, redirect, url_for
from . import Main
from .form import RegisterForm, LoginForm 

@Main.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        flash(f'Account created successfully for {form.username.data}', 'success')
        return redirect(url_for('.view'))
    return render_template('register.html', form=form)


@Main.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', form=form)
