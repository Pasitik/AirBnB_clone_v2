from sqlalchemy import create_engine, session_maker

Class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_enginie('mysql+mysqldb://{}:{}@{}:3306/{}'.format("hbnb_dev", "hbnb_dev_pwd", "localhost", "hbnb_dev_db"), pool_pre_ping=True)
        self.__session = session_maker(bind=engine) 
        

