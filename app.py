# Import dependencies
from flask import Flask, jsonify

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

import datetime as dt
import numpy as np
import pandas as pd

# Create SQLite engine (Access Database)
engine = create_engine("sqlite:///hawaii.sqlite")

# Reflect database
Base = automap_base()

# Reflect table
Base.prepare(engine, reflect=True)

# Variables referencing to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create a session link from Python to DB
session = Session(engine)

# Create new Flask instance
app = Flask(__name__)

# Flask route - root/welcome
@app.route('/')
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')

# Precipitation Route
@app.route('/api/v1.0/precipitation')
def precipitation():
	# Calculate date one year ago from the most recent date in DB
	prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)

	# Get the date and precipitation for the previous year
	precipitation = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= prev_year).all()

	# Format query results into JSON format
	precip = {date: prcp for date, prcp in precipitation}

	return jsonify(precip)

# Stations route
@app.route("/api/v1.0/stations")
def stations():
	# get all of the stations in DB
    results = session.query(Station.station).all()

    # Unravel query data into one-dimensional array and then put it into a list
    stations = list(np.ravel(results))

    return jsonify(stations=stations)

# Temperature observations route
@app.route("/api/v1.0/tobs")
def temp_monthly():
	# Calculate date one year ago from the most recent date in DB
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    # Query the primary station for all the temperature observations from the previous year
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()

    # Unravel query data into one-dimensional array and then put it into a list
    temps = list(np.ravel(results))

    return jsonify(temps=temps)

# Report on the minimum, average, and maximum temperatures
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    
    if not end:
	    results = session.query(*sel).\
	        filter(Measurement.date >= start).all()
	    temps = list(np.ravel(results))
	    return jsonify(temps=temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))

    return jsonify(temps)
