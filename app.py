from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', pageTitle="My Calculator")

@app.route('/zhehuan')
def zhehuan():
    return "hello Zhehuan!"

if __name__ == '__main__':
    app.run(debug=True)
