from tokenize import String
import random
from setupDB import *

class Trashtalk(object):
    def __init__(self, list):
        self.list = list

    @staticmethod
    def from_dict(source):
        # [START_EXCLUDE]
        trashtalk = Trashtalk(source[u'list'])
        return trashtalk
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
            f'Trashtalk(\
                list={self.list}, \
            )'
        )
# [END firestore_data_custom_type_definition]
# [END custom_class_def]

def save(message):
    ref = db.collection(u'files').document(u'trashtalks')
    ref.update({u'list': firestore.ArrayUnion([message])})
def get():
    docs = db.collection(u'files').document(u'trashtalks').get()
    trashtalk = Trashtalk.from_dict(docs.to_dict())
    randomLine = random.randint(0,len(trashtalk.list) - 1)
    return trashtalk.list[randomLine]