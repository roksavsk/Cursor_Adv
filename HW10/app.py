from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def hello_world():
    return 'Hey, we have Flask in a Docker container!'


@app.route('/calc/<int:x>/<int:y>/<string:func>')
def calc(x, y, func):
    if func == 'sum':
        return render_template('calc.html', x=x, y=y, func='+', result=x+y)
    elif func == 'dif':
        return render_template('calc.html', x=x, y=y, func='-', result=x-y)
    elif func == 'mult':
        return render_template('calc.html', x=x, y=y, func='*', result=x*y)
    elif func == 'div':
        if y == 0:
            return render_template('calc.html', y=y)
        else:
            return render_template('calc.html', x=x, y=y, func='/', result=x/y)
    else:
        return render_template('calc.html', func='None')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
