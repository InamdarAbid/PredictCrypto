from flask import Flask,render_template
import requests

app = Flask(__name__)


r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
price = r.json()['bpi']['USD']['rate']

@app.route('/')
@app.route('/home/<float:price>')
def index():
    return render_template("home.html", price=price)

if(__name__=="__main__"):
    app.run(debug=True)