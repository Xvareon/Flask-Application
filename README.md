## Flask application made with Python, psycopg2, Jinja, SQLAlchemy and PostgreSQL.

## PROJECT DEPENDENCIES
- [Python 3 +](https://www.python.org/downloads/)
- [PyCharm (IDE)](https://www.jetbrains.com/pycharm/download/?section=windows)
- [PostgreSQL](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads)
- [Table Plus](https://tableplus.com/windows) or [pgAdmin 4](https://www.pgadmin.org/download/pgadmin-4-windows/)

## PROJECT SETUP
- Upon python installation, ensure that it is added to PATH
- Create a folder named YourProjectName
- Open your PyCharm and navigate to the lower left corner to open your terminal or just use " Alt+F12 "
- Enter:" pip install flask "
- Enter:" pip install psycopg2 " then restart the terminal
- Enter:" pip install python-dotenv " then restart the terminal
- Enter:" pip install SQLAlchemy " then restart the terminal
- Create a new python package/directory/folder inside YourProjectName and name it YourAppName
- If a python file named " `__init__.py` " is created, rename it to " init_db.py ", otherwise, create it manually inside the YourAppName folder/package

## DB SETUP
- Ensure psycopg2 is installed
- Configure your PostgreSQL management studio
- Create a database and take note of its name

- Also pip install django-environ (for .env)
- Create a .env file beside your settings.py and fill it with it like this (no single quotes):
```
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```
- Add this .env file to your gitignore if you are using git

- Create a file named " 'models.py' " and fill it with your models, similar to this example:
```python
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    variant = Column(Integer)
    qty = Column(Integer)
    price = Column(Float)
    description = Column(String(255))
```

- Configure the init_db.py to look similar to this:
```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, Product

# Load environment variables
import environ
env = environ.Env()
environ.Env.read_env()

# Create engine
db_url = f'postgresql://{env("DB_USER")}:{env("DB_PASSWORD")}@{env("DB_HOST")}:{env("DB_PORT")}/{env("DB_NAME")}'
engine = create_engine(db_url)

# Create tables
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Commit the session and close it
session.commit()
session.close()
```
- Open the terminal, make sure you are in the same directory with the init_db.py (cd YourAppName) and run the command " python init_db.py " to migrate the table
- Create a new python file inside YourAppName folder/package and name it " app.py "
- There, you will have to define your db connection again, you will also configure your application's routes and main functions there
- Create a templates folder/package/directory in YourAppName and add your html pages there
- Open your terminal and make sure you are in your app directory or use cd YourAppName
- Then run the command:" flask run "

## AND YOU ARE SET!
- Make sure your installed python packages/dependency versions do not conflict with other python applications

## =================================================

# Flask
=====

Flask is a lightweight [WSGI](https://wsgi.readthedocs.io/) web application framework. It is designed
to make getting started quick and easy, with the ability to scale up to
complex applications. It began as a simple wrapper around [Werkzeug](https://werkzeug.palletsprojects.com/)
and [Jinja](https://jinja.palletsprojects.com/) and has become one of the most popular Python web
application frameworks.

Flask offers suggestions, but doesn't enforce any dependencies or
project layout. It is up to the developer to choose the tools and
libraries they want to use. There are many extensions provided by the
community that make adding new functionality easy.


## Installing

Install and update using pip:

```

    $ pip install -U Flask


## A Simple Example
----------------

```python

    # save this as app.py
    from flask import Flask

    app = Flask(__name__)

    @app.route("/")
    def hello():
        return "Hello, World!"
```

```

    $ flask run
      * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```


## Contributing
------------

For guidance on setting up a development environment and how to make a
contribution to Flask, see the [contributing guidelines](https://github.com/pallets/flask/blob/main/CONTRIBUTING.rst)


## Donate
------

The Pallets organization develops and supports Flask and the libraries
it uses. In order to grow the community of contributors and users, and
allow the maintainers to devote more time to the projects, [please
donate today](https://palletsprojects.com/donate).


## Links
-----

-   Documentation: https://flask.palletsprojects.com/
-   Changes: https://flask.palletsprojects.com/changes/
-   PyPI Releases: https://pypi.org/project/Flask/
-   Source Code: https://github.com/pallets/flask/
-   Issue Tracker: https://github.com/pallets/flask/issues/
-   Chat: https://discord.gg/pallets
