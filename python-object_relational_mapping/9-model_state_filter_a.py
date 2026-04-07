#!/usr/bin/python3
"""List all State objects containing the letter 'a' from the database"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    """Connect to the database and fetch states with 'a' in their name"""
    if len(sys.argv) != 4:
        return

    user, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine(
        f'mysql+mysqldb://{user}:{password}@localhost/{db_name}',
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    # Filter states containing 'a', case-sensitive as per example
    states = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()

    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()


if __name__ == "__main__":
    main()
