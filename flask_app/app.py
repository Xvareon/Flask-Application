import psycopg2
import environ

env = environ.Env()
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


def db_conn():
    conn = psycopg2.connect(database=env("DB_NAME"), host=env("DB_HOST"), user=env("DB_USER"),
                            password=env("DB_PASSWORD"), port=env("DB_PORT"))
    return conn


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/products')
def products_index():
    conn = db_conn()
    cur = conn.cursor()
    cur.execute('''SELECT * FROM products''')
    products = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('products_index.html', products=products)


@app.route('/products/create', methods=['GET'])
def products_create_form():
    if request.method == 'GET':
        return render_template('products_create.html')


@app.route('/products/create', methods=['POST'])
def products_create():
    if request.method == 'POST':
        conn = db_conn()
        cur = conn.cursor()
        name = request.form['name']
        variant = request.form['variant']
        qty = request.form['qty']
        price = request.form['price']
        description = request.form['description']
        cur.execute(
            'INSERT INTO products (name, variant, qty, price, description) VALUES (%s, %s, %s, %s, %s)',
            (name, variant, qty, price, description)
        )
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('products_index'))

    # If an error occurred
    return redirect(url_for('index'))
