from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class Day(db.Model):
    __tablename__ = "days"
    id = db.Column(db.Integer, primary_key=True)
    month_id = db.Column(db.Integer, db.ForeignKey("months.id"))
    month_name = db.Column(db.String, nullable=False)
    number = db.Column(db.Integer, nullable=False)
    active = db.Column(db.Boolean, nullable=False)
   
    def serialize_for_day(self):
        return {
            "id": self.id,
            "month": self.month_name,
            "number": self.number,
            "active": self.active,
             # "timeslots": [slot.serialize_for_day() for slot in self.timeslots]
        }

    def serialize_for_month(self):

        return {
            "number": self.number,
            "active": self.active
        }


class Month(db.Model):
    __tablename__ = "months"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    number = db.Column(db.Integer, nullable=False)
    num_days = db.Column(db.Integer, nullable=False)
    active = db.Column(db.Boolean, nullable=False)
    days = db.relationship("Day", cascade="delete")

    def serialize_for_month(self):
        return {
            "id": self.id,
            "name": self.name,
            "active": self.active,
            "days": [day.serialize_for_month() for day in self.days]
        }

class Timeslots(db.Model):
    __tablename__ = "timeslots"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.String, nullable=False)
    start_time = db.Column(db.Integer, nullable=False)
    end_time = db.Column(db.Integer, nullable=False)

    # Course for timeslot: One-to-many relationship
    # course = db.relationship("Courses", cascade="delete")

    def __init__(self, **kwargs):
        """
        Initialize Timeslot object
        """
        self.date = kwargs.get("date")
        self.start_time = kwargs.get("start_time")
        self.end_time = kwargs.get("end_time")

    def serialize(self):
        """
        Serialize Timeslot object
        """
        return {
            "id": self.id,
            "date": self.date,
            "start_time": self.start_time,
            "end_time": self.end_time
        }

        
