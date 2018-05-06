from sqlalchemy import MetaData, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.mysql import TIMESTAMP
from datetime import date, datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine



Base = declarative_base()


class Meters(Base):
    __tablename__ = 'meters'

    id = Column(Integer, primary_key=True)
    label = Column(String(250), nullable=False)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
              'label': self.label,
            
              'id': self.id,
		}
            

class MeterData(Base):
    __tablename__ = 'meter_data'

    id = Column(Integer, primary_key=True)
    timestamp = Column(String(250),default=datetime.utcnow())
    meters_id = Column(Integer, ForeignKey('meters.id'))
    meters = relationship(Meters)
    value = Column(Integer)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
 
        return {
            
              'id': self.id,

              'value' : self.value,




              'meters_id' : self.meters_id,

              'timestamp' : self.timestamp,



        }

    
    


engine = create_engine('sqlite:///meter.db')


Base.metadata.create_all(engine)