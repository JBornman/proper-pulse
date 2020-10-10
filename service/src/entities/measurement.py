from sqlalchemy import Column, String, Numeric
from marshmallow import Schema, fields
from .entity import Entity, Base


class Measurement(Entity, Base):
    __tablename__ = 'measurement'

    title = Column(String)
    description = Column(String)
    systolic = Column(Numeric)
    diastolic = Column(Numeric)
    pulse = Column(Numeric)

    def __init__(self, title, description, systolic, diastolic,pulse, created_by):
        Entity.__init__(self, created_by)
        self.title = title
        self.description = description
        self.systolic = systolic
        self.diastolic = diastolic
        self.pulse = pulse


class MeasurementSchema(Schema):
    id = fields.Number()
    title = fields.Str()
    description = fields.Str()
    systolic = fields.Number()
    diastolic = fields.Number()
    pulse = fields.Number()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    last_updated_by = fields.Str()