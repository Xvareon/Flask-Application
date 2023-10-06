import psycopg2
import environ
env = environ.Env()
environ.Env.read_env()

conn = psycopg2.connect(database=env("DB_NAME"), host=env("DB_HOST"), user=env("DB_USER"), password=env("DB_PASSWORD"), port=env("DB_PORT"))
cur = conn.cursor()

# one model table
cur.execute('''CREATE TABLE IF NOT EXISTS products (id serial PRIMARY KEY, name varchar(100), variant integer, qty integer, price float, description varchar(255));''')

conn.commit()
cur.close()
conn.close()
