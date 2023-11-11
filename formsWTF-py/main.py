from flask import Flask, render_template
from wtforms import StringField, PasswordField, SubmitField
import flask_wtf
from wtforms.validators import DataRequired
app = Flask(__name__)


class LoginForm(flask_wtf.FlaskForm):
    email = StringField(label='Email', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label="Log In")


app.secret_key = "my-secret"


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login")
def login():
    login_form = LoginForm()
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
