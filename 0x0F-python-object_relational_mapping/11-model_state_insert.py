#!/usr/bin/python3
"""
Script that adds the State object "Louisiana" to the database hbtn_0e_6_usa
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

    # Create a new State object for Louisiana
    new_state = State(name="Louisiana")

    # Add the new State object to the session
    session.add(new_state)

    # Commit the session to the database to add the new State object
    session.commit()

    # Print the id of the new State object
    print(new_state.id)

    # Close the session
    session.close()
