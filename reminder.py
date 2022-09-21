from tokenize import String
import random
from setupDB import *

class Reminder(object):
    def __init__(self, description):
        self.description = description

    @staticmethod
    def from_dict(source):
        # [START_EXCLUDE]
        description = Reminder(source[u'description'])
        return description
        # [END_EXCLUDE]

    def to_dict(self):
        # [START_EXCLUDE]
        dest = {
            u'description': self.description,
        }
        return dest
        # [END_EXCLUDE]
# [END firestore_data_custom_type_definition]
# [END custom_class_def]

def saveReminder(id, reminder):
    data = {
    u'description': reminder
    }
    db.collection(u'reminders').document(f'{id}').set(data)
def getReminder():
    docs = db.collection(u'reminders').document(u'123123').get()
    reminder = Reminder.from_dict(docs.to_dict())
    return reminder.description