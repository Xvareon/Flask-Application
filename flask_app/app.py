from flask import Flask, render_template, request, redirect, url_for
from models import Product, Base
from init_db import engine, session

app = Flask(__name__)
Base.metadata.create_all(engine)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/products')
def products_index():
    products = session.query(Product).all()
    return render_template('products_index.html', products=products)


@app.route('/products/create', methods=['GET'])
def products_create_form():
    if request.method == 'GET':
        return render_template('products_create.html')


@app.route('/products/create', methods=['POST'])
def products_create():
    if request.method == 'POST':
        name = request.form['name']
        variant = request.form['variant']
        qty = request.form['qty']
        price = request.form['price']
        description = request.form['description']

        new_product = Product(
            name=name,
            variant=variant,
            qty=qty,
            price=price,
            description=description
        )

        session.add(new_product)
        session.commit()
        return redirect(url_for('products_index'))

    # If an error occurred
    return redirect(url_for('index'))

@app.route('/products/update/<int:id>', methods=['GET'])
def products_update_form(id):
    product = session.query(Product).filter(Product.id == id).first()
    if product:
        return render_template('products_update.html', product=product)
    else:
        return "Product not found", 404


@app.route('/products/update/<int:id>', methods=['POST'])
def products_update(id):
    product = session.query(Product).filter(Product.id == id).first()
    if product:

        product.name = request.form['name']
        product.variant = request.form['variant']
        product.qty = request.form['qty']
        product.price = request.form['price']
        product.description = request.form['description']

        session.commit()
        return redirect(url_for('products_index'))
    else:
        return "Product not found", 404


if __name__ == '__main__':
    app.run(debug=True)