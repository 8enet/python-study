from flask import Flask
from flask import request
from flask import Response
from flask import render_template
from flask import make_response
from pymongo import MongoClient

app = Flask(__name__)


def init_db():
    # https://mongolab.com/     free mongodb service
    client = MongoClient('ds039073.mongolab.com', 39073)
    client.py_db.authenticate('py_db1', 'admin1', mechanism='SCRAM-SHA-1')
    global db
    db = client.py_db.bintest


@app.route('/')
def hello_world():
    resp = make_response("hello ")
    resp.headers['X-Parachutes'] = 'parachutes are cool'
    return resp


@app.route('/user/<username>')
def aaa(username):
    return 'request username %s ' % username


@app.route('/name')
@app.route('/name/<name>')
def aaa2(name=None):
    return render_template('hello.html', name=name)


@app.route('/list')
def list():
    return render_template('list.html', doc=db.find({}))


@app.route('/add')
@app.route('/add', methods=['post'])
def add(u_name='u_name', u_value='u_value'):
    if request.method == 'GET':
        return render_template('add.html', u_name=u_name, u_value=u_value)
    else:
        name = request.form[u_name]
        value = request.form[u_value]
        id = db.insert_one({u_name: name, u_value: value}).inserted_id
        return 'add ok name:%s  value:%s ,db id:%s' % (name, value, id)


if __name__ == '__main__':
    init_db()
    app.run(debug=True)
