# Import the dependencies.
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt

from flask import Flask, jsonify, render_template
from flask_cors import CORS



#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///SpotifyDB.sqlite")
# engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost:5432/Spotify_DB")
# reflect an existing database into a new model
Base = automap_base()



# reflect the tables
Base.prepare(autoload_with = engine)
# print(Base.classes.keys())
# Save reference to the table
spotify_data = Base.classes.spotify_data
db_columns = Base.classes.spotify_data.__table__.columns.keys()
print(db_columns)

# Create our session (link) from Python to the DB
# session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__, template_folder="")
# app = Flask(__name__)
CORS(app)


#################################################
# Flask Routes
#################################################

@app.route("/help")
def welcome():
    """List of all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/all_data<br/>"
        f"/api/by_decade<br/>"
        f"/api/by_a_decade/<decade_name><br/>"
        f"/api/by_analysis<br/>"
        
    )

@app.route("/")
def index():
    """Render the home page"""
    return render_template('decade.html')

@app.route("/api/all_data")
def all_data():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    

    results = [x.__dict__ for x in session.query(spotify_data)]
    for result in results:
        del result['_sa_instance_state']
    session.close()

    return jsonify(results)


@app.route("/api/by_decade")
def by_decade():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    
    """Return a list of all precipitation data for last year"""
    # Query all data from past year
    results = session.query(spotify_data.decade).distinct().all()
    
    session.close()
    all_names = list(np.ravel(results))
    all_data = []
    for decade in all_names:
        name_dict = {}
        name_dict["decade"] = int(decade)
        all_data.append(name_dict)
  
    return jsonify(all_data)



@app.route("/api/by_a_decade/<decade_name>")
def by_a_decade(decade_name):
    """ search by decade """
    session = Session(engine)
    # Query all decades
    query_results = session.query(spotify_data).filter(spotify_data.decade == decade_name)
    results = [{"id": x.id, "decade": x.decade} for x in query_results]

    
    session.close()
    return jsonify(results)

@app.route("/api/by_analysis")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    
    """Return a list of names of all stations"""
    # Query all data from past year
    results = session.query((spotify_data.song_name)).all()
    
    session.close()
   
    
    all_songs = []
    for song in results:
        song_dict = {}
        song_dict["Song"] = song[0]
        all_songs.append(song_dict)

    return jsonify(all_songs)
    
if __name__ == '__main__':
    app.run(debug=True)
      