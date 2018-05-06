from flask import Flask, render_template, jsonify, redirect, url_for, request
from sqlalchemy import create_engine, asc
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Meters, MeterData, Base

app = Flask(__name__)

# Connect to Database and create database session
engine = create_engine('sqlite:///meter.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Show all Meters
@app.route('/')
@app.route('/meters/')
def showMeters():
	meterss = session.query(Meters).order_by(asc(Meters.label)) 
	return render_template('meters.html', meterss=meterss)

## Show Each Meter Separately
@app.route('/meters/<int:meters_id>/')
def viewMeter(meters_id):
    meters = session.query(Meters).filter_by(id=meters_id).one()
    items = session.query(MeterData).filter_by(meters_id=meters_id).all()
    return render_template('viewMeter.html', items=items, meters=meters)

# JSON APIs to view MeterData Information
@app.route('/meters/<int:meters_id>/JSON/')
def viewMeterJSON(meters_id):
    meters = session.query(Meters).filter_by(id=meters_id).one()
    items = session.query(MeterData).filter_by(meters_id=meters_id).all()
    return jsonify(meter_data_entries=[i.serialize for i in items])
    
# JSON APIs to view Meters Information
@app.route('/meters/JSON/')
def viewAllMeters():
	meters = session.query(Meters).order_by(asc(Meters.label)) 
	return jsonify(meters=[m.serialize for m in meters])



if __name__ == '__main__':
   app.debug = True
   app.run(host='0.0.0.0', port=5000)
