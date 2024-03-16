#!/usr/bin/python3
"""Adds the State "California" with the City "San Francisco" to the database"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(username, password, db_name),
                           pool_pre_ping=True)

    # Create all the tables in the database (if not existing)
    Base.metadata.create_all(engine)

    # Create a Session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create a new State
    california = State(name="California")

    # Create a new City
    san_francisco = City(name="San Francisco")

    # Add the City to the State
    california.cities.append(san_francisco)

    # Add the State and City to the session
    session.add(california)

    # Commit changes to the database
    session.commit()

    # Close the session
    session.close()
