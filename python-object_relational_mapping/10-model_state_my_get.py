#!/usr/bin/python3
"""Print the State object with a given name from the database"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    """Fetch a state by name and print its id or Not found"""
    if len(sys.argv) != 5:
        return

    user, password, db_name, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    engine = create_engine(
        f"mysql+mysqldb://{user}:{password}@localhost/{db_name}",
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    # SQL injection safe: using filter with parameters
    state = session.query(State).filter(State.name == state_name).first()

    if state:
        print(state.id)
    else:
        print("Not found")

    session.close()


if __name__ == "__main__":
    main()
