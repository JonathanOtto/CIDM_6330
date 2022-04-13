from importlib.metadata import metadata
from sqlalchemy import create_engine, ForeignKey, select, Table
from sqlalchemy import Column, Date, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite:///users.db', echo=False)
connection = engine.connect()
metadata = MetaData()

users = Table("users", metadata, autoload=True, autoload_with=engine)
stmt = select([users])
results = connection.execute(stmt).fetchall()
#print (results[0])

class Login:
    type = ""
    def login(self,id):
        for x in range(len(results)):
            row = results[x]
            if(id == row[2]):
                self.type = row[3]
        return(self.type)



            