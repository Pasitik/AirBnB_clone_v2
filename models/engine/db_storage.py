from sqlalchemy import create_engine, session_maker
import os


Class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_enginie('mysql+mysqldb://{}:{}@{}:3306/{}'.format("hbnb_dev", "hbnb_dev_pwd", "localhost", "hbnb_dev_db"), pool_pre_ping=True)
        if os.env("HBNB_ENV") == "test":
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
        from models import State, City, Amenity, Review, User, Place
        
		Base.metadata.create_all(engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session)
		self.__session = Session()

