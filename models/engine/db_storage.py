from sqlalchemy import create_engine, session_maker
import os


Class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_enginie('mysql+mysqldb://{}:{}@{}:3306/{}'.format("hbnb_dev", "hbnb_dev_pwd", "localhost", "hbnb_dev_db"), pool_pre_ping=True)
        if os.env("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)
        

