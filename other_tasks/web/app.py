from flask import Flask, render_template
from connector import fetchData

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fetch-data')
def data():
    return fetchData()

if __name__ == '__main__':
    app.run(debug=True)
