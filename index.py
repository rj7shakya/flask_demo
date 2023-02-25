from flask import Flask, render_template, request

app = Flask(__name__)

moviesArr = ['Avatar', 'Avengers', 'RRR', 'antamn']


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if (request.method == 'POST'):
        return render_template('index.html', marks=int(request.form['marks']))

    else:
        return render_template('index.html', marks=0)


@app.route('/age', methods=['GET', 'POST'])
def age():
    if (request.method == 'POST'):

        return render_template('age.html', age=int(request.form['age']))

    else:
        return render_template('age.html', age=0)


if __name__ == '__main__':
    app.run(debug=True)
