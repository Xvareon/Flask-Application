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