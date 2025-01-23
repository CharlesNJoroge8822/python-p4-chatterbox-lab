# server/seed.py

from app import app, db
from models import Message

with app.app_context():
    # Create some sample messages
    message1 = Message(body="Hello, World!", username="Ian")
    message2 = Message(body="Goodbye, World!", username="Alex")

    # Add to the database
    db.session.add_all([message1, message2])
    db.session.commit()
