from flask import Flask, render_template,request,redirect
import csv
app = Flask(__name__)

#my home
@app.route("/")
def myhome():
    return render_template("index.html")


if __name__=="__main__":
    app.run(debug=True,port=9000)