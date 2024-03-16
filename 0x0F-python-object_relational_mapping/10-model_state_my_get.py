#!/usr/bin/python3
"""
Script that prints the State object with the name passed as argument
from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Create an engine for database connection
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3])
    )

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query State object with the provided state name
    state_name = sys.argv[4]
    state = session.query(State).filter(State.name == state_name).first()

    # Print the id of the State object if found, otherwise print "Not found"
    if state:
        print(state.id)
    else:
        print("Not found")

    # Close the session
    session.close()
