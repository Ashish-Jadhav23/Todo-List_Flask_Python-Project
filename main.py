from flask import Flask, render_template, request, redirect, url_for
from model import db, Todo

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
def welcome():
    todo_list = Todo().get_todo_list()
    return render_template('base.html', todo_list=todo_list)

@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    Todo().add_todo(title)
    return redirect(url_for("welcome"))

@app.route("/update/<int:todo_id>")
def update(todo_id):
    Todo().update_todo_status(todo_id)
    return redirect(url_for("welcome"))

@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    Todo().delete_todo(todo_id)
    return redirect(url_for("welcome"))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=9000)
