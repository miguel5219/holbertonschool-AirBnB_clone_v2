#!/usr/bin/python3
""" module that define a class to manage database storage """

from sqlalchemy import create_engine
from os import getenv
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy.orm import sessionmaker, scoped_session

class DBStorage:
    """ class DBStorage """

    __engine = None
    __session = None

    def __init__(self):
        """ this is the constructor """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            getenv("HBNB_MYSQL_USER"),
            getenv("HBNB_MYSQL_PWD"),
            getenv("HBNB_MYSQL_HOST"),
            getenv("HBNB_MYSQL_DB")),
            pool_pre_ping=True)

        if getenv("HBNB_ENV") == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ the query on the current database session """

        obj_dict = {}
        classes = [User, State, City, Amenity, Place, Review]

        if cls:
            objects = self.__session.query(cls).all()

            for i in objects:
                obj_dict[type(i).__name__ + "." + i.id] = i
        else:
            for elem in classes:
                objects = self.__session.query(elem).all()
                for i in objects:
                    obj_dict[type(i).__name__ + "." + i.id] = i

        return obj_dict

    def new(self, obj):
        """ add object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ commit changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete from the current database session obj if not None """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ creating tables and session """
        Base.metadata.create_all(self.__engine)
        session_fact = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_fact)
        self.__session = Session()

    def close(self):
        """ close session """
        self.__session.close()
