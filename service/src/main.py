from flask import Flask, jsonify, request
from flask_cors import CORS
from .entities.entity import Session, engine, Base
from .entities.measurement import Measurement, MeasurementSchema

# creating the Flask application
app = Flask(__name__)
CORS(app)

# if needed, generate database schema
Base.metadata.create_all(engine)


@app.route('/measurements')
def get_measurements():
    # fetching from the database
    session = Session()
    measurement_objects = session.query(Measurement).all()

    # transforming into JSON-serializable objects
    schema = MeasurementSchema(many=True)
    measurements = schema.dump(measurement_objects)

    # serializing as JSON
    session.close()

    # return jsonify(measurements.data)
    return jsonify(measurements)

@app.route('/measurements', methods=['POST'])
def add_measurement():
    # mount measurement object
    posted_measurement = MeasurementSchema(only=('title', 'description','systolic','diastolic','pulse'))\
        .load(request.get_json())

    # measurement = Measurement(**posted_measurement.data, created_by="HTTP post request")
    measurement = Measurement(**posted_measurement, created_by="HTTP post request")

    # persist measurement
    session = Session()
    session.add(measurement)
    session.commit()

    # return created measurement
    # new_measurement = MeasurementSchema().dump(measurement).data
    new_measurement = MeasurementSchema().dump(measurement)
    session.close()
    return jsonify(new_measurement), 201