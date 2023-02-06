from flask import Flask
import sqlite3

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

@app.route("/")
def hello():
    return "Hello World!"

DATABASE = 'db.sqlite'
def connect_db():
    return sqlite3.connect(DATABASE)


#criação da tabela
def init_db():
    with connect_db() as con:
        con.execute('CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)')

#criação de valores
def create_user(name):
    with connect_db() as con:
        con.execute("INSERT INTO users (name) VALUES (?)", (name,))


        #pesquisa de dados

def get_users():
     with connect_db() as con:
         cursor = con.execute("SELECT * FROM users")
     return cursor.fetchall()

        #atualização de dados

def update_user(id, name):
     with connect_db() as con:
        con.execute("UPDATE users SET name = ? WHERE id = ?", (name, id))

        #eliminação de dados

def delete_user(id):
    with connect_db() as con:
        con.execute("DELETE FROM users WHERE id = ?", (id,))


if __name__ == "__main__":
    init_db()
    app.run()

