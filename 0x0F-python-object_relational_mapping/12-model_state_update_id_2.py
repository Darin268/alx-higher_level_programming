#!/usr/bin/python3
"""
Script that changes the name of a State object from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Create engine for database connection
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    # Create configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create Session
    session = Session()

    # Query State object with id = 2
    state_to_update = session.query(State).filter(State.id == 2).first()

    # Update name of State object to "New Mexico"
    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()

    # Close session
    session.close()
