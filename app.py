import sqlite3

from flask import Flask, render_template, g

DATABASE = './my_database.sqlite'
app = Flask(__name__, template_folder='./templates')


def make_dicts(cursor, row):
    return dict((cursor.description[idx][0], value)
                for idx, value in enumerate(row))


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = g._database.row_factory = make_dicts
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/')
def main_page():
    return render_template('task_list.html', taks=[{'id': 5, 'name': "placki"}, {'id': 2, 'name': "placki"}])


if __name__ == '__main__':
    app.run(debug=True)
