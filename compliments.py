from tokenize import String
import random
from setupDB import *

class Compliment(object):
    def __init__(self, list):
        self.list = list

    @staticmethod
    def from_dict(source):
        # [START_EXCLUDE]
        compliment = Compliment(source[u'list'])
        return compliment
        # [END_EXCLUDE]

    def to_dict(self):
        # [START_EXCLUDE]
        dest = {
            u'list': self.list,
        }
        return dest
        # [END_EXCLUDE]

    def __repr__(self):
        return (
            f'Compliment(\
                list={self.list}, \
            )'
        )
# [END firestore_data_custom_type_definition]
# [END custom_class_def]

def saveCompliment(message):
    ref = db.collection(u'files').document(u'compliments')
    ref.update({u'list': firestore.ArrayUnion([message])})
def getCompliment():
    docs = db.collection(u'files').document(u'compliments').get()
    compliment = Compliment.from_dict(docs.to_dict())
    randomLine = random.randint(0,len(compliment.list) - 1)
    return compliment.list[randomLine]
