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
import json

class inputForm(Form):
    name = StringField('name of the Ticker')
    fromDate = DateField('From Date', format="%Y-%m-%d")
    toDate = DateField('To date', format="%Y-%m-%d")



class Code(Form):
    code = TextAreaField("Enter Python Code here ")
    invest = StringField("Invest Amount")
    fee = StringField("Fees Amount")


@app.route("/", methods=['GET', 'POST'])
def index():
    # form = inputForm(request.form)
    # if request.method == 'POST' and form.validate():
    #     ticker = request.form['name']
    #     toDate = request.form['toDate']
    #     fromDate = request.form['fromDate']
    #    # print(fromDate, toDate)
    #     res = dropbox_api.downloadTickerData(ticker,fromDate, toDate)
    #     if res is True:
    #         return redirect(url_for("editor",range = ""+str(ticker)+'_'+str(datetime.strptime(fromDate, "%Y-%m-%d").date()))+'_'+str(datetime.strptime(toDate, "%Y-%m-%d").date()))
    return redirect(url_for('editor',range="index"))




@app.route('/<range>', methods=["GET", 'POST'])
def editor(range):
    b=[]
    dis = ""
    if range == "index":
        dis = "disabled"
    # if request.method =="POST":
    #     res = dropbox_api.execCode(request.form['code'],range)
    #     return res
    # if range == "index":
    #     dis = "disabled"
    if request.method=='POST':
        if request.form['ref'] =='ticker':
            ticker = request.form['name']
            toDate = request.form['toDate']
            fromDate = request.form['fromDate']
            # print(fromDate, toDate)
            res = dropbox_api.downloadTickerData(ticker,fromDate, toDate)
            if res is True:
                return redirect(url_for("editor",range = ""+str(ticker)+'_'+str(datetime.strptime(fromDate, "%Y-%m-%d").date()))+'_'+str(datetime.strptime(toDate, "%Y-%m-%d").date()))
        if request.form['ref']=="code":
            print("hmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm")
            error,output = dropbox_api.execCode(request.form['code'],request.form['invest'],request.form['fee'],range)
            res = {
                "output":output,
                "error":error,
                "range":range
            }
            return json.dumps(res).encode("utf-8")
    if range !="index":
        b=range.split("_")
        print("here")
        formCode = Code(request.form)
        formInput = inputForm(request.form)
        formInput.fromDate.data = datetime.strptime(b[1],"%Y-%m-%d")
        formInput.toDate.data = datetime.strptime(b[2],"%Y-%m-%d")
        formInput.name.data = b[0]
        return render_template("interpreter.html", formCode=formCode,range = range,formInput=formInput,dis=dis)
    formCode = Code(request.form)
    formInput = inputForm(request.form)
    return render_template("interpreter.html", formCode=formCode,range = range,formInput=formInput,dis=dis)


if __name__ == "__main__":
    app.run()
