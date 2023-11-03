from models import Dog
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.models import Dog, Base

def create_table(base):
    pass
def create_table(Base, engine):
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()

def save(session, dog):
    pass
    session.add(dog)
    session.commit()

def get_all(session):
    pass
    return session.query(Dog).all()

def find_by_name(session, name):
    pass
    return session.query(Dog).filter_by(name=name).first()

def find_by_id(session, id):
    pass
    return session.query(Dog).filter_by(id=id).first()

def find_by_name_and_breed(session, name, breed):
    pass
    return session.query(Dog).filter_by(name=name, breed=breed).first()

def update_breed(session, dog, breed):
    pass
    dog.breed = breed
    session.commit()