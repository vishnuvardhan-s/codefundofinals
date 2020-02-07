# Access to this file : ZoneRepresentative
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

print('Looking for Voter-IDs')

try:
    text,id = reader.read()
    client = MongoClient('mongodb+srv://root:root@cluster0-6qril.mongodb.net/test?retryWrites=true&w=majority')
    db = client.get_database('rag')
    records = db.get_collection('votingsystem')
    records.update_one({'voterid':text},{'$set':update})
    print('Voter status updated successfully!')
finally:
    GPIO.cleanup()
