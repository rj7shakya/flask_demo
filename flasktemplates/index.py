from flask import Flask, render_template

from utils import check

app = Flask(__name__)

moviesArr = ['Avatar', 'Avengers', 'RRR', 'antamn']


@app.route('/')
def hello_world():
    return render_template('index.html', marks=60)


# if __name__ == '__main__':
#     app.run(debug=True)
