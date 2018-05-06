from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Meters, MeterData, Base

engine = create_engine('sqlite:///meter.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

#create Meters
meters1 = Meters(label = "X")

session.add(meters1)
session.commit()

meters2 = Meters(label = "B")

session.add(meters2)
session.commit()

meters3 = Meters(label = "A")

session.add(meters3)
session.commit()

meters4 = Meters(label = "C")

session.add(meters4)
session.commit()


# create MeterData linking to Meters
meter_data2 = MeterData(meters=meters2, value = "20")

session.add(meter_data2)
session.commit()

meter_data1 = MeterData(meters=meters1, value = "5")

session.add(meter_data1)
session.commit()

meter_data3 = MeterData(meters=meters3, value = "25")

session.add(meter_data3)
session.commit()


meter_data4 = MeterData(meters=meters1, value = "2")

session.add(meter_data4)
session.commit()

meter_data5 = MeterData(meters=meters2, value = "52")

session.add(meter_data5)
session.commit()


print "Added"