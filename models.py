from datetime import datetime
import mongoengine

from mongoengine import *


from mongoengine import EmbeddedDocument, Document
from mongoengine.fields import ObjectId, ReferenceField, BooleanField, DateTimeField, EmbeddedDocumentField, ListField, StringField
#mongoengine.connect('Home_t8', 'localhost:27017')

class Contact(Document):  
    fullname = StringField(max_length=150)
    mail = StringField(max_length=150)
    log_field = BooleanField(default=False)