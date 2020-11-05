from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbtodo

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/list', methods=['GET'])
def show():
    result = list(db.todolist.find({},{'_id':0}))
    return jsonify({'result':'success', 'todo':result})


@app.route('/list', methods=['POST'])
def post():
    todo = request.form['todo_receive']
    todo_one = {
        'todo':todo
    }
    db.todolist.insert_one(todo_one)
    return jsonify({'result':'success', 'msg':'등록되었습니다.'})


@app.route('/list/del', methods=['POST'])
def delete():
    todo = request.form['content']
    db.todolist.delete_one({'todo':todo})
    return jsonify({'result':'success', 'msg':'삭제되었습니다.'})


if __name__ == '__main__':
    app.run()