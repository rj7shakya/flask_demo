from flask import Flask, render_template, request, url_for

app = Flask(__name__)

moviesArr = ['Avatar', 'Avengers', 'RRR', 'antamn']


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if (request.method == 'POST'):
        return render_template('index.html', marks=int(request.form['marks']))

    else:
        return render_template('index.html', marks=0)


if __name__ == '__main__':
    app.run(debug=True)
