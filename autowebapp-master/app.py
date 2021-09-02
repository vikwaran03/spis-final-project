import os
import pandas as pd

from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

df = pd.read_csv("autotest.csv")
df.set_index('Make', inplace=True)


app = Flask(__name__)
app.secret_key='w98fw9ef8hwe98fhwef'; 

@app.route('/')
def renderMain():
    return render_template('home.html') 

@app.route('/welcome')
def renderWelcome():
    return render_template('welcome.html')

@app.route('/question1')
def renderQuestion1():
    return render_template('question1.html')

@app.route('/question2')
def renderQuestion2():
    return render_template('question2.html')

@app.route('/question3_over_25')
def renderQuestion3_over_25():
    return render_template('question3_over_25.html')

@app.route('/question3_under_25')
def renderQuestion3_under_25():
    return render_template('question3_under_25.html')

@app.route('/question4_over_25')
def renderQuestion4_over_25():
    return render_template('question4_over_25.html')

@app.route('/path1')
def renderpath1():
    return render_template('path1.html')

@app.route('/welcome',methods=['GET','POST'])
def renderWelcomeResult():
    session["name"]=request.form['name']
    return render_template('welcome.html')

@app.route('/question1',methods=['GET','POST'])
def renderQuestion1Result():
    session["age1"]=request.form['age1']
    if session["age1"] == 'True':
        return render_template('question2.html')
    if session["age1"] == 'False':
        return render_template('question3_under_25.html')

@app.route('/question2',methods=['GET','POST'])
def renderQuestion2Result():
    session["age2"]=request.form['age2']
    return render_template('question3_over_25.html') 

@app.route('/question3_over_25',methods=['GET','POST'])
def renderQuestion3_over_25Result():
    session["experience"]=request.form['experience']
    return render_template('question4_over_25.html')

@app.route('/question4_over_25',methods=['GET','POST'])
def renderQuestion4_over_25Result():
    session["drivetype"]=request.form['drivetype']
    if session["drivetype"] == 'True' and session["age1"] == 'True' and session["age2"] == 'True' and session["experience"] == 'True': 
        path1 = df[(df.Symboling >= 0) & (df.BodyStyle == "suv" ) & (df.HighwayMPG >= 30)]
        path1 = path1.to_html()
        return render_template('path1.html', df2=path1)

    if session["drivetype"] == 'False':
        return render_template('question5_over_25.html')


if __name__=="__app__":
    
    app.run(debug=True, host='0.0.0.0')
