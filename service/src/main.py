# coding=utf-8

from .entities.entity import Session, engine, Base
from .entities.measurement import Measurement

# generate database schema
Base.metadata.create_all(engine)

# start session
session = Session()

# check for existing data
measurements = session.query(Measurement).all()

if len(measurements) == 0:
    # create and persist mock measurement
    python_measurement = Measurement("Test insert", "Here we instert some test data", "script")
    session.add(python_measurement)
    session.commit()
    session.close()

    # reload measurements
    measurements = session.query(Measurement).all()

# show existing measurements
print('### measurements:')
for measurement in measurements:
    print(f'({measurement.id}) {measurement.title} - {measurement.description}')
