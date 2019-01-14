from flask import Flask, render_template, request, redirect, url_for
from wtforms import Form, StringField, TextAreaField, validators
from wtforms.fields.html5 import DateField
import dropbox_api
app = Flask(__name__)
app.debug = True


class inputForm(Form):
    name = StringField('name of the Ticker')
    fromDate = DateField('data of the ticker', format="%Y-%m-%d")
    toDate = DateField('data of the ticker', format="%Y-%m-%d")


class Code(Form):
    code = TextAreaField("Enter Python Code here ")


@app.route("/", methods=['GET', 'POST'])
def index():
    form = inputForm(request.form)
    if request.method == 'POST' and form.validate():
        ticker = request.form['name']
        toDate = request.form['toDate']
        fromDate = request.form['fromDate']
        print(fromDate, toDate)
        res = dropbox_api.downloadTickerData(ticker,fromDate, toDate)
        return str(res)
        if res:
            return redirect(url_for("fileName", fileName=fileName))

    return render_template("index.html", form=form)


@app.route('/<fileName>', methods=["GET", 'POST'])
def fileName(fileName):
    form = Code(request.form)
    return render_template("interpreter.html", form=form, fileName=fileName)


if __name__ == "__main__":
    app.run()
