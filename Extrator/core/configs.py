from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

db_password = os.environ['db_password']
db_uri = f'postgresql+psycopg2://synapse_user:{db_password}@localhost:5432/synapse'

engine = create_engine(db_uri)
Session = sessionmaker(bind=engine, autocommit=False, autoflush=False, expire_on_commit=False)
session = Session()

