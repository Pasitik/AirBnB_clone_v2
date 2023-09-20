#!/usr/bin/python3
from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import os


class DBStorage:
    __engine = None
    __session = None


    def __init__(self):
        env = os.environ
        self.__engine = create_engine(
                'mysql+mysqldb://{}:{}@{}:3306/{}'.format(
                    env.get("HBNB_MYSQL_USER"), env.get("HBNB_MYSQL_PWD"),
                    env.get("HBNB_MYSQL_HOST"), env.get("HBNB_MYSQL_DB"),
                    pool_pre_ping=True
                    ))
        if os.environ.get("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        if cls:
            result = self.__session.query(cls).all()
        else:
            result = self.__session.query((State, City).outerjoin(City)).all()

        query_result = {}
        for obj in result:
            if cls is not None:
                key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                obj.__dict__ = obj.to_dict()
                query_result[key] = obj
            else:
                for row in obj:
                    key = '{}.{}'.format(row.__class__.__name__, row.id)
                    query_result[key] = row

        return query_result

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        from models.user import User
        from models.place import Place

        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session)
        self.__session = Session()
