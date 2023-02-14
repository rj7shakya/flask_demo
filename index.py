from flask import Flask, render_template

app = Flask(__name__)

moviesArr = ['Avatar', 'Avengers', 'RRR']


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/list')
def list():
    global moviesArr
    return render_template('list.html', movies=moviesArr)


@app.route('/about')
def about():
    return 'THIS IS ABOUT PAGE'


if __name__ == '__main__':
    app.run(debug=True)
