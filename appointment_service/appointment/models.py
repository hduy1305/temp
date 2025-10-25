from mongoengine import Document, IntField, DateTimeField

class Appointment(Document):
    patient_id = IntField(required=True)
    doctor_id  = IntField(required=True)
    date       = DateTimeField(required=True)

    meta = {
        'collection': 'appointments',   # Tên collection trong MongoDB
        'indexes': [
            'patient_id',
            'doctor_id',
            'date'
        ]
    }
