from flask import Flask,render_template


app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello Eric como estas!'

@app.route('/visualizar_html')
def visualizar_html():
    return render_template("index.html")


@app.route('/visualizar_html1')
def visualizar_html1():
    return render_template("index1.html")