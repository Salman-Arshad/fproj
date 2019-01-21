from flask import Flask, render_template, request, redirect, url_for
from wtforms import Form, StringField, TextAreaField, validators
from wtforms.fields.html5 import DateField
import logging
import dropbox_api
from datetime import datetime
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
from django.http import HttpResponse
app = Flask(__name__)
app.debug = True


class inputForm(Form):
    name = StringField('name of the Ticker')
    fromDate = DateField('From Date', format="%Y-%m-%d")
    toDate = DateField('To date', format="%Y-%m-%d")


class Code(Form):
    code = TextAreaField("Enter Python Code here ")


@app.route("/", methods=['GET', 'POST'])
def index():
    form = inputForm(request.form)
    if request.method == 'POST' and form.validate():
        ticker = request.form['name']
        toDate = request.form['toDate']
        fromDate = request.form['fromDate']
       # print(fromDate, toDate)
        res = dropbox_api.downloadTickerData(ticker,fromDate, toDate)
        if res is True:
            return redirect(url_for("editor",range = ""+str(ticker)+'_'+str(datetime.strptime(fromDate, "%Y-%m-%d").date()))+'_'+str(datetime.strptime(toDate, "%Y-%m-%d").date()))


    return render_template("index.html", form=form)


@app.route('/<range>', methods=["GET", 'POST'])
def editor(range):
    if request.method =="POST":
        res = dropbox_api.execCode(request.form['code'],range)
        return res
    form = Code(request.form)
    return render_template("interpreter.html", form=form,range = range)


if __name__ == "__main__":
    app.run()
