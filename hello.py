from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('indeks.html', title='Home', tekst='Mój tekst', wynik=suma(2, 3) )

@app.route("/test")
def hello2():
    return render_template('test.html')


def suma(a, b):
    return a+b

if __name__ == "__main__":
    app.run()
    
