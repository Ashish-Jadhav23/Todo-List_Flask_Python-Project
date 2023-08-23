from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)

    def get_todo_list(self):
        return Todo.query.all()

    def add_todo(self, title):
        new_todo = Todo(title=title, complete=False)
        db.session.add(new_todo)
        db.session.commit()

    def update_todo_status(self, todo_id):
        todo = Todo.query.get(todo_id)
        if todo:
            todo.complete = not todo.complete
            db.session.commit()

    def delete_todo(self, todo_id):
        todo = Todo.query.get(todo_id)
        if todo:
            db.session.delete(todo)
            db.session.commit()
