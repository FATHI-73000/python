import sqlite3
from bottle import route, run, request, template

# ----------------------------

# Initialiser la base de données
# ----------------------------
def init_db():
    with sqlite3.connect('users.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
        ''')
        conn.commit()

init_db()

# Routes

# Page d'accueil
@route('/')
def home():
    return template('home')

# Page dynamique avec paramètre
@route('/hello/<name>')
def hello(name):
    return template('hello', name=name)

# Formulaire (GET)
@route('/form')
def form():
    return template('form')

# Traitement du formulaire (POST)
@route('/form', method='POST')
def form_submit():
    name = request.forms.get('name')
    with sqlite3.connect('users.db') as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name) VALUES (?)", (name,))
        conn.commit()
    return template('hello', name=name)

# Liste des utilisateurs avec filtrage "show"
@route('/users')
def list_users():
    show = request.query.show or 'all'

    match show:
        case 'all':
            db_query = "SELECT id, name FROM users"
        case 'recent':
            db_query = "SELECT id, name FROM users ORDER BY id DESC LIMIT 5"
        case _:
            return template('message', message="Paramètre 'show' invalide. Utilisez 'all' ou 'recent'.")

    with sqlite3.connect('users.db') as conn:
        cursor = conn.cursor()
        cursor.execute(db_query)
        users = cursor.fetchall()

    return template('users', users=users)


# Lancer le serveur
run(host='localhost', port=8080, debug=True)
