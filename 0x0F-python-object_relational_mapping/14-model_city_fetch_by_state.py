#!/usr/bin/python3
"""Print all City objects from the database hbtn_0e_14_usa."""

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Create engine to connect to MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, db_name),
                           pool_pre_ping=True)

    # Create session maker bound to the engine
    Session = sessionmaker(bind=engine)

    # Create session
    session = Session()

    # Query all City objects
    cities = session.query(City).order_by(City.id).all()

    # Print results
    for city in cities:
        print("{}: ({}) {}".format(city.state.name, city.id, city.name))

    # Close session
    session.close()
