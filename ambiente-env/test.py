from flask import Flask

app = Flask(__name__)

@app.route('/')
def raiz():
    return 'Hello World!'

@app.route('/rota2')
def rota2():
    return '<H1> Segunda rota </H1>'

app.run()