from flask import Flask, render_template
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import Required, AnyOf
from flask_navigation import Navigation
import pandas as pd    
from flask_moment import Moment
from get_stats import *   


app = Flask(__name__)
nav = Navigation(app)
app.config['SECRET_KEY'] = 'reallyreallyreallyreallysecretkey'

bootstrap = Bootstrap(app)

#choices for length in form

class name_form(FlaskForm):
    #Validators check if the two tickers are in our list of tickers traded on nasdaq, amex, and nyse
    #Also require for every field to be filled out
    name1   = StringField(u'Name 1: ',    validators=[Required()])
    name2   = StringField(u'Name 2: ',    validators=[Required()])
    submit    = SubmitField(u'Submit')

#Home page
@app.route('/', methods=['GET', 'POST'])
def index():
    name1  = None
    name2  = None
    form   = name_form()
    if form.validate_on_submit():
        name1  = form.name1.data
        name2  = form.name2.data
        stats1 = get_player_stats(name1)
        stats2 = get_player_stats(name2)

        return render_template('index.html', form=form, name1=name1, name2=name2, stats1=stats1, stats2=stats2)
    return render_template('index.html', form=form, name1=name1, name2=name2)

#Run app
if __name__ == '__main__':
    app.run()
